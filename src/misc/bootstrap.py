from types import GeneratorType

'''
Never have problems with recursion limit again.
Mark a recursive function with @bootstrap,
but also instead of returning values, yield them.

Also when calling the function recursively unpack the value with yield.

Example:
@bootstrap
def SUM(n):
    if n == 0: yield 0
    yield n + (yield SUM(n-1))
'''
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc
