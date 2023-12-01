"""
file: reg_exp_class.py
author: Matthew Morrison msm8275

contains class structure for a regular expression
"""

from dataclasses import dataclass


@dataclass
class RegularExpression:
    """
    class that explains general information about regular expressions
    used to create NFAs
    """
    reg_exp_symbols = ['+', '*', '.'] # only operators possible for the reg exp
    special_chars = ["\u03B5, \u03A6"]  # epsilon and phi (empty set)
    alphabet: list[str]
    expression = str

    def init(self, alphabet, expression):
        self.alphabet = alphabet
        self.expression = expression
