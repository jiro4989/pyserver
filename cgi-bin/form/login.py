#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util.formutil import *
from os.path import basename, splitext

name, ext = splitext(basename(__file__))

print('Content-type: text/html; charset=UTF-8\n')
with open(BASEDIR + name + '.html') as htmlfile:
    html = htmlfile.read()
    print(rep(html, 'test'))

