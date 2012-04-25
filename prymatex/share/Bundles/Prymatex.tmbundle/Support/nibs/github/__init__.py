#!/usr/bin/env python
#-*- encoding: utf-8 -*-

from github.getbundle import GitHubBundlesDialog

def load(application):
    GitHubBundlesDialog.application = application
    dialog = GitHubBundlesDialog(application.mainWindow)
    dialog.show()