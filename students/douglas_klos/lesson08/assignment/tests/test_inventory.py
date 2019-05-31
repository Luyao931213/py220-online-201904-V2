#!/usr/bin/env python3
#pylint: disable=C0103
""" Autograde Lesson 8 assignment """

from pathlib import Path
from os import remove
from csv import reader
from pytest import fixture
from src.inventory import inventory as l


@fixture
def _customers_to_add():
    return [
        ["Elisa Miles", "LR04", "Leather Sofa", "25.00"],
        ["Edward Data", "KT78", "Kitchen Table", "10.00"],
        ["Alex Gonzales", "BR02", "Queen Mattress", "17.00"],

        ["Kyouma Hououin", "FG04", "Moad Snake", "1200.00"],
        ["Hashida Itaru", "FG204", "2nd Edition Ver. 2.31", "00.00"],
        ["Christina", "FG88", "Replicator", "800.00"]   
    ]


@fixture
def _full_invoice():
    return [
        ["Elisa Miles", "LR04", "Leather Sofa", "25.00"],
        ["Edward Data", "KT78", "Kitchen Table", "10.00"],
        ["Alex Gonzales", "BR02", "Queen Mattress", "17.00"],
        ["Kyouma Hououin", "FG04", "Moad Snake", "1200.00"],
        ["Hashida Itaru", "FG204", "2nd Edition Ver. 2.31", "00.00"],
        ["Christina", "FG88", "Replicator", "800.00"],
        ["Kyouma Hououin", "FG06", "Cyalume Saber", "7.50"],
        [
            "Kyouma Hououin",
            "FG07",
            "Active-Shell Optical Camouflage Ball",
            "12.50",
        ],
        ["Kyouma Hououin", "FG08", "Phonewave", "1000.00"],
        ["Kyouma Hououin", "FG204", "Time Machine", "0.00"]
    ]


@fixture
def _customer_search_christina():
    return [["Christina", "FG88", "Replicator", "800.00"]]


def test_add_furniture_write(_customers_to_add):
    """ Tests that add furniture new file writing works """

    test_invoice = "../data/test-invoice.csv"
    csv_contents = []

    if Path(test_invoice).exists():
        remove(test_invoice)

    for customer in _customers_to_add:
        l.add_furniture(
            test_invoice, customer[0], customer[1], customer[2], customer[3]
        )

    with open(test_invoice, "r") as csv_file:
        contents = reader(csv_file, delimiter=',')
        for line in contents:
            if line != []:
                csv_contents += [line]

        csv_contents += contents

    assert _customers_to_add == csv_contents


def test_add_furniture_append(_customers_to_add):
    """ Tests that add furniture append file writing works """

    test_invoice = "../data/test-invoice.csv"
    csv_contents = []

    if Path(test_invoice).exists():
        remove(test_invoice)

    if not Path(test_invoice).exists():
        open(test_invoice, "a").close()

    for customer in _customers_to_add:
        l.add_furniture(
            test_invoice, customer[0], customer[1], customer[2], customer[3]
        )

    with open(test_invoice, "r") as csv_file:
        contents = reader(csv_file, delimiter=',')
        for line in contents:
            if line != []:
                csv_contents += [line]

        csv_contents += contents

    assert _customers_to_add == csv_contents


def test_single_customer(_full_invoice):
    """ Tests single customer closure is working """

    test_invoice = "../data/test-invoice.csv"
    items_to_insert = "../data/items.csv"
    csv_contents = []

    function = l.single_customer("Kyouma Hououin", test_invoice)
    function(items_to_insert)

    with open(test_invoice, "r") as csv_file:
        contents = reader(csv_file, delimiter=',')
        for line in contents:
            if line != []:
                csv_contents += [line]

        csv_contents += contents

    assert _full_invoice == csv_contents


def test_customer_search(_customers_to_add, _customer_search_christina):
    """ Tests that customer serach is working"""

    test_invoice = "../data/test-invoice.csv"
    csv_contents = []

    if Path(test_invoice).exists():
        remove(test_invoice)

    for customer in _customers_to_add:
        l.add_furniture(
            test_invoice, customer[0], customer[1], customer[2], customer[3]
        )

    func = l.single_customer_search("Christina", test_invoice)
    assert func("FG88") == _customer_search_christina
    assert func("FG204") == "Nothing Found"
