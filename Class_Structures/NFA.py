"""
file: NFA.py
author: Matthew Morrison msm8275

NFA.py contains the class structure for a non-deterministic finite
automata machine
"""

from Class_Structures import finite_automata_class as fa


def new_nfa(nfa_states, nfa_ss, nfa_as, nfa_transitions, nfa_alph):
    """
    Initialize a new NFA
    :param nfa_states: a set of states that the NFA will have
    :param nfa_ss: the start state of the NFA
    :param nfa_as: a set of states that accept a string in the NFA
    :param nfa_transitions: the transitions of the NFA
    :param nfa_alph: the alphabet of the NFA
    :return: the newly created NFA
    """
    built_nfa = fa.FiniteAutomaton(accept_states=nfa_as, states=nfa_states,
                                   start_state=nfa_ss, alphabet=nfa_alph)
    built_nfa.transitions = nfa_transitions
    return built_nfa


def epsilon_closure(curr_nfa, curr_states):
    """
    obtain a set of transitions that are through an epsilon closure
    :param curr_nfa: the current NFA
    :param curr_states: the current set of states to check for epsilon trans
    :return: a set of transitions from the nfa
    """
    transition_set = set()
    for state in curr_states:
        transition_set.add(state)
    for state in curr_states:
        transition = curr_nfa.transitions.get(state).get("epsilon")
        if transition != "":
            for trans_state in transition:
                transition_set.add(trans_state)

    return transition_set


def single_transition(curr_nfa, state, input_char):
    """
    get a single transition and the state traveled to in the NFA
    :param curr_nfa: the current NFA
    :param state: the current state to check
    :param input_char: the character that is inputted in the state and NFA
    :return: the state that the NFA transitions to with the input
    """
    return curr_nfa.transitions.get(state).get(input_char)


def recursive_transition(curr_nfa, state, input_string):
    """
    Using the recursive definition for NFA, compute the set of states that
    a given input can arrive to in the NFA and check against the NFAs
    accepting states to determine if the string is accepted
    :param curr_nfa: the NFA object
    :param state: the start state or set of states in the current iteration
    :param input_string: the input string to be tested against the NFA
    """

    if input_string == "":
        curr_states = epsilon_closure(curr_nfa, state)

        if len(curr_states) == 0:
            return {}
        else:
            return curr_states
    else:
        # get states for union transition in recursive call
        union_states = recursive_transition(curr_nfa, state, input_string[0:-1])

        final_states = set()
        # get every single transition with all the states found
        for state in union_states:
            final_states.add(single_transition(curr_nfa, state, input_string[-1]))

        # get all the states epsilon-closures and return it
        e_closure_states = epsilon_closure(curr_nfa, final_states)

        return e_closure_states


def is_string_accepted(curr_nfa, state, input_string):
    """
    Test if a given string is accepted in a NFA machine with the recursive
    transition definition of a NFA

    :param state: the start state of the nfa
    :param curr_nfa: the current NFA
    :param input_string: the input string to be tested against the NFA
    :return if the string was accepted or not
    """
    final_states = recursive_transition(curr_nfa, state, input_string)

    for curr_state in final_states:
        if curr_state == curr_nfa.final_state:
            return True

    return False


if __name__ == "__main__":
    states = set()
    states.add("1")
    states.add("2")
    alphabet = ["a", "b"]
    accept_states = set()
    accept_states.add("1")
    start_state = set()
    start_state.add("1")

    transitions = dict()
    transitions["1"] = {}
    transitions["2"] = {}

    transitions["1"]["epsilon"] = ""
    transitions["2"]["epsilon"] = ""
    transitions["1"]["a"] = "1"
    transitions["2"]["a"] = "2"
    transitions["1"]["b"] = "2"
    transitions["2"]["b"] = "1"

    nfa = new_nfa(states, start_state, accept_states, transitions, alphabet)
    print(nfa.states)
    print(nfa.start_state)
    print(nfa.alphabet)
    print(nfa.accept_states)
    print(nfa.transitions)

    print(recursive_transition(nfa, nfa.start_state, ""))
    print(recursive_transition(nfa, nfa.start_state, "a"))
    print(recursive_transition(nfa, nfa.start_state, "b"))
    print(recursive_transition(nfa, nfa.start_state, "abb"))

    print("\n")

    states2 = set()
    states2.add("1")
    states2.add("2")
    states2.add("3")
    alphabet2 = ["a", "b"]
    accept_states2 = set()
    accept_states2.add("1")
    start_state2 = set()
    start_state2.add("1")

    transitions2 = dict()
    transitions2["1"] = {}
    transitions2["2"] = {}
    transitions2["3"] = {}

    transitions2["1"]["epsilon"] = ""
    transitions2["2"]["epsilon"] = ""
    transitions2["3"]["epsilon"] = ""
    transitions2["1"]["a"] = "1"
    transitions2["2"]["a"] = "2"
    transitions2["3"]["a"] = "3"
    transitions2["1"]["b"] = "2"
    transitions2["2"]["b"] = "3"
    transitions2["3"]["b"] = "1"

    nfa2 = new_nfa(states2, start_state2, accept_states2, transitions2, alphabet2)
    print(nfa2.states)
    print(nfa2.start_state)
    print(nfa2.alphabet)
    print(nfa2.accept_states)
    print(nfa2.transitions)

    print(recursive_transition(nfa2, nfa2.start_state, ""))
    print(recursive_transition(nfa2, nfa2.start_state, "a"))
    print(recursive_transition(nfa2, nfa2.start_state, "b"))

    nfa2.build_graph()

