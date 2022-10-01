"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    #e.g. items = [a,b,a,a,a,a,b,a]
    frequencies = {}
    for item in items:
        stringItem = str(item)
        if(frequencies.get(stringItem) == None):
            frequencies[stringItem] = 1
        else:
            frequencies[stringItem] = frequencies.get(stringItem) + 1
    return frequencies
