import sys

params = sys.argv[1:]

if not params:
    print("none")
else:
    for word in params:
        if not word.endswith("ism"):
            print(word + "ism")
