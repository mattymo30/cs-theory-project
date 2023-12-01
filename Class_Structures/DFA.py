"""
file: DFA.py
author: Matthew Morrison msm8275

DFA.py contains the class structure for a deterministic finite automaton
"""

import finite_automata_class as fa


def new_dfa(states, start_state, accept_states, transitions, alphabet):
    """
    Initialize a new DFA
    :param states: a set of states that the DFA will have
    :param start_state: the start state of the DFA
    :param accept_states: a set of states that accept a string in the DFA
    :param transitions: the transitions of the DFA
    :param alphabet: the alphabet of the DFA
    :return: the newly created DFA
    """
    dfa = fa.FiniteAutomaton(accept_states=accept_states, states=states,
                             start_state=start_state, alphabet=alphabet)
    dfa.transitions = transitions
    return dfa


def single_transition(dfa, state, input_char):
    """
    Helper function for the recursive transition definition of a DFA
    :param state: the state in the DFA to check
    :param input_char: the input char to be tested against the DFA
    :param dfa:  DFA object
    """
    return dfa.transitions.get(state).get(input_char)


def recursive_transition(dfa, state, input_string):
    """
    Using the recursive definition for DFA, compute the set of states that
    a given input can arrive to in the DFA and check against the DFAs
    accepting states to determine if the string is accepted
    :param dfa: the DFA object
    :param state: the current state in the DFA
    :param input_string: the input string to be tested against the DFA
    """

    if input_string == "":
        return state
    else:
        return single_transition(dfa,
                                 recursive_transition(
                                     dfa, state, input_string[0:-1]),
                                 input_string[-1])


def is_string_accepted(dfa, input_string):
    """
    Test if a given string is accepted in a DFA machine with the recursive
    transition definition of a DFA

    :param dfa: the DFA object
    :param input_string: the input string to be tested against the DFA
    :return if the string was accepted or not
    """
    final_state = recursive_transition(dfa.start_state, input_string, dfa)

    if final_state == dfa.final_state:
        return True

    return False
