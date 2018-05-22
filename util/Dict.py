#!/usr/bin/env python
# coding: utf-8
#
# Author: Mackee <demin7926@gmail.com>
# Date: Tue Man 22, 2018
#
# Licensed Declare: 
#   NO LICENSE
#


class Dict(dict):
    """ A costom dict class support the dot syntax.
    """

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value





