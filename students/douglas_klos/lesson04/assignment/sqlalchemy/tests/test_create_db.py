# pylint: disable=E0401
"""
    Tests for create_db.py
"""

import logging
from sqlalchemy import exc
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import create_db as cdb


def test_add_tables():
    """Test add_tables function
    """
    engine = create_engine("sqlite:///HPNorton.db")
    db_session = sessionmaker(bind=engine)
    session = db_session()
    metadata = MetaData(bind=engine)
    cdb.add_tables(engine)

    # Verifies that table is created in database
    try:
        customers = Table("Customer", metadata, autoload=True)
    except exc.NoSuchTableError:
        raise exc.NoSuchTableError

    fields = str(session.query(customers))

    # Verifies that all expected columns are present.
    assert "customer_id" in fields
    assert "name" in fields
    assert "last_name" in fields
    assert "home_address" in fields
    assert "phone_number" in fields
    assert "email_address" in fields
    assert "status" in fields
    assert "credit_limit" in fields


def test_get_line():
    """Test get_line function
    """
    lines = [x for x in range(10)]
    for num, line in enumerate(cdb.get_line(lines)):
        assert line == lines[num]


def test_open_file():
    """Test open file function
    """
    file = cdb.open_file("./data/head-cust.csv")

    with open("./data/head-cust.csv", "rb") as content:
        next(content)
        lines = content.read().decode("utf-8", errors="ignore").split("\n")
        for line in lines:
            assert line in file


def test_parse_cmd_arguments():
    """Test parse_cmd_arguments function
    """
    parser = cdb.parse_cmd_arguments(["-i", "./data/head-cust.csv"])
    print(parser.input)
    assert parser.input == "./data/head-cust.csv"
    assert parser.blank is False
    parser = cdb.parse_cmd_arguments(["-i", "./data/head-cust.csv", "-b"])
    assert parser.blank is True


def test_populate_database():
    """Test populate_database function
    """
    engine = create_engine("sqlite:///HPNorton.db")
    db_session = sessionmaker(bind=engine)
    session = db_session()
    metadata = MetaData(bind=engine)
    customers = Table("Customer", metadata, autoload=True)

    # Seed database
    with open("./data/head-cust.csv", "rb") as content:
        next(content)
        lines = content.read().decode("utf-8", errors="ignore").split("\n")
        for line in lines:
            cdb.populate_database(line, session)

    # Make sure we cover code for IntegriteError, assert records are skipped.
    with open("./data/head-cust.csv", "rb") as content:
        next(content)
        lines = content.read().decode("utf-8", errors="ignore").split("\n")
        for line in lines[:-1]:
            customer = line.split(",")
            record = str(cdb.populate_database(line, session))
            assert (
                f"Records already in database. Skipping. {customer[0]}"
                in record
            )

    # Assert records are present.
    with open("./data/head-cust.csv", "rb") as content:
        next(content)
        lines = content.read().decode("utf-8", errors="ignore").split("\n")
        for line in lines[:-1]:
            customer = line.split(",")
            select_st = customers.select().where(
                customers.c.customer_id == customer[0]
            )
            query = session.execute(select_st)
            for item in query:
                # print(item.customer_id)
                assert item.customer_id == customer[0]
                assert item.name == customer[1]
                assert item.last_name == customer[2]
                assert item.home_address == customer[3]
                assert item.phone_number == customer[4]
                assert item.email_address == customer[5]
                assert item.status.lower() == customer[6].lower()
                assert int(item.credit_limit) == int(customer[7])

    cleanup_database(customers)


def test_main(caplog):
    """Test main function
    """
    engine = create_engine("sqlite:///HPNorton.db")
    db_session = sessionmaker(bind=engine)
    session = db_session()
    metadata = MetaData(bind=engine)
    customers = Table("Customer", metadata, autoload=True)

    caplog.set_level(logging.INFO)
    cdb.main(["-i", "./data/head-cust.csv"])
    output = [record for record in caplog.records]
    assert "Parsing command line arguments..." in str(output)
    assert "Initializes the HP Norton database from csv" in str(output)
    assert "Adding tables..." in str(output)
    for record in range(9):
        assert f"Adding record for C00000{record}" in str(output)

    assert "End of file" in str(output)
    assert "Closing database" in str(output)

    with open("./data/head-cust.csv", "rb") as content:
        next(content)
        lines = content.read().decode("utf-8", errors="ignore").split("\n")
        for line in lines[:-1]:
            customer = line.split(",")
            select_st = customers.select().where(
                customers.c.customer_id == customer[0]
            )
            query = session.execute(select_st)
            for item in query:
                assert item.customer_id == customer[0]
                assert item.name == customer[1]
                assert item.last_name == customer[2]
                assert item.home_address == customer[3]
                assert item.phone_number == customer[4]
                assert item.email_address == customer[5]
                assert item.status.lower() == customer[6].lower()
                assert int(item.credit_limit) == int(customer[7])

    cleanup_database(customers)


def cleanup_database(customers):
    """Remove records from database to prepare for next test
    """
    with open("./data/head-cust.csv", "rb") as content:
        next(content)
        lines = content.read().decode("utf-8", errors="ignore").split("\n")
        for line in lines[:-1]:
            customer = line.split(",")
            query = customers.delete().where(
                customers.c.customer_id == customer[0]
            )
            assert bool(query.execute()) is True
    # assert False
