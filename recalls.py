# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click
import tqdm

from recalldatatool import factory
from recalldatatool import database as db
from recalldatatool import usfda

db_options = click.Choice(['pgsql', 'sqlite'])
source_options = click.Choice(['usfda', 'cfia', 'ukfsa', 'efsa'])


@click.group()
def cli():
    pass


@cli.command(help='Initialize a PostgreSQL or SQLite database.')
@click.option('--database', '-db', type=db_options)
def init(database):
    session = None

    if database == 'pgsql':
        db._pgsql_env_file()
        username, password = db._pgsql_get_vars()
        pgsql_conn = db._pgsql_conn(username, password)
        session = db.create_session(pgsql_conn, create_all=True)
        click.echo('PostgreSQL database successfully created.')
    if database == 'sqlite':
        sqlite_conn = db._sqlite_conn()
        session = db.create_session(sqlite_conn)

    return session


@cli.command(help='Retrieve data from recall event sources.')
@click.option('--source', '-s', type=source_options, multiple=True)
@click.option('--database', '-db', type=db_options)
@click.option('--filepath', '-f', type=str)
def scrape(source, database, filepath):

    # Create a new session to the chosen database.
    session = db.create_session(database=database, path=filepath)

    if 'usfda' in source:
        usfda = factory.create('USFDA_RECALL')
        usfda.get_metadata()
        usfda.get_events()
        usfda.to_db(session)
    if 'cfia' in source:
        cfia = factory.create('CFIA_RECALL')
        cfia.get_event_urls()
        cfia.get_events()
        cfia.get_product_details()
        cfia.to_db(session)
    if 'ukfsa' in source:
        pass
    if 'efsa' in source:
        pass


@cli.command(help='Run machine learning models.')
def model():
    pass


@cli.command(help='Start the recalls dashboard.')
def start():
    pass


if __name__ == '__main__':
    cli()
