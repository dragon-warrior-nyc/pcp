import sys
if len(sys.argv) > 1:
    print( "~ Script: " + sys.argv[0])
    print( "~ Arg : " + sys.argv[1])
else:
    print(" No arguments ")

# try the following in command line
# python sys_argv.py
# python sys_argv.py 1
# python sys_argv.py 1 2
