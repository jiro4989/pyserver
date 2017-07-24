#!/usr/bin/env python3
# -*- coding: utf-8 -*-

BASEDIR = './cgi-bin/form/'
LIST = '/cgi-bin/form.py'

def rep(html, url):
    top = 'http://localhost/'
    return html.format(url=top + url, list=LIST)

