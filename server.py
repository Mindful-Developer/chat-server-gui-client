import asyncio
import socket
from utils.events import Event, EventQueue, EventType, Client
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Server:
    clients: dict = field(default_factory=dict)
    event_queue: EventQueue = field(default_factory=EventQueue)
    server: socket.socket = field(default_factory=socket.socket)
    host_port: tuple = field(default_factory=tuple)
    event_loop: asyncio.AbstractEventLoop = field(default_factory=asyncio.get_event_loop)

    async def run(self):
        self.server.bind(self.host_port)
        self.event_loop.create_task(self.accept())
        await self.process_events()

    async def accept(self):
        print('Server listening...')
        while True:
            try:
                print('Waiting for client...')
                self.server.listen(64)
                client, address = await self.event_loop.sock_accept(self.server)
                print(f'Client {address} connecting...')
                self.event_loop.create_task(self.get_events(client))
            except BlockingIOError:
                pass
            await asyncio.sleep(0.1)

    async def get_events(self, client):
        user_id = None
        print("User connected.")
        while True:
            print('Waiting for message...')
            try:
                msg = await self.event_loop.sock_recv(client, 4096)
            except OSError:
                print('Client disconnected.')
                break
            print(f'got message {msg}')
            if msg:
                event = Event.decode(msg)
                event.client = Client(client, event.sender)
                if event.type == EventType.CONNECT:
                    user_id = event.data
                self.event_queue.push(event)
            else:
                self.event_queue.push(Event(EventType.DISCONNECT, '', client=Client(client, user_id)))
                break
            await asyncio.sleep(0.1)

    async def connect(self, event):
        if event.data in self.clients:
            event.client.send(Event(EventType.CONNECT_ERR, 'Username already taken.'))
            print(f'Client {event.data} already connected.')
            event.client.close()
        else:
            self.clients[event.data] = event.client
            event.client.send(Event(EventType.CONNECT_OK, ''))
            await self.send_message(Event(EventType.SERVER, f'User {event.data} connected.'))
            print(f'Client {event.data} connected.')

    async def process_events(self):
        while True:
            if self.event_queue:
                event = self.event_queue.pop()
                print(f"processing event {event.type} {event.data}")
                if event.type == EventType.OUT_MSG:
                    await self.send_message(event)
                elif event.type == EventType.DISCONNECT:
                    await self.disconnect(event)
                elif event.type == EventType.LIST:
                    await self.list_users(event)
                elif event.type == EventType.CONNECT:
                    await self.connect(event)
                else:
                    print(f'Unknown event type {event.type}')
            await asyncio.sleep(0.1)

    async def send_message(self, event):
        print(f'sending message {event.type} {event.data}')
        if event.type == EventType.OUT_MSG:
            event.type = EventType.IN_MSG
            event.data = f'{datetime.now().strftime("%Y-%m-%d %H:%M")} > {event.sender}: {event.data}'
        else:
            event.data = f'{datetime.now().strftime("%Y-%m-%d %H:%M")} > {event.data}'

        if event.recipient and event.recipient in self.clients:
            client = self.clients[event.recipient]
            event.data = f'{event.data} (private)'
            client.send(event)
            event.data = f'{event.data} (to {event.recipient})'
            event.client.send(event)

        elif event.recipient:
            event.client.send(Event(EventType.ERROR, f'User {event.recipient} not found.'))
        else:
            for client in self.clients.values():
                client.send(event)

    async def disconnect(self, event):
        print(f'disconnecting client {event.client.user_ID}')
        client = self.clients.pop(event.client.user_ID)
        client.close()
        print(f'Client {event.client.user_ID} disconnected.')
        await self.send_message(Event(EventType.SERVER, f'User {event.client.user_ID} disconnected.'))

    async def list_users(self, event):
        print(f'listing users for {event.client.user_ID}')
        event.client.client.send(Event(EventType.SERVER, f'Users: {", ".join(self.clients.keys())}').encode())


async def main(host_port=("127.0.0.1", 55555)):
    server = Server()
    server.host_port = host_port
    server.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    await server.run()


if __name__ == '__main__':
    asyncio.run(main())
