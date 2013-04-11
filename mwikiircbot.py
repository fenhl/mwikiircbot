import ircbotframe
import sys

class Handler:
    def __init__(self, host, port=6667, name="MediaWiki", description="MediaWiki recent changes bot", channels=[]):
        self.channels = channels
        self.bot = ircbotframe.ircBot(host, port, name, description)
        self.bot.bind("376", self.endMOTD)
        self.bot.start()
    
    def endMOTD(self, sender, headers, message):
        for chan in self.channels:
            self.bot.joinchan(chan)

def main(cmd, args):
    args = args[:]
    parsemode = ["host"]
    host = None
    name = "MediaWiki"
    channels = []
    while len(args) > 0:
        if args[0] == "-n" and parsemode[0] != "name":
            parsemode.insert(0, "name")
        elif len(parsemode) < 1:
            if args[0] == "-n":
                parsemode.insert(0, "name")
            else:
                channels.append(args[0])
        else:
            if parsemode[0] == "name":
                name = args[0]
            elif parsemode[0] == "host":
                host = args[0]
            parsemode = parsemode[1:]
        args = args[1:]
    if host == None:
        print("Usage: " + cmd + " [-n <name>] <host> <channel> [<channel> ...]")
        return
    else:
        Handler(host=host, name=name, channels=channels)

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:] if len(sys.argv) > 1 else [])
