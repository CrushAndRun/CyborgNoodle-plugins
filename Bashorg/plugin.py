###
# Copyright (c) 2011, Juan Manuel Santos
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
from lxml.html import fromstring
from lxml.html.clean import Cleaner
import urllib2
import random


import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Bash(callbacks.Plugin):
    """Gets a random quote from bash.org, either Random or Latest Quotes sections

    To use this plugin, just type <botname> bash rr|rl. rr: random quote from Random Quotes section. rl: random quote from Latest Quotes section."""
    threaded = True

    def __init__(self, irc):
        self._parent = super(Bash, self)
        self._parent.__init__(irc)
        self.base_url = "http://bash.org/"
        self.random_url = self.base_url + "?random"
        self.latest_url = self.base_url + "?latest"

    def rr(self, irc, msg, args):
        """takes no arguments

        Returns a random quote from the \"Random Quote\" section of bash.org"""
        msglines = self._get_random_quote_for_url(self.random_url)
        for line in msglines:
            irc.reply(line)
    rr = wrap(rr)

    def rl(self, irc, msg, args):
        """takes no arguments

        Returns a random quote from the \"Latest Quote\" section of bash.org"""
        msglines = self._get_random_quote_for_url(self.latest_url)
        for line in msglines:
            irc.reply(line)
    rl = wrap(rl)

    def _get_random_quote_for_url(self, url):
        """Internal method to fetch a random quote from the url given."""
        html = urllib2.urlopen(url).read()
        
        doc = fromstring(html)
        
        tags = ['h1','h2','h3','h4','h5','h6',
               'div', 'span', 
               'img', 'area', 'map']
        args = {'meta':False, 'safe_attrs_only':False, 'page_structure':False, 
               'scripts':True, 'style':True, 'links':True, 'remove_tags':tags}
        cleaner = Cleaner(**args)
        
        path = '/html/body'
        body = doc.xpath(path)[0]
        
        lines = cleaner.clean_html(body).text_content().encode('ascii', 'ignore').split("\n")
        x = random.randint(1,50)
        index = 0
        while x > 0:
            for line in lines:
                if line.startswith("#"):
                    index = lines.index(line)
                    break
        
            x -= 1
        quote = lines[index] + "\n"
        index += 1
        while not lines[index].startswith("#"):
            quote += lines[index] + "\n"
            index += 1
        return [line.replace("\r", "") for line in quote.split("\n") if line is not None and line != ""]




Class = Bash


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
