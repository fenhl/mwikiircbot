This is an [IRC][] bot that sits in a channel and posts a livestream of recent changes from a [MediaWiki][] to the channel. It uses [the Python IRC bot framework](https://github.com/Fenhl/Python-IRC-Bot-Framework).

Usage
=====

    python3 mwikiircbot.py [-n <name>] <host> <channel> [<channel> ...]

*   If specified, the bot will use `<name>` as its IRC nick. The default value is MediaWiki.
*   Upon startup, the bot will connect to the IRC server specified by `<host>` at port 6667, and join the `<channel>`s. Make sure to prefix the channels with `#`, and to escape the channel name when calling from a command line.

[IRC]: http://en.wikipedia.org/wiki/Internet_Relay_Chat (Wikipedia: Internet Relay Chat)
[MediaWiki]: http://www.mediawiki.org/wiki/MediaWiki (MediaWikiWiki: MediaWiki)
