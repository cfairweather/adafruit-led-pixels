from gluon.tools import Service
from gluon.utils import web2py_uuid

import sys
import hashlib
import ast
import ssl

from datetime import datetime
import thread

from ledpixels import *

service = Service(globals())
service_public = Service(globals())

@auth.requires_login()    
def call():
    return service()

def call_public():
    return service_public()

@service_public.jsonrpc
def ledRunProgram(duration, program):
    print "ledRunProgram"
    ret = dict()

    print str(duration)
    print str(program)

    pix = Pixels()
    # pix.run(program, duration) #def run(self, tracks, duration):
    thread.start_new_thread(ledRunProgram_Threaded,(program,duration))
        
    return ret

def ledRunProgram_Threaded(data, duration):
    pix = Pixels()
    pix.run(data, duration) #def run(self, tracks, duration):


@service_public.jsonrpc
def led_login(username, password):
    ret = dict()
    if auth.login_bare(str(username), str(password)) is not False:
        print "iPad Login success"
        ret['success'] = True
    else:
        print "iPad Login fail"
        ret['success'] = False
    return ret
