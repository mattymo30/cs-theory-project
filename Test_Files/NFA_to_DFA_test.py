"""
file: NFA_to_DFA_test.py
author: Matthew Morrison msm8275

Contains several test implementations of Non-Deterministic Finite Automaton
Machines and converts them to equivalent Deterministic Fintie Automaton
Machines
"""

from Class_Structures import NFA
from NFA_to_DFA import power_set_construction


def test_1():
    print("Test 1:")
    print("NFA:")

    states = set()
    states.add("1")
    states.add("2")
    states.add("3")
    alphabet = ["a", "b"]
    accept_states = set()
    accept_states.add("1")
    start_state = set()
    start_state.add("1")

    transitions = dict()
    transitions["1"] = {}
    transitions["2"] = {}
    transitions["3"] = {}

    transitions["1"]["epsilon"] = {"2"}
    transitions["2"]["epsilon"] = {}
    transitions["3"]["epsilon"] = {}
    transitions["1"]["a"] = {"1"}
    transitions["2"]["a"] = {"2"}
    transitions["3"]["a"] = {"1"}
    transitions["1"]["b"] = {"2"}
    transitions["2"]["b"] = {"3"}
    transitions["3"]["b"] = {}

    nfa = NFA.new_nfa(states, start_state, accept_states, transitions, alphabet)
    print(nfa.states)
    print(nfa.start_state)
    print(nfa.alphabet)
    print(nfa.accept_states)
    print(nfa.transitions)

    dfa = power_set_construction(nfa)

    print("Equivalent DFA:")

    print(dfa.states)
    print(dfa.start_state)
    print(dfa.alphabet)
    print(dfa.accept_states)
    print(dfa.transitions)

    dfa.build_graph()


def test_2():
    print("Test 2:")
    print("NFA:")

    states = set()
    states.add("q0")
    states.add("q1")
    states.add("q2")
    alphabet = ["0", "1"]
    accept_states = set()
    accept_states.add("q2")
    start_state = set()
    start_state.add("q0")

    transitions = dict()
    transitions["q0"] = {}
    transitions["q1"] = {}
    transitions["q2"] = {}

    transitions["q0"]["epsilon"] = {}
    transitions["q1"]["epsilon"] = {}
    transitions["q2"]["epsilon"] = {}
    transitions["q0"]["0"] = {"q0", "q1"}
    transitions["q1"]["0"] = {}
    transitions["q2"]["0"] = {"q2"}
    transitions["q0"]["1"] = {"q0"}
    transitions["q1"]["1"] = {"q2"}
    transitions["q2"]["1"] = {"q2"}

    nfa = NFA.new_nfa(states, start_state, accept_states, transitions, alphabet)
    print(nfa.states)
    print(nfa.start_state)
    print(nfa.alphabet)
    print(nfa.accept_states)
    print(nfa.transitions)

    dfa = power_set_construction(nfa)

    print("Equivalent DFA:")

    print(dfa.states)
    print(dfa.start_state)
    print(dfa.alphabet)
    print(dfa.accept_states)
    print(dfa.transitions)

    dfa.build_graph()


def test_3():
    print("Test 3:")
    print("NFA:")

    states = set()
    states.add("q0")
    states.add("q1")
    states.add("q2")
    states.add("q3")
    states.add("q4")
    alphabet = ["0", "1"]
    accept_states = set()
    accept_states.add("q4")
    start_state = set()
    start_state.add("q0")

    transitions = dict()
    transitions["q0"] = {}
    transitions["q1"] = {}
    transitions["q2"] = {}
    transitions["q3"] = {}
    transitions["q4"] = {}

    transitions["q0"]["epsilon"] = {}
    transitions["q1"]["epsilon"] = {"q2"}
    transitions["q2"]["epsilon"] = {}
    transitions["q3"]["epsilon"] = {"q4"}
    transitions["q4"]["epsilon"] = {}
    transitions["q0"]["0"] = {"q1"}
    transitions["q1"]["0"] = {"q1"}
    transitions["q2"]["0"] = {"q3"}
    transitions["q3"]["0"] = {"q3"}
    transitions["q4"]["0"] = {}

    transitions["q0"]["1"] = {}
    transitions["q1"]["1"] = {}
    transitions["q2"]["1"] = {"q2", "q3"}
    transitions["q3"]["1"] = {"q1"}
    transitions["q4"]["1"] = {}

    nfa = NFA.new_nfa(states, start_state, accept_states, transitions, alphabet)
    print(nfa.states)
    print(nfa.start_state)
    print(nfa.alphabet)
    print(nfa.accept_states)
    print(nfa.transitions)

    dfa = power_set_construction(nfa)

    print("Equivalent DFA:")

    print(dfa.states)
    print(dfa.start_state)
    print(dfa.alphabet)
    print(dfa.accept_states)
    print(dfa.transitions)

    dfa.build_graph()


if __name__ == "__main__":
    test_3()
    