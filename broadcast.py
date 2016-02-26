#!/usr/bin/env python
# -*- coding: utf-8 -*-

def coroutine(func):
	"""this is a decorator aiming to luanch coroutine automaticaly by calling next()"""
    def wrapper(*args, **kwargs):
	cr = func(*args, **kwargs)
	cr.next()
	return cr
    return wrapper

def station(content, *radiosets):
	"""this is not coroutine but a source content producer"""
    while content:
	for radioset in radiosets:
	    radioset.send(content[0])
	content.pop(0)

@coroutine
def radio(channel, loudspeaker):
	"""coroutine to consume source and pipe result to next coroutine"""
    while True:
	content = yield
	if content == channel:
	    loudspeaker.send(content)

@coroutine
def loudspeaker(id):
	"""finale coroutine that consumes the sent value"""
    while True:
	content = yield
	print 'loudspeaker',id,
	print content

def content_generator():
	"""a generator to generate the iteration"""
	for c in ['channel2', 'channel3', 'channel4', 'channel1', 'channel5'] * 10:
	    yield c

content = list(content_generator())
loudspeaker1 = loudspeaker(1)
loudspeaker2 = loudspeaker(2)
loudspeaker3 = loudspeaker(3)
radiosets = [radio('channel1', loudspeaker1), radio('channel2', loudspeaker2), radio('channel3', loudspeaker3)]

station(content, *radiosets)