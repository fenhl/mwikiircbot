#!/usr/bin/env python3
"""MediaWiki recent changes IRC bot.

Usage:
  mwikiircbot.py [options] <host> <channel>...
  
Options:
  -h, --help         Print this message and exit.
  -n, --name=<name>  Use this name as the IRC nick [Default: MediaWiki].
  --port=<port>      Connect to the IRC server at this port [Default: 6667].
  --version          Print version info and exit.
"""

__version__ = '1.0.0'

from docopt import docopt
import ircbotframe
import socketserver
import sys

class RecentChangesServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

class RecentChangesHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            line = self.request[0]
        except:
            return
        if not line:
            return
        line = line.decode("utf-8").rstrip("\r\n")
        for chan in handler.channels:
            handler.bot.say(chan, line)

class Handler:
    def __init__(self, host, port=6667, name="MediaWiki", description="MediaWiki recent changes bot", channels=[]):
        self.channels = channels
        self.bot = ircbotframe.ircBot(host, port, name, description)
        self.bot.bind("376", self.endMOTD)
        self.bot.start()
    
    def endMOTD(self, sender, headers, message):
        for chan in self.channels:
            self.bot.joinchan(chan)

def main(arguments):
    channels = arguments['<channel>']
    global handler
    handler = Handler(host=arguments['<host>'], port=arguments['--port'], name=arguments=['--name'], channels=arguments['<channel>'])
    rcserver = RecentChangesServer(('localhost', 51666), RecentChangesHandler)
    rcserver.serve_forever()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='mwikiircbot ' + __version__)
    main(arguments)
