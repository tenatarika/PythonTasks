# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:35:32 2021

@author: Furcas
"""

import time 
import wsgiref.simple_server
import 

def hello_world(environ, start_response):
    headers = [
            ("Context-type", "text/html; charset=utf-8"),
            ("Context=Security-Policy", "default-src 'none';"),
        ]
    
    start_response("200 OK", headers)
    yield b"<html><body>"
    
    for i in range(20):
        yield b"<p>hello world</p>"
        for i in range(10):
            time.sleep(0.5)
            yield b"<h1>RaRe</h1>"
        time.sleep(1)
    
    yield b"</body></html>"
    
    
    
if __name__ == "__main__":
    with wsgiref.simple_server.make_server("", 8000, hello_world) as server:
        server.serve_forever()