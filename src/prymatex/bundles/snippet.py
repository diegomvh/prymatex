#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Snippte's module
'''

from prymatex.bundles.base import PMXBundleItem
from prymatex.bundles.processor import PMXDebugSyntaxProcessor

class PMXSnippet(PMXBundleItem):
    parser = None
    def __init__(self, hash, name_space = "default"):
        super(PMXSnippet, self).__init__(hash, name_space)
        for key in [    'content', 'disableAutoIndent', 'inputPattern', 'bundlePath' ]:
            setattr(self, key, hash.pop(key, None))
    
    def compile(self):
        if self.parser == None:
            #FIXME: obtenerlo de una forma mas limpia
            self.__class__.parser = self.bundle.getBundleByName('Bundle Development').syntaxes[1]
        self.parser.parse(self.content, PMXDebugSyntaxProcessor())