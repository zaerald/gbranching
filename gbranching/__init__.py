#! /usr/local/bin/python3
"""
gbranching
Command line utility to easily create branch names for Git from a ticket name.

Usage
```text
$ gbranching [-t <ticket-type>] [-n <ticket-number>] title
$ gbranching
$ gbranching title
```

@author Zaerald Denze Lungos
@version 1.0
__doc__
"""
import argparse
import re
import textwrap
from argparse import RawTextHelpFormatter

import pyperclip


def transform_title(title):
    title = title.lower()
    branch_invalid_patterns = r'''
        [.]|            # cannot start with a dot `.`
        [@{(..)\\\?'"]|   # must not contain any of this characters
        (@{)
        [\t\r\n\v\f]|   # exclude other white spaces except space ` `
        \-{2,}|         # remove consecutive `--`
        [/(.lock)]$     # must not end with `/` `.lock`
    '''

    return re.sub(branch_invalid_patterns, '', title, flags=re.VERBOSE).strip().replace(' ', '-')


parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
    gbranching a command line utility to easily transform ticket name to create branch names for Git. 
""", epilog=textwrap.dedent("""
    Author: Zaerald Denze Lungos
    Version: 1.0
"""))

parser.add_argument('-t', '--type', choices=['story', 'bug', 'bau'],
                    help='the ticket type ')
parser.add_argument('-p', '--project',
                    help='project name initials')
parser.add_argument('-n', '--number', type=int,
                    help='ticket number')
parser.add_argument('title', help='title of the ticket')
args = parser.parse_args()

ticket_type = 'story'
if args.type:
    ticket_type = args.type

project = ''
if args.project:
    project = f'{args.project}-'

ticket_number = ''
if args.number:
    ticket_number = f'{args.number}-'

branch_name = f'{ticket_type}/{project}{ticket_number}{transform_title(args.title)}'
pyperclip.copy(branch_name)

print(f"'{branch_name}' is copied to clipboard!")
