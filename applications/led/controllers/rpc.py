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
def ledRunProgram(program):
    print "ledRunProgram"
    ret = dict()

    duration = program[0]
    data = program[1]

    print str(duration)
    print str(data)

    pix = Pixels()
    pix.run(data, duration) #def run(self, tracks, duration):
    # thread.start_new_thread(ledRunProgram_Threaded,(data,duration))
    print "DONE"
        
    return ret

def ledRunProgram_Threaded(data, duration):
    pix = Pixels()
    pix.run(data, duration) #def run(self, tracks, duration):


@service.jsonrpc
def led_login(username, password):
    print "login"
    ret = dict()
    ret['success'] = auth.login_bare(username, password)
    return ret
