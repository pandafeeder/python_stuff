"""
sys._getframe(0) will get current executing stack
sys._getframe(1) will get upper frame stack
"""

import sys

class ViolateCallingProtocolException(Exception): pass

def callee():
    caller_frame = sys._getframe(1)
    if not caller_frame.f_code.co_name.endswith("_protocol"):
        raise ViolateCallingProtocolException("caller function name must ends with _protocol")
    print("Do the job")


def comply_protocol():
    """this will work as normal"""
    callee()

def violate_protocol_func():
    """this will throw ViolateCallingProtocolException"""
    callee()

comply_protocol()
violate_protocol_func()
