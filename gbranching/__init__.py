#! /usr/local/bin/python3
"""
gbranching
Command line utility to easily create branch names for Git from a ticket name.

@author Zaerald Denze Lungos
@version 1.0
"""
import re
import sys
import pyperclip

args = sys.argv

branch_name = str(args[1]).lower()
branch_invalid_patterns = r'''
    [.]|            # cannot start with a dot `.`
    [@{(..)\\\?]|   # must not contain any of this characters
    (@{)
    [\t\r\n\v\f]|   # exclude other white spaces except space ` `
    \-{2,}|         # remove consecutive `--`
    [/(.lock)]$     # must not end with `/` `.lock`
'''

branch_name = re.sub(branch_invalid_patterns, '', branch_name, flags=re.VERBOSE).strip().replace(' ', '-')
pyperclip.copy(branch_name)

print(branch_name)
