import subprocess

import click


def _get_current_errors(code_path: str) -> set:
    symbols = set()

    result = subprocess.check_output(['pylint', "--msg-template='# {msg_id}: {symbol}'", code_path, '--exit-zero'])

    for line in result.decode('utf-8').splitlines():
        if line.startswith('#'):
            _, symbol = line.split(':')
            symbols.add(symbol.strip())

    return symbols


def _print_pylintrc_content(symbols: set):
    click.echo('[MESSAGES CONTROL]')
    for i, symbol in enumerate(symbols):
        if i == 0:
            click.echo(f'disable={symbol},')
        else:
            click.echo(f'        {symbol},')


@click.command()
@click.argument('modules_or_packages', type=click.Path(exists=True))
def disable(modules_or_packages):
    """
    Run pylint and provide a configuration which explicitly disables all errors.
    This command is very useful for an initial setup of pylint in an existing codebase.

    \b
    This command can be nicely combined with the `ignore` command in the following workflow:
    1. run the `disable` command to explicitly disable all present errors
    2. prune the disable list to activate the errors you care about
    3. run the `ignore` command to create a ignore list of files with errors
    4. treat this list as a todo list and improve your codebase one error at a time.

    Don't execute this command when you already have a pylintrc file with disabled errors.
    These suppressed errors will not be present in the output and might lead to confusing results.
    """
    error_symbols = _get_current_errors(modules_or_packages)
    _print_pylintrc_content(error_symbols)
