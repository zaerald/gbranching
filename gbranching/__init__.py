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
@version 1.0.2
__doc__
"""
import argparse
import re
import textwrap
from argparse import RawTextHelpFormatter

import pyperclip

__version__ = '1.0.2'


class Ticket:
    def __init__(self, title):
        self.title = title
        self.type = 'story'
        self.project_name = ''
        self.number = ''
        self.separator = '-'
        self.format = '{type}/{project}{sep}{number}{sep}{title}'


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

    return re.sub(branch_invalid_patterns, '', title, flags=re.VERBOSE).strip().replace(' ', '-').replace(',', '-')


def parse_number(_number):
    if not _number.isdigit():
        raise argparse.ArgumentTypeError(f"{_number} contains a letter, must only contain a digit.")
    return _number


def generate_branch_formatted(_ticket):
    return _ticket.format \
        .replace('{type}', _ticket.type) \
        .replace('{project}', _ticket.project_name) \
        .replace('{number}', str(_ticket.number)) \
        .replace('{title}', _ticket.title) \
        .replace('{sep}', _ticket.separator) \
        .replace(ticket.separator * 2, '')


parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
    gbranching a command line utility to easily transform ticket name to create branch names for Git. 
""", epilog=textwrap.dedent(f"""
    Author: Zaerald Denze Lungos
    Version: {__version__}
"""))

parser.add_argument('-t', '--type', choices=['story', 'bug', 'bau'],
                    help='the ticket type ')
parser.add_argument('-p', '--project',
                    help='project name initials')
parser.add_argument('-n', '--number', type=parse_number,
                    help='ticket number')
parser.add_argument('-f', '--format',
                    help='format of the generated ticket, default is {type}/{project}{sep}{number}{sep}{title}')
parser.add_argument('title', help='title of the ticket')
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
args = parser.parse_args()

ticket = Ticket(transform_title(args.title))

if args.type:
    ticket.type = args.type
if args.project:
    ticket.project_name = args.project.upper()
if args.number:
    ticket.number = args.number
if args.format:
    ticket.format = args.format

branch_name = generate_branch_formatted(ticket)
pyperclip.copy(branch_name)
print(f"'{branch_name}' is copied to clipboard!")
