"""
Checks downforeveryoneorjustme.com to see if the requested web page is available

Might be useful if your network administrators are incompetent
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = "0.1"

__author__ = supybot.Author("Dan Scott", "dbs", "dan@coffeecode.net")

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = { }

import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    import test

Class = plugin.Class
configure = config.configure

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
