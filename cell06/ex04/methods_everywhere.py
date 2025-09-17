import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s + "Z" * (8 - len(s)))

params = sys.argv[1:]

if not params:
    print("none")
else:
    for word in params:
        if len(word) > 8:
            shrink(word)
        elif len(word) < 8:
            enlarge(word)
        else:
            print(word)
