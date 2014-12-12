#!/usr/bin/env python
#-*-coding: utf-8 -*-

print(ord('A'))
print(chr(65))

print(u'中文')
print(u'\u4e2d')
print('ABC'.encode('utf-8'))
print('中文'.encode('utf-8'))
print(len(u'中文'))
print('\xe4\xb8\xad\xe6\x96\x87')
print(b'ABC')
print(b'ABC'.decode('utf-8'))
print(len(b'ABC'))
print(u'ABC')
print(len(u'ABC'))
print(b'\xe4\xb8\xad\xe6\x96\x87')
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('\xe4\xb8\xad\xe6\x96\x87'))

print('Hello,%s'%'world')
print('Hi,%s,you have $%d.'%('fiks',10000))

print('%2d-%02d'%(3,1))
print('%.2f'%3.1415926)
print('True or False:%s'%(True))

print('对还是错:%s'%(True))

print(u'中文'.encode('gb2312'))
print(u'中文'.encode('utf-8'))

