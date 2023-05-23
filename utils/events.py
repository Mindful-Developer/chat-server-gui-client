from enum import Enum, auto
from dataclasses import dataclass, field
from json import dumps, loads
from collections import deque
import socket


class EventType(Enum):
    IN_MSG = auto()
    OUT_MSG = auto()
    SERVER = auto()
    LIST = auto()
    ERROR = auto()
    CONNECT = auto()
    DISCONNECT = auto()
    CONNECT_OK = auto()
    CONNECT_ERR = auto()


@dataclass
class EventQueue:
    events: deque = field(default_factory=deque)

    def push(self, event):
        self.events.append(event)

    def pop(self):
        return self.events.popleft()

    def remove(self, event):
        self.events.remove(event)

    def __len__(self):
        return len(self.events)

    def __bool__(self):
        return bool(self.events)

    def __str__(self):
        return str(self.events)

    def __repr__(self):
        return str(self.events)

    def __iter__(self):
        return iter(self.events)


@dataclass
class Client:
    client: socket.socket
    user_ID: str

    def __str__(self):
        return f'{self.user_ID} {self.client}'

    def __repr__(self):
        return f'{self.user_ID} {self.client}'

    def send(self, event):
        try:
            self.client.send(event.encode())
        except OSError:
            raise ConnectionError('Client is not connected.')

    def close(self):
        self.client.close()


@dataclass
class Event:
    type: EventType
    data: str
    client: Client | None = None
    sender: str | None = None
    recipient: str | None = None

    def encode(self):
        event_dict = {}
        event_dict['type'] = self.type.value
        event_dict['data'] = self.data
        if self.sender:
            event_dict['sender'] = self.sender
        if self.recipient:
            event_dict['recipient'] = self.recipient
        msg = dumps(event_dict)
        return msg.encode()

    @classmethod
    def decode(cls, data):
        data = loads(data)
        event = cls(EventType(data['type']), data['data'])
        if 'sender' in data:
            event.sender = data['sender']
        if 'recipient' in data:
            event.recipient = data['recipient']
        return event

    def __str__(self):
        return f'{self.type.name} {self.data}'

    def __repr__(self):
        return f'{self.type.name} {self.data}'
