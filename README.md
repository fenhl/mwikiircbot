**mwikiircbot** is an [IRC][] bot that sits in one or more IRC channels and posts a livestream of recent changes from a [MediaWiki][] to the channels. It uses [the Python IRC bot framework][PythonIRCBotFramework].

This is `mwikiircbot` verson 1.0.1 ([semver][Semver]). The versioned API includes the usage pattern, as found in the docstring of [`mwikiircbot.py`](mwikiircbot.py).

Configuration
=============

*   Make sure [the Python IRC bot framework][PythonIRCBotFramework] and [docopt][Docopt] are in [the module search path][Pythonpath].
*   If your wiki is running MediaWiki 1.21 or lower:
    *   Set your wiki's [$wgRC2UDPAddress](https://www.mediawiki.org/wiki/Manual:$wgRC2UDPAddress) to an IP address or host name of the host where mwikiircbot will run.
    *   Set your wiki's [$wgRC2UDPPort](https://www.mediawiki.org/wiki/Manual:$wgRC2UDPPort) to `51666`, and [$wgRC2UDPPrefix](https://www.mediawiki.org/wiki/Manual:$wgRC2UDPPrefix) to the empty string.
*   If your wiki is running MediaWiki 1.22 or higher, configure its [$wgRCFeeds](https://www.mediawiki.org/wiki/Manual:$wgRCFeeds) accordingly.

Usage
=====

See the docstring in [`mwikiircbot.py`](mwikiircbot.py).

*   If specified, the bot will use `<name>` as its IRC nick. The default value is MediaWiki.
*   Upon startup, the bot will connect to the IRC server specified by `<host>` at port 6667, and join the `<channel>`s. Make sure to prefix the channels with `#`, and to escape the channel name when calling from a command line.

[Docopt]: https://docopt.org/ (docopt)
[IRC]: http://en.wikipedia.org/wiki/Internet_Relay_Chat (Wikipedia: Internet Relay Chat)
[MediaWiki]: http://www.mediawiki.org/wiki/MediaWiki (MediaWikiWiki: MediaWiki)
[PythonIRCBotFramework]: https://github.com/Fenhl/Python-IRC-Bot-Framework (github: Fenhl/Python-IRC-Bot-Framework)
[Pythonpath]: http://docs.python.org/3.3/tutorial/modules.html#the-module-search-path (Python 3.3 documentation: Modules: More on Modules: The Module Search Path)
[Semver]: http://semver.org/ (Semantic Versioning 2.0.0)
