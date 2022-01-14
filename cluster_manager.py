#!/bin/python3

#===============================================================================
# Author: Edson Manners
# Version: 0.1a
#===============================================================================

# Imports
import subprocess
import getopt, sys

# Sanitize command <==> option mapping
def command_mapping(opt):
    print("This is OPT: " + opt)
    if opt == 'kernel':
        return 'uname -r'
    elif opt == 'uptime':
        return 'uptime'
    elif opt == 'ibver':
        return 'ibstat'
    else:
        return 'unavailable'

# Main function
def main(argv):
    COMMAND = 'uname -r'
    HPC_HOSTS = 'threeleaf-left,threeleaf-4u'
    HPC_GROUPS = ''
    # https://www.w3schools.com/python/python_arrays.asp
    ARG_LIST = ['kernel','ibver',['uptime']]

    # Deal with parameters passed in
    # https://www.tutorialspoint.com/python/python_command_ling_arguments.htm
    try:
        opts, args = getopt.getopt(argv,"chv",['version','help'])
    except getopt.GetoptError:
        print('xom_cluster -c <command>')
        sys.exit(2)
    for opt, arg in opts:
        if opts in ('-h', '--help'):
            print('xom_cluster -c <command>\n')
            sys.exit(2)
        elif opt in ('-v', '--version'):
            print('xom_cluster version 0.1a\n')
            sys.exit(2)
        elif opt == 'c':
            COMMAND1 = command_mapping(arg)
            print(COMMAND1)
    
    # Read DSH group into array
    host_list = open("./test_nodes", "r")
    xom_hosts = host_list.readlines()
    host_list.close()

    # Get COMMAND results from HPC_HOSTS
    hpc_result = subprocess.run(['pdsh', '-w ' + HPC_HOSTS, COMMAND], stdout=subprocess.PIPE)
    print(hpc_result)

if __name__ == "__main__":
    main(sys.argv[1:])