"""
file: NFA_to_DFA.py
author: Matthew Morrison msm8275

main file that converts a provided Non-Deterministic Finite Automata
and turns it into an equivalent Deterministic Finite Automata machine
"""

import ast

from Class_Structures import finite_automata_class as fa, NFA


def build_empty_dfa(start_state, alphabet):
    """
    build an empty DFA that will hold the new object after power set
    construction
    :return:  a new instance of the FiniteAutomaton object class
    """
    dfa = fa.FiniteAutomaton(states=set(), start_state=start_state,
                             accept_states=set(), alphabet=alphabet)
    dfa.transitions = {}
    return dfa


def build_new_dfa(states, start_state, accept_states, transitions, alphabet):
    """
    after completing the power set construction for the DFA, add the new
    elements to it
    :param states: the new states of the DFA
    :param accept_states: the new accept states of the DFA
    :param transitions: the new transitions of the DFA
    :return: updated dfa with the new states, accept_states, and transitions
    """

    dfa = fa.FiniteAutomaton(accept_states=accept_states, states=states,
                             start_state=start_state, alphabet=alphabet)
    dfa.transitions = transitions
    return dfa


def initialize_power_set(nfa):
    """
    Initialize the new power set DFA with known information
    from the NFA: the start state and its alphabet
    :param nfa: the NFA object
    """
    start_state = set()
    for state in nfa.start_state:
        start_state.add(state)

    e_closure_states = NFA.epsilon_closure(nfa, nfa.start_state)
    for state in e_closure_states:
        start_state.add(state)

    new_dfa = build_empty_dfa(start_state, nfa.alphabet)
    new_dfa.states.add(str(start_state))

    return new_dfa


def get_transitions(nfa, states, letter):
    """
    obtain a set of all transitions at a given set of states
    and an nfa with transition information
    :param nfa: the nfa with the required information
    :param states: the current set of states
    :param letter: the letter to find transitions for
    :return: a set of transitions that occur with the letter
    """
    transitions = set()

    # first check for any epsilon closures with the states
    start_state_transitions = NFA.epsilon_closure(nfa, states)

    transitions.add(start_state_transitions)

    # check where each state transitions to with the letter
    for state in transitions:
        transition = NFA.single_transition(nfa, state, letter)
        transitions.add(transition)

    return transitions


def get_accepting_states(nfa, new_dfa):
    """
    get every accepting state from the new states for the DFA
    :param nfa: the NFA to check what states are accepted
    :param new_dfa: the new_dfa to add accepting states to
    :return:
    """
    accepting_states = set()
    states = []

    for str_state in new_dfa.states:
        str_state = set(ast.literal_eval(str_state))
        states.append(str_state)

    for curr_state in states:
        for single_state in curr_state:
            if single_state in nfa.accept_states:
                accepting_states.add(str(curr_state))
                break

    return accepting_states


def power_set_recursion(nfa, state, new_dfa, sets_visited):
    """
    recursively build up a new dfa, provided with information
    of an nfa
    :param nfa: the nfa to obtain information from
    :param state: the current state(s) the search from
    :param new_dfa: the new dfa to be build
    :param sets_visited: a list of all previous sets of states visited
    """
    state_string = str(state)
    new_dfa.transitions[state_string] = {}

    # hold the actual sets created
    transitions_made = []

    if state == {"\u03A6"}:
        for symbol in new_dfa.alphabet:
            new_dfa.transitions[state_string][symbol] = {"\u03A6"}
    else:
        for symbol in new_dfa.alphabet:
            transition = set()
            for single_state in state:
                this_trans = NFA.single_transition(nfa, single_state, symbol)

                if this_trans != "":
                    for trans_state in this_trans:
                        transition.add(trans_state)
            transition = NFA.epsilon_closure(nfa, transition)
            # if no transitions occur, symbol moves to empty set
            if not transition:
                transition = {"\u03A6"}
            new_dfa.transitions[state_string][symbol] = transition
            transitions_made.append(transition)

        # keep track of all states already visited with this function
        sets_visited.append(state)

    # for every new transition found, check if it is already in the new dfa
    # transition keys
    for transition_set in transitions_made:
        already_visited = False
        for sets in sets_visited:
            if transition_set == sets:
                already_visited = True
                break
        if not already_visited:
            new_dfa.states.add(str(transition_set))
            power_set_recursion(nfa, transition_set, new_dfa, sets_visited)


def power_set_construction(nfa):
    """
    recursive definition of power set construction to build a DFA from
    an NFA
    :param nfa: the original NFA
    :return: a newly constructed DFA
    """
    # initialize the new DFA
    new_dfa = initialize_power_set(nfa)

    sets_visited = []

    # construct the new transition table using power set construction
    power_set_recursion(nfa, new_dfa.start_state, new_dfa, sets_visited)

    # get all the accepting states in the new_dfa
    accepting_states = get_accepting_states(nfa, new_dfa)
    new_dfa.accept_states = accepting_states

    return new_dfa
