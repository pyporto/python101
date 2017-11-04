import sys

def hello():
    if len(sys.argv) == 2:
        print("Hello, {}".format(sys.argv[1]))
    elif len(sys.argv) == 3:
        print("Hello, {} and {}".format(sys.argv[1], sys.argv[2]))
    else:
        print("Hello world")


if __name__ == '__main__':
    hello()
