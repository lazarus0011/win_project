#coding=utf-8
import re
import asyncio
import time


@asyncio.coroutine
def f():
	time.sleep(1)
	print('world')
	return "abc"
	
	

@asyncio.coroutine
def hello():
	print('hello')
#	r = yield from asyncio.sleep(3)
	r = yield from f()
	print(r)
	print('hello again')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
print('end')
loop.close()
