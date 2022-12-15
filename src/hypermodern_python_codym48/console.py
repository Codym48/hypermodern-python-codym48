import click

from hypermodern_python_codym48 import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """Codym48's hypermodern Python project."""
    click.echo("Hello, world!")