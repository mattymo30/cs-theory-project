"""
file: CFG_class.py
author: Matthew Morrison msm8275

Contains the class structure and relatable operator functions for a
Context-Free Grammar (CFG)
"""

from dataclasses import dataclass


@dataclass
class CFG:
    """General class that contains the structure of
    a context free grammar

    variables: a set of states that the CFG can traverse through
    alphabet: the list of symbols accepted in the CFG
    productions: a set of 2-tuples of what each variable in the CFG
    can produce
    start_var: the start variable of the string, where all strings will
    begin productions

    """
    variables = set
    alphabet = list[str]
    productions = set
    start_var = str

    def init(self, variables, alphabet, productions, start_var):
        self.variables = variables
        self.alphabet = alphabet
        self.productions = productions
        self.start_var = start_var


def union(cfg1, cfg2):
    """
    perform a union operator on two provided context-free grammars
    :param cfg1: the first cfg
    :param cfg2: the second cfg
    :return: an updated unionized cfg
    """
    cfg = CFG()

    start_var_1 = cfg1.start_var
    start_var_2 = cfg2.start_var

    vars_1 = cfg1.variables
    vars_2 = cfg2.variables

    union_vars = set()
    union_vars.union(vars_1, vars_2)

    alphabet_1 = cfg1.alphabet
    alphabet_2 = cfg2.alphabet

    union_alphabet = list()

    for symbol in alphabet_1:
        union_alphabet.append(symbol)
    for symbol in alphabet_2:
        union_alphabet.append(symbol)

    productions_1 = cfg1.productions
    productions_2 = cfg2.productions

    union_productions = set()
    union_productions.union(productions_1, productions_2)

    start_state = "U"

    union_productions.add((start_state, start_var_1))
    union_productions.add((start_state, start_var_2))

    cfg.variables = union_vars
    cfg.alphabet = union_alphabet
    cfg.productions = union_productions
    cfg.start_var = start_state

    return cfg


def concat(cfg1, cfg2):
    """
    perform a concatenation operator on two provided context-free grammars
    :param cfg1: the first cfg
    :param cfg2: the second cfg
    :return: an updated concatenated cfg
    """
    cfg = CFG()

    start_var_1 = cfg1.start_var
    start_var_2 = cfg2.start_var

    vars_1 = cfg1.variables
    vars_2 = cfg2.variables

    concat_vars = set()
    concat_vars.union(vars_1, vars_2)

    alphabet_1 = cfg1.alphabet
    alphabet_2 = cfg2.alphabet

    concat_alphabet = list()

    for symbol in alphabet_1:
        concat_alphabet.append(symbol)
    for symbol in alphabet_2:
        concat_alphabet.append(symbol)

    productions_1 = cfg1.productions
    productions_2 = cfg2.productions

    concat_prods = set()
    concat_prods.union(productions_1, productions_2)

    start_state = "C"

    concat_prods.add((start_state, "%s%s" % (start_var_1, start_var_2)))

    cfg.variables = concat_vars
    cfg.alphabet = concat_alphabet
    cfg.productions = concat_prods
    cfg.start_var = start_state

    return cfg


def kleene_star(cfg):
    """
    perform a Kleene Star operation on a provided cfg
    :param cfg: the cfg to perform the operation on
    """
    old_start_state = cfg.start_var

    new_start_state = "K"
    cfg.variables.add(new_start_state)
    cfg.start_var = new_start_state

    cfg.productions.add((new_start_state, "%s%s" % (old_start_state, new_start_state)))
    cfg.productions.add((new_start_state, "\u03B5"))


