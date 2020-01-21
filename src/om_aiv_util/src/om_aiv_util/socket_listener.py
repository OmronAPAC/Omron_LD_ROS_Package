import io
import selectors2 as selectors
import socket
import traceback
import time
import threading
from collections import deque

RECV_BUFFER = 4096

"""A driver class to handle all input and output communication with ARCL server.

"""
class SocketListener(object):
    def __init__(self, addr, port):
        self.selector = None
        self.sock = None
        self.addr = str(addr)
        self.port = int(port)
        self.responses = dict()
        self._recv_buffer = b""
        self.lock = threading.Lock()

    
    """Given the event mask from selectors, do read or write accordingly.

    param mask:
    The mask to use to decide which event can be executed.
    
    """
    def process_events(self, mask):
        if mask & selectors.EVENT_READ:
            self.read()

    """
    Read incoming bytes from the socket and save into receive buffer.
    If there are data received, append into the receiver buffer.
    
    """
    def _read(self):
        try:
            recv_data = self.sock.recv(RECV_BUFFER)
        except io.BlockingIOError:
            pass
        else:
            if recv_data:
                print recv_data
                # self._recv_buffer += recv_data

    """
    Read incoming bytes and generate the correct responses.
    
    """
    def read(self):
        self._read()

    """
    Extracts the required string to find from the receive buffer.
    
    Returns:
        str -- The extracted string.
    """
    def extract_resp(self):
        line_s = self._recv_buffer.index(self._find_str)
        resp_e = self._recv_buffer.index("\r\n", line_s) + 1 # Add one to get the index of \n.
        ret = self._recv_buffer[:resp_e+1] # We want the \n char.
        self._recv_buffer = self._recv_buffer[resp_e+1:]
        return ret


    """
    Retrieve the response associated with the given identifier integer.

    param identifier:
    The identifier integer associated with returned response.
    
    Returns:
        str -- The response string associated with the identifier integer.
    """
    def get_response(self, identifier):
        ret = self.responses.pop(identifier)
        self.clr_id(identifier)
        return ret

    """
    # TODO: Add check for failed connection
    Connects the driver to the given address and port.

    param addr:
    Address to connect to.

    param port:
    Port number to connect to.

    """
    def begin(self, addr, port):
        print "Listening on", self.addr, "at port", self.port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        incoming = (self.addr, self.port)
        sock.bind(incoming)
        sock.listen(5)
        (connection, address) = sock.accept()
        self.sock = connection
        events = selectors.EVENT_READ
        self.selector = selectors.DefaultSelector()
        self.selector.register(sock, events, data=self)

