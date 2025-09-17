import sys

def downcase_it(s):
    return s.lower()

params = sys.argv[1:]

if not params:
    print("none")
else:
    for word in params:
        print(downcase_it(word))
