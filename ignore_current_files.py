"""
This is the last step in setting up pylint (step3).
1. Disable all errors/warning
2. Prune and enable the ones you think are import
3. Disable the current files to enable gradual implementation, but prevent them from occurring in new files

This script runs pylint, checks which errors are present and suggests an ignore list
"""


import subprocess


code_path = 'opensoar'

#todo: add check on current file (same defaults as pylint)
# accept pylintrc flag for location if different

#output to screen. can then be piped if wanted

#todo: deal with duplicate file_names


def get_symbols(code_path: str):
    result = subprocess.check_output(['pylint', "--msg-template='# {path} {symbol}'", code_path, '--exit-zero'])

    symbols = {}
    for line in result.decode('utf-8').splitlines():

        if line.startswith('#'):
            _, file_path, symbol = line.split(' ')
            file_name = file_path.split('/')[-1]

            if symbol in symbols:
                symbols[symbol].append(file_name)
            else:
                symbols[symbol] = [file_name]

    return symbols


symbols = get_symbols(code_path)
if symbols:

    print('[MASTER]')
    for i, (symbol, file_names) in enumerate(symbols.items()):
        for j, file_name in enumerate(file_names):
            if i == 0 and j == 0:
                print("ignore={0:30} # {1}".format(f'{file_name},', symbol))
            elif i != 0 and j == 0:
                print("")
                print("       {0:30} # {1}".format(f'{file_name},', symbol))
            else:
                print("       {0:30}".format(f'{file_name},'))

