# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


import ledpixels
from ledpixels import Pixels
from ledpixels import PixelColor
import pickle

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import hmac
import sys
import optparse
import urllib
import time
import thread
import json

listeners = {}
names = {}
tokens = {}


@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in 
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())


@auth.requires_login()
def startLEDSocket():
    try:
        hmac_key = None
        DistributeHandler.tokens = False
        urls = [
            (r'/led/(.*)', DistributeHandler)]
        application = tornado.web.Application(urls, auto_reload=True)
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(8080, address='0.0.0.0')
        thread.start_new_thread(tornado.ioloop.IOLoop.instance().start,())
        print "Started websocket"
    
    except Exception, e:
        print "The socket has already started"


def websocket_send(url, message, hmac_key=None, group='default'):
    sig = hmac_key and hmac.new(hmac_key, message).hexdigest() or ''
    params = urllib.urlencode(
        {'message': message, 'signature': sig, 'group': group})
    f = urllib.urlopen(url, params)
    data = f.read()
    f.close()
    return data


class PostHandler(tornado.web.RequestHandler):
    """
    only authorized parties can post messages
    """
    def post(self):
        if hmac_key and not 'signature' in self.request.arguments:
            return 'false'
        if 'message' in self.request.arguments:
            message = self.request.arguments['message'][0]
            group = self.request.arguments.get('group', ['default'])[0]
            print '%s:MESSAGE to %s:%s' % (time.time(), group, message)
            if hmac_key:
                signature = self.request.arguments['signature'][0]
                if not hmac.new(hmac_key, message).hexdigest() == signature:
                    return 'false'
            for client in listeners.get(group, []):
                client.write_message(message)
            return 'true'
        return 'false'


class TokenHandler(tornado.web.RequestHandler):
    """
    if running with -t post a token to allow a client to join using the token
    the message here is the token (any uuid)
    allows only authorized parties to joins, for example, a chat
    """
    def post(self):
        if hmac_key and not 'message' in self.request.arguments:
            return 'false'
        if 'message' in self.request.arguments:
            message = self.request.arguments['message'][0]
            if hmac_key:
                signature = self.request.arguments['signature'][0]
                if not hmac.new(hmac_key, message).hexdigest() == signature:
                    return 'false'
            tokens[message] = None
            return 'true'
        return 'false'


class DistributeHandler(tornado.websocket.WebSocketHandler):
    def open(self, params):

        self.pixelcontroller=Pixels()

        print '%s:CONNECTED' % (time.time())

    def on_message(self, message):
        try:
            ledpixelsarray = json.loads(message)

            for p in range(len(ledpixelsarray)):
                c = ledpixelsarray[p]
                self.pixelcontroller.setpixelcolor(p, PixelColor(c[0], c[1], c[2]))
            self.pixelcontroller.writestrip()

        except Exception, e:
            print "There was an error interpreting the message:"+ message

    def on_close(self):
        # self.pixelcontroller.close()

        self.pixelcontroller.colorwipe(PixelColor(0, 0, 0), 0.01)
        
        print '%s:DISCONNECTED' % (time.time())

