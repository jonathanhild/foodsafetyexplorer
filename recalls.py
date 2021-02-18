# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click
import tqdm

from recalldatatool import factory, create_session


@click.group()
def cli():
    pass


@cli.command(help='Initialize a PostgreSQL or SQLite database.')
@click.option('--database', '-db', type=click.Choice(['pgsql', 'sqlite']))
@click.option()
def init(database):
    if database == 'pgsql':
        pass
    if database == 'sqlite':
        pass


@cli.command(help='Retrieve data from recall event sources.')
@cli.option('--all', '-a')
@cli.option('--source', '-s', type=click.Choice(['usfda', 'cfia', 'ukfsa', 'efsa']))
def scrape():
    pass


@cli.command(help='Run machine learning models.')
def model():
    pass


@cli.command(help='Start the recalls dashboard.')
def start():
    pass


if __name__ == '__main__':
    cli()
