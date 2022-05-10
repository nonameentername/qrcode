#!/usr/bin/env python

import qrcode
import sys

secret = sys.argv[1]
name = sys.argv[2]
img = qrcode.make('otpauth://totp/{name}:android?secret={secret}&issuer={name}'.format(secret=secret, name=name))
img.save('img.jpeg')
