###
# Copyright (c) 2011, Stryker Blue
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring
import commands

#<div class="message"><b>Now:</b> Test</div>
#<dash> Deathspawn: lxml.html.fromstring(yourhtml).xpath("//div[@class='message']/b")[0].tail

_ = PluginInternationalization('CrushCastHelper')

@internationalizeDocstring
class CrushCastHelper(callbacks.Plugin):
    """Add the help for "@plugin help CrushCastHelper" here
    This should describe *how* to use this plugin."""
    threaded = True

    def postnow(self, irc, msg, args, text):
        """<text>

        Post updates to the Now section of the ticker. You can use nested commands to save time with this, for example: postnow (shownext)
        """
        #commands.getoutput("echo \"<b>Now:</b> %s\" > /home/boldvoices/public_html/ircbot/now.html" % (text))
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "r")
        cache = file.readlines()
        if text.startswith("Now: ") == 1:
            changenow = "<div class=\"message\"><b>Now:</b> "+text.split("Now: ")[0]+"</div>\n"
        elif text.startswith("Next: ") == 1:
            changenow = "<div class=\"message\"><b>Now:</b> "+text.split("Next: ")[0]+"</div>\n"
        elif text.startswith("Soon: ") == 1:
            changenow = "<div class=\"message\"><b>Now:</b> "+text.split("Soon: ")[0]+"</div>\n"
        else:
            changenow = "<div class=\"message\"><b>Now:</b> "+text+"</div>\n"
        cache = changenow+cache[1]+cache[2]
        file.close()
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "w")
        file.write(cache)
        file.close()
        changenoww = changenow.split("<div class=\"message\"><b>Now:</b> ")[1]
        changenoww = changenoww.split("</div>\n")[0]
        irc.reply("\""+changenoww+"\" has been successfully written to the ticker.")
    postnow = wrap(postnow, [('checkCapability', 'bvhost'), 'text'])

    def postnext(self, irc, msg, args, text):
        """<text>

        Post updates to the Next section of the ticker. You can use nested commands to save time with this, for example: postnext (showsoon)
        """
        #commands.getoutput("echo \"<b>Next:</b> %s\" > /home/boldvoices/public_html/ircbot/next.html" % (text))
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "r")
        cache = file.readlines()
        if text.startswith("Now: ") == 1:
            changenext = "<div class=\"message\"><b>Next:</b> "+text.split("Now: ")[0]+"</div>\n"
        elif text.startswith("Next: ") == 1:
            changenext = "<div class=\"message\"><b>Next:</b> "+text.split("Next: ")[0]+"</div>\n"
        elif text.startswith("Soon: ") == 1:
            changenext = "<div class=\"message\"><b>Next:</b> "+text.split("Soon: ")[0]+"</div>\n"
        else:
            changenext = "<div class=\"message\"><b>Next:</b> "+text+"</div>\n"
        cache = cache[0]+changenext+cache[2]
        file.close()
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "w")
        file.write(cache)
        file.close()
        changenextt = changenext.split("<div class=\"message\"><b>Next:</b> ")[1]
        changenextt = changenextt.split("</div>\n")[0]
        #changenextt = changenext.lstrip("<div class=\"message\"><b>Next:</b> ").rstrip("</div>\n")
        irc.reply("\""+changenextt+"\" has been successfully written to the ticker.")
    postnext = wrap(postnext, [('checkCapability', 'bvhost'), 'text'])

    def postsoon(self, irc, msg, args, text):
        """<text>

        Post updates to the Soon section of the ticker. You can use nested commands to save time with this, for example: postsoon (shownext)
        """
        #commands.getoutput("echo \"<b>Next:</b> %s\" > /home/boldvoices/public_html/ircbot/next.html" % (text))
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "r")
        cache = file.readlines()
        if text.startswith("Now: ") == 1:
            changesoon = "<div class=\"message\"><b>Soon:</b> "+text.split("Now: ")[0]+"</div>\n"
        elif text.startswith("Next: ") == 1:
            changesoon = "<div class=\"message\"><b>Soon:</b> "+text.split("Next: ")[0]+"</div>\n"
        elif text.startswith("Soon: ") == 1:
            changesoon = "<div class=\"message\"><b>Soon:</b> "+text.split("Soon: ")[0]+"</div>\n"
        else:
            changesoon = "<div class=\"message\"><b>Soon:</b> "+text+"</div>\n"
        cache = cache[0]+cache[1]+changesoon
        file.close()
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "w")
        file.write(cache)
        file.close()
        changesoonn = changesoon.split("<div class=\"message\"><b>Soon:</b> ")[1]
        changesoonn = changesoonn.split("</div>\n")[0]
        irc.reply("\""+changesoonn+"\" has been successfully written to the ticker.")
    postsoon = wrap(postsoon, [('checkCapability', 'bvhost'), 'text'])

    def shownow(self, irc, msg, args):
        """takes no arguments

        Shows the entry for the Now section of the ticker. You can use this as a nested command with posting.
        """
        #now = commands.getoutput("tail -1 /home/boldvoices/public_html/ircbot/now.html").lstrip("<b>Now: </b>").split("\n")
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "r")
        cache = file.readlines()
        #now = cache[0].lstrip("<div class=\"message\"><b>Now:</b> ").rstrip("</div>\r\n")
        now = cache[0].split("<div class=\"message\"><b>Now:</b> ")[1]
        now = now.split("</div>\n")[0]
        file.close()
        irc.reply("Now: "+now)
    shownow = wrap(shownow)

    def shownext(self, irc, msg, args):
        """takes no arguments

        Shows the entry for the Next section of the ticker. You can use this as a nested command with posting.
        """
        #next = commands.getoutput("tail -1 /home/boldvoices/public_html/ircbot/next.html").lstrip("<b>Next: </b>").split("\n")
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "r")
        cache = file.readlines()
        #nextthing = cache[1].lstrip("<div class=\"message\"><b>Next:</b> ").rstrip("</div>\r\n")
        nextthing = cache[1].split("<div class=\"message\"><b>Next:</b> ")[1]
        nextthing = nextthing.split("</div>\n")[0]
        file.close()
        irc.reply("Next: "+nextthing)
    shownext = wrap(shownext)

    def showsoon(self, irc, msg, args):
        """takes no arguments

        Shows the entry for the Soon section of the ticker. You can use this as a nested command with posting.
        """
        file = open("/home/jellybean/supybot/bin/plugins/CrushCastHelper/webUpdate.txt", "r")
        cache = file.readlines()
        soon = cache[2].split("<div class=\"message\"><b>Soon:</b> ")[1]
        soon = soon.split("</div>\n")[0]
        file.close()
        irc.reply("Soon: "+soon)
    showsoon = wrap(showsoon)

Class = CrushCastHelper


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
