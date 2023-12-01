"""
file: reg_exp_to_NFA_test.py
author: Matthew Morrison msm8275

Contains several test implementations of regular expressions and
converting those tests into Non-Deterministic Finite Automaton machines
"""
from reg_exp_to_NFA import construct_nfa


def test_1():
    reg_exp_1 = "\u03A6"
    reg_exp_1_alp = ["a", "b"]

    print("Regular Expression 1: " + reg_exp_1)
    nfa = construct_nfa(reg_exp_1, reg_exp_1_alp)

    print("NFA 1: ")
    print("States: ")
    print(nfa.states)
    print("Start State: " + nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")
    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_2():
    reg_exp_2 = "\u03B5"
    reg_exp_2_alp = ["a", "b"]

    print("Regular Expression 2: " + reg_exp_2)
    nfa = construct_nfa(reg_exp_2, reg_exp_2_alp)

    print("NFA 2: ")
    print("States: ")
    print(nfa.states)
    print("Start State: " + nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")
    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_3():
    reg_exp_3 = "a"
    reg_exp_3_alp = ["a", "b"]

    print("Regular Expression 3: " + reg_exp_3)
    nfa = construct_nfa(reg_exp_3, reg_exp_3_alp)

    print("NFA 3: ")
    print("States: ")
    print(nfa.states)
    print("Start State: " + nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")
    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_4():
    reg_exp_4 = "a+b"
    reg_exp_4_alp = ["a", "b"]

    print("Regular Expression 4: " + reg_exp_4)
    nfa = construct_nfa(reg_exp_4, reg_exp_4_alp)

    print("NFA 4: ")
    print("States: ")
    print(nfa.states)
    print("Start State: ")
    print(nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")
    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_5():
    reg_exp_5 = "a.b"
    reg_exp_5_alp = ["a", "b"]

    print("Regular Expression 5: " + reg_exp_5)
    nfa = construct_nfa(reg_exp_5, reg_exp_5_alp)

    print("NFA 5: ")
    print("States: ")
    print(nfa.states)
    print("Start State: ")
    print(nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")
    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_6():
    reg_exp_6 = "a*"
    reg_exp_6_alp = ["a", "b"]

    print("Regular Expression 6: " + reg_exp_6)
    nfa = construct_nfa(reg_exp_6, reg_exp_6_alp)

    print("NFA 6: ")
    print("States: ")
    print(nfa.states)
    print("Start State: ")
    print(nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")
    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_7():
    reg_exp_7 = "a+b*"
    reg_exp_7_alp = ["a", "b"]

    print("Regular Expression 7: " + reg_exp_7)
    nfa = construct_nfa(reg_exp_7, reg_exp_7_alp)

    print("NFA 7: ")
    print("States: ")
    print(nfa.states)
    print("Start State: ")
    print(nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")
    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_8():
    reg_exp_8 = "(a+b)*"
    reg_exp_8_alp = ["a", "b"]

    print("Regular Expression 8: " + reg_exp_8)
    nfa = construct_nfa(reg_exp_8, reg_exp_8_alp)

    print("NFA 8: ")
    print("States: ")
    print(nfa.states)
    print("Start State: ")
    print(nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")

    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_9():
    reg_exp_9 = "(a+b*).a*"
    reg_exp_9_alp = ["a", "b"]

    print("Regular Expression 9: " + reg_exp_9)
    nfa = construct_nfa(reg_exp_9, reg_exp_9_alp)

    print("NFA 9: ")
    print("States: ")
    print(nfa.states)
    print("Start State: ")
    print(nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")

    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


def test_10():
    reg_exp_10 = "((a+b*).a*)*"
    reg_exp_10_alp = ["a", "b"]

    print("Regular Expression 10: " + reg_exp_10)
    nfa = construct_nfa(reg_exp_10, reg_exp_10_alp)

    print("NFA 10: ")
    print("States: ")
    print(nfa.states)
    print("Start State: ")
    print(nfa.start_state)
    print("Alphabet: ")
    print(nfa.alphabet)
    print("Accept States: ")
    print(nfa.accept_states)
    print("Transitions: ")

    for key in nfa.transitions:
        print("{}: {}".format(key, nfa.transitions[key]))

    nfa.re_to_nfa_build_graph()


if __name__ == "__main__":
    test_10()
