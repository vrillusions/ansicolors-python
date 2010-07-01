#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""ANSI Colors

Convenience class for using colors on the terminal.

@todo: document

"""

import sys


class AnsiColors():
    def __init__(self, reset=True):
        # should text auto-reset after color method?
        self.autoreset = reset

        self.code = {}
        self.fg = {}
        self.bg = {}
        
        self.code['reset'] = '\033[0m'
        self.code['bold']  = '\033[1m'

        # Using the names as best as I can determine to be the most literal
        # interpretation (the "1;" is for bold, for example)
        self.fg['black']      = '\033[0;30m'
        self.fg['boldblack']  = '\033[1;30m'
        self.fg['red']        = '\033[0;31m'
        self.fg['boldred']    = '\033[1;31m'
        self.fg['green']      = '\033[0;32m'
        self.fg['boldgreen']  = '\033[1;32m'
        self.fg['brown']      = '\033[0;33m'
        self.fg['boldbrown']  = '\033[1;33m'
        self.fg['blue']       = '\033[0;34m'
        self.fg['boldblue']   = '\033[1;34m'
        self.fg['purple']     = '\033[0;35m'
        self.fg['boldpurple'] = '\033[1;35m'
        self.fg['cyan']       = '\033[0;36m'
        self.fg['boldcyan']   = '\033[1;36m'
        self.fg['white']      = '\033[0;37m'
        self.fg['boldwhite']  = '\033[1;37m'

        self.bg['black']      = '\033[40m'
        self.bg['red']        = '\033[41m'
        self.bg['green']      = '\033[42m'
        self.bg['brown']      = '\033[43m'
        self.bg['blue']       = '\033[44m'
        self.bg['purple']     = '\033[45m'
        self.bg['cyan']       = '\033[46m'
        self.bg['white']      = '\033[47m'
        
    def color(self, fg=None, bg=None, text='', reset=None):
        """Formats string to specific colors.
        
        @todo: throw an exception on invalid names
        
        """
        output = ''
        if fg != None and self.fg.has_key(fg):
            output += self.fg[fg]
        if bg != None and self.bg.has_key(bg):
            output += self.bg[bg]
        output += text
        if reset == None: 
            reset = self.autoreset
        if reset == True:
            output += self.code['reset']
        return output
        
    def reset(self):
        """Resets terminal to default colors."""
        sys.stdout.write(self.code['reset'])
        sys.stderr.write(self.code['reset'])
        pass
        
        
if __name__ == "__main__":
    # Recommend just removing this in production to save space
    ac = AnsiColors()
    # calling it manually
    print ac.fg['red'] + 'This is red'
    print ac.code['bold'] + 'bold'
    ac.reset()
    print "this should not"
    # It's better to use function
    print ac.color(fg='red', text='This is red')
    print 'no need to reset'
    print ac.color(fg='red', text='This is red')
    print ac.color(fg='black', bg='green', text='This is black on green')
    print ac.color(fg='boldpurple', text='This is bold purple', reset=False)
    print ac.color(text='Last one did not reset so this is the same', reset=False)
    print 'So is this'
    print ac.color(text='After this line it will reset again')
    print 'See?'
    print ac.color(fg='nonexistent', text='Silently ignores invalid names')
    # Since user's prompt is usually color, it gets changed when kicked back to
    # prompt.  Should still reset just in case
    ac.reset()