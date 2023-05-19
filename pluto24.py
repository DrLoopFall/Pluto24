import sys

def parse(src, defs):
    for i in src.split():
        if i[-1] == ':': defs[i[:-1]] = curr = []
        else: curr.append(i)

def run(stack, defs, fn):
    def runfn(fn):
        fnc = {
            'add' : lambda a, b    : a + b,
            'sub' : lambda a, b    : a - b,
            'mul' : lambda a, b    : a * b,
            'div' : lambda a, b    : a // b,
            'mod' : lambda a, b    : a % b,
            'copy': lambda i       : stack[-i],
            'drop': lambda i       : stack.pop(-i) is None or None,
            'if'  : lambda cnd, fn : runfn(fn) if cnd > 0 else None,
            'get' : lambda         : ord(sys.stdin.read(1)),
            'put' : lambda i       : print(chr(i), end='', flush=True)
        }.get(fn,   lambda         : run(stack, defs, fn))
        args = [stack.pop() for _ in  range(fnc.__code__.co_argcount)][::-1]
        return fnc(*args)

    for i in defs[fn]:
        res = int(i) if i.isdigit() else i[1:] if i[0] == '&' else runfn(i)
        if res is not None: stack.append(res)
