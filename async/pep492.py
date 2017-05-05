from types import coroutine

def pure_gen():
    '''pure generator'''
    for i in range(2):
        yield i

@coroutine
def gen_cor():
    '''generator based coroutine'''
    for i in range(2):
        yield 'gen_cor:'+str(i)

@coroutine
def gen_cor2():
    '''generator based coroutine'''
    for i in range(2):
        yield 'gen_cor2 inside native coroutine:'+str(i)

async def ag():
    '''
    async-generator: in python3.5 this would throw a syntax Error
    you cannot yield in an async def in python3.5, but python3.6 can   
    '''
    for i in range(2):
        yield i

async def native_cor():
    '''native coroutine'''
    await gen_cor2()

pure_gen_i = pure_gen()
gen_cor_i = gen_cor()
ag_i = ag()
native_cor_i = native_cor()

#prints out generator
print(pure_gen_i)
#prints out generator
print(gen_cor_i)
#prints out aync-generator
print(ag_i)
#prints out coroutine
print(native_cor_i)

class Future:
    '''Objects with __await__ method are called Future-like objects.'''
    def __init__(self, data):
        self.data = data
    def __await__(self):
        return iter(self.data)

f = Future('future')

async def wait_fun():
    '''
    await only accepts an awaitable , which can be one of:
    1. A native coroutine object returned from a native coroutine function .
    2. A generator-based coroutine object returned from a function decorated with types.coroutine() .
    3. An object with an __await__ method returning an iterator.
    '''
    print('#1')
    #1
    await native_cor_i
    print('#2')
    #2
    await gen_cor_i
    print('#3')
    #3
    await f
    print('Done')

wf = wait_fun()
while True:
    try:
        print(wf.send(None))
    except:
        break

class AsyncContextManager:
    '''
    a new protocol for asynchronous context managers
    __aenter__ and __aexit__ both must return an awaitable .
    '''
    async def __aenter__(self):
        print('__aenter__')
        await gen_cor()
    async def __aexit__(self, exec_type, exec_val, traceback):
        print('__aexit__')
        await Future('FUTURE')

async def use_async_cm():
    '''It is a SyntaxError to use async with outside of an async def function.'''
    async with AsyncContextManager():
        print(ac)

use_async_cm_i = use_async_cm()
while True:
    try:
        print(use_async_cm_i.send(None))
    except:
        break


class AsyncIterator:
    def __init__(self, future):
        self.future = future

    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await self.future
        if data:
            return data
        else:
            raise StopAsyncIteration

f = Future('12345')

async def ai():
    '''It is a SyntaxError to use async with outside of an async def function.'''
    async for i in AsyncIterator(f):
        print(i)

ai_i = ai()
while True:
    try:
        print(ai_i.send(None))
    except:
        break
