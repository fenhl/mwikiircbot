This is an [IRC][] bot that sits in a channel and posts a livestream of recent changes from a [MediaWiki][] to the channel. It uses [the Python IRC bot framework][PythonIRCBotFramework].

Configuration
=============

*   Make sure [the Python IRC bot framework][PythonIRCBotFramework] is in [the module search path][Pythonpath].
*   Set your wiki's [$wgRC2UDPAddress](https://www.mediawiki.org/wiki/Manual:$wgRC2UDPAddress) to an IP address or host name of the host where mwikiircbot will run.
*   Set your wiki's [$wgRC2UDPPort](https://www.mediawiki.org/wiki/Manual:$wgRC2UDPPort) to `51666`, and [$wgRC2UDPPrefix](https://www.mediawiki.org/wiki/Manual:$wgRC2UDPPrefix) to the empty string.

Usage
=====

    python3 mwikiircbot.py [-n <name>] <host> <channel> [<channel> ...]

*   If specified, the bot will use `<name>` as its IRC nick. The default value is MediaWiki.
*   Upon startup, the bot will connect to the IRC server specified by `<host>` at port 6667, and join the `<channel>`s. Make sure to prefix the channels with `#`, and to escape the channel name when calling from a command line.

[IRC]: http://en.wikipedia.org/wiki/Internet_Relay_Chat (Wikipedia: Internet Relay Chat)
[MediaWiki]: http://www.mediawiki.org/wiki/MediaWiki (MediaWikiWiki: MediaWiki)
[PythonIRCBotFramework]: https://github.com/Fenhl/Python-IRC-Bot-Framework (github: Fenhl/Python-IRC-Bot-Framework)
[Pythonpath]: http://docs.python.org/3.3/tutorial/modules.html#the-module-search-path (Python 3.3 documentation: Modules: More on Modules: The Module Search Path)
