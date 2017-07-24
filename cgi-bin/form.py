#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Content-type: text/html; charset=UTF-8\n')

with open('./cgi-bin/form.html') as htmlfile:
    html = htmlfile.read()

    links = ''
    linktag = '<a href="/cgi-bin/form/{link}">{link}</a><br>'
    dirs = [d for d in os.listdir('./cgi-bin/form') if d.endswith('.py')]
    for d in dirs:
        links += linktag.format(link=str(d))

    print(html.format(links=links))

