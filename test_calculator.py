# test_calculator.py

import sys
import os

import calc

def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(5, 2) == 3

def test_add():
    assert calc.add(7, 8) == 15
