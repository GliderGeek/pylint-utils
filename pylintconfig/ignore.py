import subprocess

import click


def _get_files_per_error(code_path: str) -> dict:

    result = subprocess.check_output(['pylint', "--msg-template='# {path} {symbol}'", code_path, '--exit-zero'])

    symbols = {}
    for line in result.decode('utf-8').splitlines():

        if line.startswith('#'):
            _, file_path, symbol = line.split(' ')
            file_name = file_path.split('/')[-1]

            if symbol in symbols:
                if file_name not in symbols[symbol]:
                    symbols[symbol].add(file_name)
            else:
                symbols[symbol] = {file_name}

    return symbols


def _print_pylintrc_content(errors: dict):
    if errors:

        click.echo('[MASTER]')
        for i, (error, file_names) in enumerate(errors.items()):
            for j, file_name in enumerate(file_names):
                if i == 0 and j == 0:
                    click.echo("ignore={0:30} # {1}".format(f'{file_name},', error))
                elif i != 0 and j == 0:
                    click.echo("")
                    click.echo("       {0:30} # {1}".format(f'{file_name},', error))
                else:
                    click.echo("       {0:30}".format(f'{file_name},'))


@click.command()
@click.argument('modules_or_packages', type=click.Path(exists=True))
def ignore(modules_or_packages):
    """
    Run pylint and provide a configuration which explicitly ignores all files with errors. These files can then
    be fixed one at a time: like a todo list for necessary code changes.

    \b
    This command can be nicely combined with the `disable` command in the following workflow:
    1. run the `disable` command to explicitly disable all present errors
    2. prune the disable list to activate the errors you care about
    3. run the `ignore` command to create a ignore list of files with errors
    4. treat this list as a todo list and improve your codebase one error at a time.

    Don't execute this command when you already have a pylintrc file with ignored files.
    These suppressed files will not be present in the output and might lead to confusing results.
    """
    errors = _get_files_per_error(modules_or_packages)
    _print_pylintrc_content(errors)
