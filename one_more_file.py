#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Этот модуль реализует простую процедуру приветствия"""

__author__ = "Дмитрий Г."

def hello(name=None):
    if name:
        print("Добрый день, {}!".format(name))
    else:
        print("Добрый день!")

if __name__ == '__main__':
    hello("Палел")
