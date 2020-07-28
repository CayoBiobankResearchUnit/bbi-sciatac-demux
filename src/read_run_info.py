#!/usr/bin/python3

import sys
import json
import run_info

if __name__ == '__main__':
    pathname = sys.argv[1]
    run_info_json = run_info.get_run_info( pathname )
    json.dump( run_info_json, sys.stdout, indent = 4 )
