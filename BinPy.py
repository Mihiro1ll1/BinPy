#!/usr/bin/env python
import sys
from ctypes import *
import struct

type_length = { 'int':4, 'uint':4, 'int8':1, 'uint8':1, \
                'int16':2, 'uint16':2, 'float':4, 'char':1 } 
type_symbol = { 'int':'i', 'uint':'I', 'int8':'b', 'uint8':'B', \
                'int16':'h', 'uint16':'H', 'float':'f', 'char':'c' } 
endian_symbol = { 'little':'<', 'big':'>' }

def bin_read(fd, type, endian):
    if type in type_length:
        raw = fd.read(type_length[type])
        symbol = endian_symbol[endian]+type_symbol[type]
        data = struct.unpack(symbol, raw)[0]
    else:
        print('Specified type is not available..')
        return

    return data

def bin_read_str(fd, length):
    data = fd.read(length)
    return data

def bin_write(fd, type, endian, val):
    if type in type_symbol:
        symbol = endian_symbol[endian]+type_symbol[type]
        raw = struct.pack(symbol, val)
        fd.write(raw)
    else:
        print('Specified type is not available..')
        return

    return raw 

def bin_write_str(fd, val):
    fd.write(val)
    return
