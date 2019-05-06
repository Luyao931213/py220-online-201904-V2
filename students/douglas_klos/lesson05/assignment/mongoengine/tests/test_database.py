"""grade lesson 5
"""

import pytest
import src.database_operations as l


@pytest.fixture
def _show_available_products():
    """ Expected output for show available products call """
    return {
        "prd001": {
            "description": "60-inch TV stand",
            "product_type": "livingroom",
            "quantity_available": 3,
        },
        "prd003": {
            "description": "Acacia kitchen table",
            "product_type": "kitchen",
            "quantity_available": 7,
        },
        "prd004": {
            "description": "Queen bed",
            "product_type": "bedroom",
            "quantity_available": 10,
        },
        "prd005": {
            "description": "Reading lamp",
            "product_type": "bedroom",
            "quantity_available": 20,
        },
        "prd006": {
            "description": "Portable heater",
            "product_type": "bathroom",
            "quantity_available": 14,
        },
        "prd008": {
            "description": "Smart microwave",
            "product_type": "kitchen",
            "quantity_available": 30,
        },
        "prd010": {
            "description": "60-inch TV",
            "product_type": "livingroom",
            "quantity_available": 3,
        },
    }


@pytest.fixture
def _show_rentals():
    """ Expected output for show rentals call """
    return {
        "user005": {
            "name": "Dan Sounders",
            "address": "861 Honeysuckle Lane",
            "zip_code": "98244",
            "phone_number": "206-279-1723",
            "email": "soundersoccer@mls.com",
        },
        "user008": {
            "name": "Shirlene Harris",
            "address": "4329 Honeysuckle Lane",
            "zip_code": "98055",
            "phone_number": "206-279-5340",
            "email": "harrisfamily@gmail.com",
        },
    }


@pytest.fixture
def _list_all_customers():
    """ Expected output for list all customeers """
    return {
        "user001": {
            "address": "4490 Union Street",
            "email": "elisa.miles@yahoo.com",
            "name": "Elisa Miles",
            "phone_number": "206-922-0882",
            "zip_code": "98109",
        },
        "user002": {
            "address": "4936 Elliot Avenue",
            "email": "mdata@uw.edu",
            "name": "Maya Data",
            "phone_number": "206-777-1927",
            "zip_code": "98115",
        },
        "user003": {
            "address": "348 Terra Street",
            "email": "andy.norris@gmail.com",
            "name": "Andy Norris",
            "phone_number": "206-309-2533",
            "zip_code": "98501",
        },
        "user004": {
            "address": "885 Boone Crockett Lane",
            "email": "matseattle@pge.com",
            "name": "Flor Matatena",
            "phone_number": "206-414-2629",
            "zip_code": "97209",
        },
        "user005": {
            "address": "861 Honeysuckle Lane",
            "email": "soundersoccer@mls.com",
            "name": "Dan Sounders",
            "phone_number": "206-279-1723",
            "zip_code": "98244",
        },
        "user006": {
            "address": "2725 Mutton Town Road",
            "email": "leo.dembele@comcast.com",
            "name": "Leo Dembele",
            "phone_number": "206-203-1294",
            "zip_code": "98368",
        },
        "user007": {
            "address": "668 Elliot Avenue",
            "email": "nicholasp@amazon.com",
            "name": "Pete Nicholas",
            "phone_number": "206-279-8759",
            "zip_code": "98115",
        },
        "user008": {
            "address": "4329 Honeysuckle Lane",
            "email": "harrisfamily@gmail.com",
            "name": "Shirlene Harris",
            "phone_number": "206-279-5340",
            "zip_code": "98055",
        },
        "user009": {
            "address": "4679 Goodwin Avenue",
            "email": "nick.rather@microsoft.com",
            "name": "Nick Rather",
            "phone_number": "206-777-1965",
            "zip_code": "98619",
        },
        "user010": {
            "address": "2717 Raccoon Run",
            "email": "joegarza@boeing.com",
            "name": "Jose Garza",
            "phone_number": "206-946-8200",
            "zip_code": "98116",
        },
    }


@pytest.fixture
def _list_all_products():
    """ Expected output for list_all_products() """
    return {
        "prd001": {
            "description": "60-inch TV stand",
            "product_type": "livingroom",
            "quantity_available": 3,
        },
        "prd002": {
            "description": "L-shaped sofa",
            "product_type": "livingroom",
            "quantity_available": 0,
        },
        "prd003": {
            "description": "Acacia kitchen table",
            "product_type": "kitchen",
            "quantity_available": 7,
        },
        "prd004": {
            "description": "Queen bed",
            "product_type": "bedroom",
            "quantity_available": 10,
        },
        "prd005": {
            "description": "Reading lamp",
            "product_type": "bedroom",
            "quantity_available": 20,
        },
        "prd006": {
            "description": "Portable heater",
            "product_type": "bathroom",
            "quantity_available": 14,
        },
        "prd007": {
            "description": "Ballerina painting",
            "product_type": "livingroom",
            "quantity_available": 0,
        },
        "prd008": {
            "description": "Smart microwave",
            "product_type": "kitchen",
            "quantity_available": 30,
        },
        "prd009": {
            "description": "Popcorn machine",
            "product_type": "kitchen",
            "quantity_available": 0,
        },
        "prd010": {
            "description": "60-inch TV",
            "product_type": "livingroom",
            "quantity_available": 3,
        },
    }


@pytest.fixture
def _list_rentals_for_customer():
    """ Expected output for list_rentals_for_customers """
    return {
        "prd007": {
            "description": "Ballerina painting",
            "product_type": "livingroom",
            "quantity_available": 0,
        },
        "prd010": {
            "description": "60-inch TV",
            "product_type": "livingroom",
            "quantity_available": 3,
        },
    }


def test_import_data():
    """ import """
    l.drop_collections()

    data_dir = "./data/"
    added, errors = l.import_data(
        data_dir, "product.csv", "customers.csv", "rental.csv"
    )

    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)

    added, errors = l.import_data(
        data_dir, "product.csv", "customers.csv", "rental.csv"
    )

    assert added == (0, 0, 0)
    assert errors == (10, 10, 9)


def test_insert_to_mongo():
    """ import given csv file into mongo """

    l.drop_collections()
    data_dir = "./data/"

    added, errors = l.insert_to_mongo(data_dir, "product.csv")
    assert isinstance(added, int)
    assert isinstance(errors, int)
    assert added == 10
    assert errors == 0

    added, errors = l.insert_to_mongo(data_dir, "product.csv")
    assert added == 0
    assert errors == 10

    added, errors = l.insert_to_mongo(data_dir, "customers.csv")
    assert isinstance(added, int)
    assert isinstance(errors, int)
    assert added == 10
    assert errors == 0

    added, errors = l.insert_to_mongo(data_dir, "customers.csv")
    assert added == 0
    assert errors == 10

    added, errors = l.insert_to_mongo(data_dir, "rental.csv")
    assert isinstance(added, int)
    assert isinstance(errors, int)
    assert added == 9
    assert errors == 0

    added, errors = l.insert_to_mongo(data_dir, "rental.csv")
    assert added == 0
    assert errors == 9


def test_show_available_products(_show_available_products):
    """ available products """
    students_response = l.show_available_products()
    print(students_response)
    assert students_response == _show_available_products


def test_list_all_customers(_list_all_customers):
    """ customers """
    my_response = l.list_all_customers()
    assert my_response == _list_all_customers


def test_list_all_products(_list_all_products):
    """ customers """
    my_response = l.list_all_products()
    assert my_response == _list_all_products


def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = l.show_rentals("prd002")
    assert students_response == _show_rentals


def test_rentals_for_customer(_list_rentals_for_customer):
    """ rentals for customers """
    my_response = l.rentals_for_customer("user002")
    assert my_response == _list_rentals_for_customer


def test_get_line():
    """Test get_line function
    """
    lines = [x for x in range(10)]
    for num, line in enumerate(l.get_line(lines)):
        assert line == lines[num]


def test_open_file():
    """Test open file function
    """
    file = l.open_file("./data/customers.csv")

    with open("./data/customers.csv", "rb") as content:
        next(content)
        lines = content.read().decode("utf-8-sig", errors="ignore").split("\n")
        for line in lines:
            assert line in file


def test_drop_databases():
    """Test drop HPNorton database
    """
    l.drop_database()

    data_dir = "./data/"
    added, errors = l.import_data(
        data_dir, "product.csv", "customers.csv", "rental.csv"
    )

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)

    l.drop_database()

    # If drop_database() wasn't working, the following assertions would fail.
    #   This is a sloppy test and I don't like it, works though...
    #   It's something I'd improve upon in a production environment.
    #   But time is limitied, so I choose to move on to new things to learn.

    added, errors = l.import_data(
        data_dir, "product.csv", "customers.csv", "rental.csv"
    )

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)


def test_drop_collections():
    """Test drop HPNorton collections
    """
    l.drop_collections()

    data_dir = "./data/"
    added, errors = l.import_data(
        data_dir, "product.csv", "customers.csv", "rental.csv"
    )

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)

    l.drop_collections()

    # If drop_collections() wasn't working, the following assertions would fail.

    added, errors = l.import_data(
        data_dir, "product.csv", "customers.csv", "rental.csv"
    )

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)
