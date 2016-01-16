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
import random

_ = PluginInternationalization('RPS')

@internationalizeDocstring
class RPS(callbacks.Plugin):
    """Play a game of rock, paper, scissors.
    Choose what to go as against the bot."""
    threaded = True

    def rock(self, irc, msg, args):
        """takes no arguments

        Choose rock in Rock, Paper, Scissors.
        """
        botchoice2 = random.randint(1, 3)
        if botchoice2 == 1:
            botchoice = "rock"
        elif botchoice2 == 2:
            botchoice = "paper"
        elif botchoice2 == 3:
            botchoice = "scissors"
        userchoice = "rock"
        if botchoice == userchoice:
            irc.reply("I chose %s. Looks like we tied." % (botchoice))
        elif botchoice == "paper" and userchoice == "rock":
            irc.reply("I chose %s. Looks like I won." % (botchoice))
        elif botchoice == "scissors" and userchoice == "rock":
            irc.reply("I chose %s. Looks like you won." % (botchoice))
    rock = wrap(rock)

    def paper(self, irc, msg, args):
        """takes no arguments

        Choose paper in Rock, Paper, Scissors.
        """
        botchoice2 = random.randint(1, 3)
        if botchoice2 == 1:
            botchoice = "rock"
        elif botchoice2 == 2:
            botchoice = "paper"
        elif botchoice2 == 3:
            botchoice = "scissors"
        userchoice = "paper"
        if botchoice == userchoice:
            irc.reply("I chose %s. Looks like we tied." % (botchoice))
        elif botchoice == "scissors" and userchoice == "paper":
            irc.reply("I chose %s. Looks like I won." % (botchoice))
        elif botchoice == "rock" and userchoice == "paper":
            irc.reply("I chose %s. Looks like you won." % (botchoice))
    paper = wrap(paper)

    def scissors(self, irc, msg, args):
        """takes no arguments

        Choose scissors in Rock, Paper, Scissors.
        """
        botchoice2 = random.randint(1, 3)
        if botchoice2 == 1:
            botchoice = "rock"
        elif botchoice2 == 2:
            botchoice = "paper"
        elif botchoice2 == 3:
            botchoice = "scissors"
        userchoice = "scissors"
        if botchoice == userchoice:
            irc.reply("I chose %s. Looks like we tied." % (botchoice))
        elif botchoice == "rock" and userchoice == "scissors":
            irc.reply("I chose %s. Looks like I won." % (botchoice))
        elif botchoice == "paper" and userchoice == "scissors":
            irc.reply("I chose %s. Looks like you won." % (botchoice))
    scissors = wrap(scissors)

Class = RPS


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
