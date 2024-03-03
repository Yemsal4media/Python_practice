#!/usr/bin/python3
import sys
arg_name = sys.argv[1:]
num_args = len(sys.argv) - 1
if num_args == 0:
    print("{} arguments.".format(num_args))
elif num_args == 1:
    print("{} argument:".format(num_args))
else:
    print("{} arguments:".format(num_args))

if __name__ == "__main__":
    for i in range(len(arg_name)):
        print("{}: {}".format(i+1, arg_name[i]))
