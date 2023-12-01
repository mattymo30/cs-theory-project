"""
file: CFG_to_PDA_test.py
author: Matthew Morrison msm8275

Contains several test implementations of Context-Free Grammars and
converting them to equivalent Pushdown Automaton Machines
"""

from CFG_to_PDA import pda_from_cfg
from Class_Structures.CFG_class import CFG


def test_1():
    print("Test 1")

    variables1 = set()
    variables1.add("S")
    variables1.add("T")

    alphabet1 = ["a", "b"]

    productions1 = set()
    productions1.add(("S", "aTb"))
    productions1.add(("S", "b"))
    productions1.add(("T", "Ta"))
    productions1.add(("T", "epsilon"))

    start_var1 = "S"

    cfg1 = CFG
    cfg1.alphabet = alphabet1
    cfg1.start_var = start_var1
    cfg1.variables = variables1
    cfg1.productions = productions1

    print("CFG 1")
    print("Variables: " + str(cfg1.variables))
    print("Alphabet: " + str(cfg1.alphabet))
    print("Productions: ")
    for production in cfg1.productions:
        print(str(production))
    print("Start Variable: " + cfg1.start_var)

    pda = pda_from_cfg(cfg1)

    print("Equivalent PDA")
    print("States: " + str(pda.states))
    print("Start State: " + pda.start_state)
    print("Accept States: " + str(pda.accept_states))
    print("Input Tape Alphabet: " + str(pda.input_tape_alphabet))
    print("Stack Alphabet: " + str(pda.stack_alphabet))
    print("Transitions:")
    for transitions in pda.transitions:
        output = pda.transitions[transitions]
        print(str(transitions) + " -> " + str(output))

    pda.build_graph()


def test_2():
    print("Test 2")

    variables = set()
    variables.add("S")
    variables.add("T")
    variables.add("U")

    alphabet = ["a", "b", "c"]

    productions = set()
    productions.add(("S", "TU"))
    productions.add(("S", "epsilon"))
    productions.add(("T", "aTb"))
    productions.add(("T", "epsilon"))
    productions.add(("U", "bUc"))
    productions.add(("U", "epsilon"))

    start_var = "S"

    cfg = CFG
    cfg.alphabet = alphabet
    cfg.start_var = start_var
    cfg.variables = variables
    cfg.productions = productions

    print("CFG 1")
    print("Variables: " + str(cfg.variables))
    print("Alphabet: " + str(cfg.alphabet))
    print("Productions: ")
    for production in cfg.productions:
        print(str(production))
    print("Start Variable: " + cfg.start_var)

    pda = pda_from_cfg(cfg)

    print("Equivalent PDA")
    print("States: " + str(pda.states))
    print("Start State: " + pda.start_state)
    print("Accept States: " + str(pda.accept_states))
    print("Input Tape Alphabet: " + str(pda.input_tape_alphabet))
    print("Stack Alphabet: " + str(pda.stack_alphabet))
    print("Transitions:")
    for transitions in pda.transitions:
        output = pda.transitions[transitions]
        print(str(transitions) + " -> " + str(output))

    pda.build_graph()


def test_3():
    print("Test 3")

    variables = set()
    variables.add("S")
    variables.add("T")
    variables.add("U")
    variables.add("V")

    alphabet = ["a", "b", "c"]

    productions = set()
    productions.add(("S", "T"))
    productions.add(("S", "U"))
    productions.add(("T", "abT"))
    productions.add(("T", "epsilon"))
    productions.add(("U", "bcV"))
    productions.add(("V", "epsilon"))
    productions.add(("V", "acV"))

    start_var = "S"

    cfg = CFG
    cfg.alphabet = alphabet
    cfg.start_var = start_var
    cfg.variables = variables
    cfg.productions = productions

    print("CFG 1")
    print("Variables: " + str(cfg.variables))
    print("Alphabet: " + str(cfg.alphabet))
    print("Productions: ")
    for production in cfg.productions:
        print(str(production))
    print("Start Variable: " + cfg.start_var)

    pda = pda_from_cfg(cfg)

    print("Equivalent PDA")
    print("States: " + str(pda.states))
    print("Start State: " + pda.start_state)
    print("Accept States: " + str(pda.accept_states))
    print("Input Tape Alphabet: " + str(pda.input_tape_alphabet))
    print("Stack Alphabet: " + str(pda.stack_alphabet))
    print("Transitions:")
    for transitions in pda.transitions:
        output = pda.transitions[transitions]
        print(str(transitions) + " -> " + str(output))

    pda.build_graph()


def test_4():
    print("Test 4")

    variables = set()
    variables.add("S")
    variables.add("T")
    variables.add("U")
    variables.add("V")
    variables.add("W")

    alphabet = ["a", "b", "c"]

    productions = set()
    productions.add(("S", "TbU"))
    productions.add(("S", "aV"))
    productions.add(("T", "aTb"))
    productions.add(("T", "epsilon"))
    productions.add(("U", "bU"))
    productions.add(("U", "Uc"))
    productions.add(("U", "epsilon"))
    productions.add(("V", "epsilon"))
    productions.add(("V", "aVc"))
    productions.add(("V", "aV"))
    productions.add(("V", "W"))
    productions.add(("W", "epsilon"))
    productions.add(("W", "bW"))

    start_var = "S"

    cfg = CFG
    cfg.alphabet = alphabet
    cfg.start_var = start_var
    cfg.variables = variables
    cfg.productions = productions

    print("CFG 1")
    print("Variables: " + str(cfg.variables))
    print("Alphabet: " + str(cfg.alphabet))
    print("Productions: ")
    for production in cfg.productions:
        print(str(production))
    print("Start Variable: " + cfg.start_var)

    pda = pda_from_cfg(cfg)

    print("Equivalent PDA")
    print("States: " + str(pda.states))
    print("Start State: " + pda.start_state)
    print("Accept States: " + str(pda.accept_states))
    print("Input Tape Alphabet: " + str(pda.input_tape_alphabet))
    print("Stack Alphabet: " + str(pda.stack_alphabet))
    print("Transitions:")
    for transitions in pda.transitions:
        output = pda.transitions[transitions]
        print(str(transitions) + " -> " + str(output))

    pda.build_graph()


if __name__ == "__main__":
    test_4()
