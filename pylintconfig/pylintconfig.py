import click

from .disable import disable
from .ignore import ignore


@click.group()
@click.version_option()
def pylintconfig():
    """cli for creating and managing the pylint configuration file"""


pylintconfig.add_command(disable)
pylintconfig.add_command(ignore)
