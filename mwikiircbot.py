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
    if len(args) < 2:
        print("Usage: " + cmd + " <host> <channel> [<channel> ...]")
        return
    elif len(args) > 1:
        Handler(host=args[0], channels=args[1:])

if __name__ == "__main__":
    if __name__ == '__main__':
        main(sys.argv[0], sys.argv[1:] if len(sys.argv) > 1 else [])
