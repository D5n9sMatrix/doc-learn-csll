#!-*- coding: utf-8 -*-
"""Python doc learn csll"""
import copyreg
import pickle

from poetry.console import io

from matrix.gnu.bin.iof import SomeClass, p


class MyPickler(pickle.Pickler):
    dispatch_table = copyreg.dispatch_table.copy()


f = io.__file__
f.title()