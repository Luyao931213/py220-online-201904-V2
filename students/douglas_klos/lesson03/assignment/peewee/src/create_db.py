#!/usr/bin/env python3
#pylint: disable=E0401
"""
    Imports customer.csv to sqlite database
"""

# Execution time for seeding the database: 293.8888795375824 seconds.
# System: Linux Mint 19, Core i7-6700k at 4.4GHz, 32GB DDR4, NVME2 Drive
# CPU usage was only around 5-6% for the process.
# I feel like it should have at least maxed one core and done this
#   much more quickly, they're more than enough RAM / CPU power.
#   Why is this bottlenecked so badly?


import sys
import logging
import argparse
import time
from peewee import IntegrityError
import db_model as db

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def main():
    """Initializes HPNorton database
    """
    start = time.time()
    args = parse_cmd_arguments()
    LOGGER.info("Initializes the HP Norton database from csv")
    LOGGER.info("Adding tables...")
    add_tables()
    if not args.blank:
        populate_database(args.input)
    LOGGER.info("Closing database")
    db.database.close()
    LOGGER.info("Time to init: %s", time.time() - start)


def parse_cmd_arguments():
    """Parses the command line arguments

    Returns:
        ArgumentParser.parse_args
    """
    parser = argparse.ArgumentParser(description="Build HP Norton Database")
    parser.add_argument("-i", "--input", help="input CSV file", required=True)
    parser.add_argument(
        "-b",
        "--blank",
        help="column headers only, no row data",
        action="store_true",
        required=False,
        default=False,
    )
    parser.add_argument("-d", "--debug", help="debugger level", required=False)

    return parser.parse_args()


def add_tables():
    """Adds tables to database"""
    db.database.create_tables([db.Customer])


def populate_database(filename):
    """Populates database from csv file"

    Arguments:
        filename {string} -- csv file to be read
    """
    with open(filename, "rb") as content:
        next(content)  # Skip first line, it's the column names
        lines = content.read().decode("utf-8", errors="ignore").split("\n")
        for line in lines:
            customer = line.split(",")
            try:
                with db.database.transaction():
                    db.Customer.create(
                        customer_id=customer[0],
                        name=customer[1],
                        last_name=customer[2],
                        home_address=customer[3],
                        phone_number=customer[4],
                        email_address=customer[5],
                        status=customer[6].lower(),
                        credit_limit=customer[7],
                    )
                    LOGGER.info("Adding record for %s", customer[0])
            except IndexError:
                LOGGER.info("End of file")
            except IntegrityError:
                LOGGER.info("Records already in database. Exiting.")
                sys.exit(0)


if __name__ == "__main__":
    main()
