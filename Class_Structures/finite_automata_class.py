"""
file: finite_automata_class.py
author: Matthew Morrison msm8275

contains class structure for the two finite automata machines:
DFAs and NFAs
"""

from dataclasses import dataclass
from graphviz import Digraph


@dataclass
class FiniteAutomaton:
    """General class that contains the structure of
    finite automata (DFAs and NFAs"""
    states: set
    start_state: set
    accept_states: set
    transitions = dict
    alphabet: list[str]
    graph = Digraph

    def init(self, states, start_state, accept_states, transitions, alphabet):
        """
        initialize the finite automaton class
        :param states: the set of states
        :param start_state: the start state
        :param accept_states: the set of accepts states
        :param transitions: the transitions of the FA
        :param alphabet: the alphabet of the FA
        """
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.transitions = transitions
        self.start_state = start_state
        self.states = states

    def build_graph(self):
        """
        Build a graph from NFA_to_DFA program
        """
        self.graph = Digraph()
        self.graph.attr(rankdir='LR')

        for state in self.states:
            if state not in self.accept_states:
                self.graph.attr('node', shape='circle')
                self.graph.node(state)

            else:
                self.graph.attr('node', shape='doublecircle')
                self.graph.node(state)
        start_state = str(self.start_state)

        self.graph.node('invisible_start', shape='point', width='0.1', style='invis')
        self.graph.edge('invisible_start', start_state, arrowhead='normal')

        for state in self.transitions:
            for letter in self.transitions[state]:
                go_to_state = str(self.transitions[state][letter])
                label = letter
                if label == "epsilon":
                    label = 'ε'
                if go_to_state != '':
                    self.graph.edge(state, go_to_state, label=label)

        # Makes a pdf with name nfa.graph.pdf and views the pdf
        self.graph.render('nfa', view=True)

    def re_to_nfa_build_graph(self):
        """
        Build the graph for the reg_exp_to_NFA program
        """
        self.graph = Digraph()
        self.graph.attr(rankdir='LR')

        for state in self.states:
            if state not in self.accept_states:
                self.graph.attr('node', shape='circle')
                self.graph.node(state)

            else:
                self.graph.attr('node', shape='doublecircle')
                self.graph.node(state)
        start_state = str(self.start_state)

        self.graph.node('invisible_start', shape='point', width='0.1', style='invis')
        self.graph.edge('invisible_start', start_state, arrowhead='normal')

        for state in self.transitions:
            for letter in self.transitions[state]:
                label = letter
                if label == "epsilon":
                    label = 'ε'
                transitions = self.transitions[state][letter]
                if transitions:
                    for single_state in transitions:
                        self.graph.edge(state, single_state, label=label)

        # Makes a pdf with name nfa.graph.pdf and views the pdf
        self.graph.render('nfa', view=True)
