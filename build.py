"""Builds index.html from src/. Run: python3 build.py"""
import os
d=os.path.dirname(os.path.abspath(__file__))
rd=lambda p:open(os.path.join(d,p),encoding='utf-8').read()
head=rd('src/head.html'); i18n=rd('src/i18n.js'); app=rd('src/app.js').replace('/*__I18N__*/',i18n)
i=head.index('<div id="app"')
top,body=head[:i],head[i:]
pwa='''<meta name="theme-color" content="#0B1530">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Tazivo">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>html{padding-top:env(safe-area-inset-top,0px);background:#0B1530}</style>'''
html=('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 +pwa+'\n'+top+'</head><body>\n'+body+'\n<script>\n(function(){\n\'use strict\';\n'+app+'\n})();\n'
 "if('serviceWorker' in navigator&&location.protocol.indexOf('http')===0){navigator.serviceWorker.register('sw.js').catch(function(){});}\n</script>\n</body></html>\n")
open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(html)
print('index.html written',len(html),'bytes')
