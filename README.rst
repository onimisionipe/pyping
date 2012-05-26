Pyping
======

A pure python ping implementation using raw sockets.

Note that ICMP messages can only be sent from processes running as root
(in Windows, you must run this script as 'Administrator').

Original Version from `Matthew Dixon Cowles <ftp://ftp.visi.com/users/mdc/ping.py>`_.
  
* Copyleft 1989-2011 by the python-ping team, see `AUTHORS <https://github.com/socketubs/pyping/blob/master/AUTHORS>`_ for more details.
* License: GNU GPL v2, see `LICENCE <https://github.com/socketubs/pyping/blob/master/LICENSE>`_ for more details.

Usage
-----
::

    ~/python-ping$ sudo ./ping.py google.com

    PYTHON-PING google.com (209.85.148.99): 55 data bytes
    64 bytes from google.com (209.85.148.99): icmp_seq=0 ttl=54 time=56.2 ms
    64 bytes from google.com (209.85.148.99): icmp_seq=1 ttl=54 time=55.7 ms
    64 bytes from google.com (209.85.148.99): icmp_seq=2 ttl=54 time=55.5 ms

    ----google.com PYTHON PING Statistics----
    3 packets transmitted, 3 packets received, 0.0% packet loss
    round-trip (ms)  min/avg/max = 55.468/55.795/56.232

TODO
----

- Refactor ping.py
- Create a CLI interface
- Add a "suprocess ping", with output parser

Contribute
----------

`Fork <http://help.github.com/fork-a-repo/>`_ this repo on `GitHub <https://github.com/socketubs/pyping>`_ and `send <http://help.github.com/send-pull-requests>`_ pull requests. Thank you.

Revision history
----------------

 * **2011-10-17**: `Bugfix <https://github.com/jedie/python-ping/pull/6>`_ if host is unknown
 * **2011-10-12**: Merge sources and create a seperate github `repository <https://github.com/jedie/python-ping>`_ and add a simple CLI interface.
 * **2011-09-12**: Bugfixes + cleanup by Jens Diemer. Tested with Ubuntu + Windows 7.
 * **2011-09-06**: `Cleanup <http://www.falatic.com/index.php/39/pinging-with-python>`_ by Martin Falatic :
  - Restored lost comments and docs. Improved functionality: constant time between pings, internal times consistently use milliseconds. Clarified annotations (e.g., in the checksum routine)
  - Using unsigned data in IP & ICMP header pack/unpack unless otherwise necessary.
  - Signal handling
  - Ping-style output formatting and stats
 * **2011-08-03**: Ported to py3k by Zach Ware. Mostly done by 2to3; also minor changes to deal with bytes vs. string changes (no more ord() in checksum() because >source_string< is actually bytes, added .encode() to data in send_one_ping()). That's about it.
 * **2010-03-11**: Changes by Samuel Stauffer:
  - Replaced time.clock with default_timer which is set to time.clock on windows and time.time on other systems.
 * **2009-11-08**: Fixes by `George Notaras <http://www.g-loaded.eu/2009/10/30/python-ping/>`_, reported by `Chris Hallman <http://cdhallman.blogspot.com>`_: 
  - Improved compatibility with GNU/Linux systems.
  - Re-use time.time() instead of time.clock(). The 2007 implementation worked only under Microsoft Windows. Failed on GNU/Linux. time.clock() behaves differently under the two `OSes <http://docs.python.org/library/time.html#time.clock>`_.
 * **2007-06-30**: Little rewrite by `Jens Diemer <http://www.python-forum.de/post-69122.html#69122>`_:
  - Change socket asterisk import to a normal import
  - Replace time.time() with time.clock()
  - Delete "return None" (or change to "return" only)
  - In checksum() rename "str" to "source_string"
 * **2000-12-04**: Changed the struct.pack() calls to pack the checksum and ID as unsigned. My thanks to Jerome Poincheval for the fix.
 * **1997-12-16**: For some reason, the checksum bytes are in the wrong order when this is run under Solaris 2.X for SPARC but it works right under Linux x86. Since I don't know just what's wrong, I'll swap the bytes always and then do an htons().
 * **1997-11-22**: Initial hack. Doesn't do much, but rather than try to guess what features I (or others) will want in the future, I've only put in what I need now.

Links
-----

 - Sourcecode at GitHub: https://github.com/socketubs/pyping
 - Python Package Index: http://pypi.python.org/pypi/pyping/