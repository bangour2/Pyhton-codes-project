__author__ = 'mohammad'

mem = {}


def fetch (var):
    return mem[var.ch]

def store (var, value):
    mem[var.ch] = value
