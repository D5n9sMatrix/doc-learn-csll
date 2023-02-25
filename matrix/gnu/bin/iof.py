#!-*- coding: utf-8 -*-
"""Python doc learn csll"""
import copyreg
import pickle
from pickle import Pickler
from typing import Type

from poetry.console import io

f = io
p: Type[Pickler] = pickle.Pickler



class SomeClass:
    pass


