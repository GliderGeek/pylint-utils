"""
This script simplifies setting up pylint on an existing python project.
It checks which errors are raised and creates a pylint rc file which disables all the errors.
These can then be checked and pruned to achieve at the desired settings.
Warning: when there is already a pylintrc file, it is completely replaced.
"""

import os
import subprocess

pylintrc_path = '.pylintrc'
code_path = 'opensoar'

# todo: add check on current file (same defaults as pylint)
# accept pylintrc flag for location if different

# output to screen, not to disc

# output can be piped if wanted

# todo: make click cli


def get_disabled_symbols(pylintrc_path: str):
    # todo: pylint use argparse for reading in file, could be used here too

    # todo: also parse other parts

    symbols = set()
    if os.path.exists(pylintrc_path):
        with open(pylintrc_path) as f:
            inside_disable_part = False
            for line in f.readlines():
                if not inside_disable_part and line.startswith('disable='):
                    inside_disable_part = True

                if inside_disable_part:
                    if line.startswith('disable='):
                        _, symbol = line.split('=')
                        symbol = symbol.strip()
                    elif line.strip() == '':
                        continue
                    else:
                        symbol = line.strip()

                    if symbol.endswith(','):
                        symbol = symbol.strip(',')
                    else:
                        inside_disable_part = False

                    symbols.add(symbol)

    return symbols


def get_error_symbols(code_path):
    symbols = set()

    if not os.path.exists(code_path):
        raise IOError('Invalid path')

    result = subprocess.check_output(['pylint', "--msg-template='# {msg_id}: {symbol}'", code_path, '--exit-zero'])

    for line in result.decode('utf-8').splitlines():
        if line.startswith('#'):
            _, symbol = line.split(':')
            symbols.add(symbol.strip())

    return symbols


def print_pylintrc(symbols: set):

    # todo: distinguish between new symbols and already existing symbols

    print('[MESSAGES CONTROL]')
    for i, symbol in enumerate(symbols):
        if i == 0:
            print(f'disable={symbol},')
        else:
            print(f'        {symbol},')


disabled_symbols = get_disabled_symbols(pylintrc_path)
error_symbols = get_error_symbols(code_path)
all_symbols = disabled_symbols | error_symbols
print_pylintrc(all_symbols)
