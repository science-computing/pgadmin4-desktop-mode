# -*- coding: utf-8 -*-

import sys
import os
import builtins
import socket
from urllib.parse import urlunparse, urlencode
import uuid
import getpass
import struct
import hashlib

def main():
    builtins.SERVER_MODE = False
    os.environ['PGADMIN_SERVER_MODE'] = 'OFF'

    # I'll add a command line parser for the next version
    schema = 'http'
    ip = ''   # use localhost. Set to '0.0.0.0' to bind to all interfaces
    port = '' # choos port based on login name
    key = ''  # generate a random key
    port_min = 11000
    port_max = 19999

    if ip:
        os.environ['PGADMIN_CONFIG_DEFAULT_SERVER'] = ip
        hostname = socket.getfqdn(ip)
    else:
        hostname = '127.0.0.1'
    if not port:
        user_hash = hashlib.sha1(getpass.getuser().encode('utf-8')).digest()  # bytes
        port = str(struct.unpack('!Q', user_hash[:8])[0] % (port_max - port_min + 1) + port_min)
    os.environ['PGADMIN_INT_PORT'] = port
    if not key:
        key = str(uuid.uuid4())
    os.environ['PGADMIN_INT_KEY'] = key
    url = urlunparse((schema, '{}:{}'.format(hostname, port), '/', '', urlencode({'key': key}), ''))
    print("Starting server, connection URL={}".format(url))
    from pgadmin4.pgAdmin4 import main as pgadmin_main
    return pgadmin_main()
