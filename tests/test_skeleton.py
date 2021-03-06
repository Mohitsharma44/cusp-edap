#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from cusp_edap.skeleton import fib
from cusp_edap.skeleton import main

__author__ = "Mohit Sharma"
__copyright__ = "Mohit Sharma"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
    assert main(["7"]) == 13
