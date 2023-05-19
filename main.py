import sys, pluto24

def main():
    defs = {}
    stack = []
    for arg in sys.argv[1:]:
        pluto24.parse(open(arg).read(), defs)

    pluto24.run(stack, defs, 'main')

if __name__ == '__main__':
    main()
