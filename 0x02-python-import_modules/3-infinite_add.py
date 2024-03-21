#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    argument_list = sys.argv[1:]
    for argument in argument_list:
        sum += int(argument)
    print("{}".format(sum))
