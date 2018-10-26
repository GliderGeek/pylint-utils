import click
from .disable import disable


@click.group()
@click.version_option()
def pylintrc():
    """pylintrc cli for creating and managing the pylint configuration file"""


pylintrc.add_command(disable)
