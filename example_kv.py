# Generated from example.kv at 2017-03-13 12:17:17.300195

import sys
from kivy.metrics import dp, sp
from kivy.factory import Factory
from functools import partial
from kivy.lang import Builder, ParserSelectorId, ParserSelectorName, ParserSelectorClass
from kivy.event import EventDispatcher, Observable
from kivy import require
_mc = {}
_otype = (EventDispatcher, Observable)
_includes = []

def _execute_directive(cmd):
    # small version without error handling of directives
    # temporary, until the compiler analyse and do the work
    cmd = cmd.strip()
    if cmd[:4] == 'set ':
        name, value = cmd[4:].strip().split(' ', 1)
        globals()[name] = eval(value)
    elif cmd[:8] == 'include ':
        ref = cmd[8:].strip()
        force_load = False
        if ref[:6] == 'force ':
            ref = ref[6:].strip()
            force_load = True
        if ref[-3:] != '.kv':
            return
        if ref in _includes:
            if not force_load:
                return
            Builder.unload_file(ref)
            Builder.load_file(ref)
        else:
            _includes.append(ref)
            Builder.load_file(ref)
    elif cmd[:7] == 'import ':
        package = cmd[7:].strip()
        l = package.split(' ')
        if len(l) != 2:
            return
        alias, package = l
        try:
            if package not in sys.modules:
                try:
                    mod = __import__(package)
                except ImportError:
                    mod = __import__('.'.join(package.split('.')[:-1]))
                for part in package.split('.')[1:]:
                    mod = getattr(mod, part)
            else:
                mod = sys.modules[package]
            globals()[alias] = mod
        except ImportError:
            return


# directives

# register dynamic classes

# registration
badd = Builder.rules.append

# support for root object



_mc[1] = []
def _mc1(self):
    if self.__class__ in _mc[1]:
        return
    if not hasattr(self, "text"):
        self.create_property("text", "Hello World")
    
    _mc[1].append(self.__class__)

def _r1(self):
    # example.kv:0 Label:
    root = self

    # ensure all properties exists
    _mc1(self)

    # ids
    self.ids = {}
    # set default properties
    self.text = "Hello World"
    

    # shortcuts

    # link handlers

_r1.avoid_previous_rules = False
def get_root():
    widget = Factory.get("Label")()
    _r1(widget)
    return widget
    
