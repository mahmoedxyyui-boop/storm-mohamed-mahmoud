# -*- coding: utf-8 -*-
import urllib.request
import json

try:
    with open('assets/images/brand/qr_code.png', 'rb') as f:
        file_bytes = f.read()

    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    body = (
        f'--{boundary}\r\n'
        'Content-Disposition: form-data; name="file"; filename="qr.png"\r\n'
        'Content-Type: image/png\r\n\r\n'
    ).encode('utf-8') + file_bytes + f'\r\n--{boundary}--\r\n'.encode('utf-8')

    req = urllib.request.Request(
        'https://api.qrserver.com/v1/read-qr-code/',
        data=body,
        headers={'Content-Type': f'multipart/form-data; boundary={boundary}'}
    )
    with urllib.request.urlopen(req, timeout=10) as res:
        data = json.loads(res.read().decode('utf-8'))
        print('Decoded data:', data)
except Exception as e:
    print('Decode error:', e)
