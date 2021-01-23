# Copyright (c) 2020 Jonathan Hildenbrand
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import click

from recalldatatool import db, factory

db_session = db()

usfda = factory.register_builder('USFDA_RECALL')
cfia = factory.register_builder('CFIA_RECALL')
ukfsa = factory.register_builder('UKFSA_RECALL')
efsa = factory.register_builder('EFSA_RECALL')


@click.command()
@click.option('--initdb-sqlite', help='Initialize a new recalls SQLite database')
@click.option('--initdb-pgsql', help='Initialize a new recalls PostgreSQL database')
def create_db():
    # Create a new SQLite database
    pass


@click.command('scrape')
@click.option('--source', '-s')
def scrape():
    # Start a web scraping session to update
    pass
