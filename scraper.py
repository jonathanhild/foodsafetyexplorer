# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click
import tqdm

from data_scraper import factory
from data_scraper import database as db
from data_scraper import openfda

db_options = click.Choice(['pgsql', 'sqlite'])
source_options = click.Choice(
    ['recalls', 'adverseevents', 'inspectionclassifications', 'inspectioncitations', 'importrefusals']
)


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


@cli.command(help='Retrieve data from API sources.')
@click.option('--source', '-s', type=source_options, multiple=True)
@click.option('--database', '-db', type=db_options)
@click.option('--filepath', '-f', type=str)
def scrape(source, database, filepath):

    # Create a new session to the chosen database.
    session = db.create_session(database=database, path=filepath)

    if 'recalls' in source:
        recall = factory.create('OPENFDA_RECALL')
        recall.get_metadata()
        recall.get_events()
        recall.to_db(session)


@cli.command(help='Run machine learning models.')
def model():
    pass


@cli.command(help='Start the recalls dashboard.')
def start():
    pass


if __name__ == '__main__':
    cli()
