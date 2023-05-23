import sys
import re

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtNetwork, QtGui
from PySide6.QtCore import QIODevice, Qt
from gui.main_window import Ui_MainWindow
from utils.events import Event, EventType, EventQueue


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.event_queue = EventQueue()
        self.user_id = None
        self.port = None
        self.server = None
        self.socket: None | QtNetwork.QTcpSocket = None
        self.event_handler = None
        self.data_stream = None
        self.txtUsername.setFocus()

        # window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.oldPos = self.pos()

        # buttons
        self.btnExit.clicked.connect(self.on_exit)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnSend.clicked.connect(self.send_message)
        self.btnLogin.clicked.connect(self.login)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.txtInput.hasFocus() and self.txtInput.text() != '':
                self.send_message()
            elif self.txtUsername.hasFocus() or self.txtPort.hasFocus() or self.txtServer.hasFocus():
                self.login()
        elif event.key() == Qt.Key_Escape:
            self.on_exit()
        else:
            super(MainWindow, self).keyPressEvent(event)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()

    def on_message(self):
        msg = self.socket.readAll()

        pattern = r'({.*?})'
        matches = re.findall(pattern, msg.data().decode())
        for match in matches:
            event = Event.decode(match)
            self.event_queue.push(event)

    def login(self):
        self.user_id = self.txtUsername.text()
        if self.user_id == '':
            self.lblLoginError.setText('Username cannot be empty.')
            return
        elif ' ' in self.user_id:
            self.lblLoginError.setText('Username cannot contain spaces.')
            return
        self.port = self.txtPort.text()
        self.server = self.txtServer.text()
        self.socket = QtNetwork.QTcpSocket()
        self.socket.connected.connect(self.on_connected)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.errorOccurred.connect(self.on_error)
        self.socket.readyRead.connect(self.on_message)
        self.socket.open(QIODevice.ReadWrite)
        self.socket.connectToHost(self.server, int(self.port))

    def on_exit(self):
        if self.socket is None:
            self.close()
            return
        self.txtInput.setText('/exit')
        self.send_message()
        self.socket.close()
        self.close()

    def on_connected(self):
        self.socket.waitForConnected()
        self.event_handler = EventHandler(self.event_queue, self.socket)
        self.event_handler.msg_signal.connect(self.display_message)
        self.event_handler.connection_signal.connect(self.on_connection_ok)
        self.event_handler.disconnection_signal.connect(self.on_disconnected)
        self.event_handler.error_signal.connect(self.on_error)
        self.event_handler.start()
        self.event_queue.push(Event(EventType.CONNECT, self.txtUsername.text()))

    def on_connection_ok(self):
        self.lblLoginError.setText('Connected.')
        self.stkPanel.setCurrentIndex(1)
        self.txtInput.setFocus()

    def display_message(self, msg):
        self.txtChat.append(msg)

    def on_disconnected(self):
        self.socket = None
        self.event_handler = None
        self.lblLoginError.setText('Disconnected.')
        self.stkPanel.setCurrentIndex(0)

    def on_error(self, error_code):
        self.socket = None
        self.event_handler = None
        self.lblLoginError.setText(f'Error: {error_code}')
        self.stkPanel.setCurrentIndex(0)

    def send_message(self):
        msg = self.txtInput.text().strip().replace('{', '~:~').replace('}', '~;~')

        match msg.split():
            case []:
                return
            case ['/exit']:
                self.event_queue.push(Event(EventType.DISCONNECT, '', sender=self.user_id))
            case ['/list']:
                self.event_queue.push(Event(EventType.LIST, '', sender=self.user_id))
            case ['/msg', recipient, *msg]:
                self.event_queue.push(Event(EventType.OUT_MSG, ' '.join(msg), sender=self.user_id, recipient=recipient))
            case _:
                self.event_queue.push(Event(EventType.OUT_MSG, msg, sender=self.user_id))

        self.txtInput.setText('')


class EventHandler(QtCore.QThread):
    msg_signal = QtCore.Signal(str)
    connection_signal = QtCore.Signal()
    disconnection_signal = QtCore.Signal()
    error_signal = QtCore.Signal(str)

    def __init__(self, event_queue: EventQueue, client: QtNetwork.QTcpSocket, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.event_queue = event_queue
        self.client = client

    def run(self):
        while True:
            if not self.event_queue:
                self.msleep(100)
                continue

            event = self.event_queue.pop()
            match event.type:
                case EventType.OUT_MSG:
                    self.client.write(event.encode())
                    self.client.waitForBytesWritten()
                case EventType.DISCONNECT:
                    self.client.write(event.encode())
                    self.client.waitForBytesWritten()
                    self.disconnection_signal.emit()
                    break
                case EventType.CONNECT:
                    self.client.write(event.encode())
                    self.client.waitForBytesWritten()
                case EventType.LIST:
                    self.client.write(event.encode())
                    self.client.waitForBytesWritten()
                case EventType.CONNECT_OK:
                    self.connection_signal.emit()
                case EventType.CONNECT_ERR:
                    self.error_signal.emit(event.data)
                case _:
                    self.msg_signal.emit(event.data.replace('~:~', '{').replace('~;~', '}'))


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
