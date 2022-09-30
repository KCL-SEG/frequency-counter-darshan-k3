"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    #e.g. items = [a,b,a,a,a,a,b,a]
    frequencies = {}
    for item in items:
        if(frequencies.get(item) == None):
            frequencies[str(item)] = 1
        else:
            frequencies[str(item)] = frequencies.get(item) + 1
    return frequencies
