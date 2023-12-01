"""
file: PDA_class.py
author: Matthew Morrison msm8275

Contains the class structure and relevant functions for a Pushdown
Automaton mahcine
"""

from dataclasses import dataclass
from graphviz import Digraph


@dataclass
class pda:
    """General class that contains the structure of
    Pushdown Automata"""
    states: set
    start_state: str
    accept_states: set
    transitions: dict
    input_tape_alphabet: list[str]
    stack_alphabet: list[str]

    graph = Digraph

    def init(self, states, start_state, accept_states, transitions,
             input_tape_alphabet, stack_alphabet):
        self.input_tape_alphabet = input_tape_alphabet
        self.stack_alphabet = stack_alphabet
        self.accept_states = accept_states
        self.transitions = transitions
        self.start_state = start_state
        self.states = states

    def build_graph(self):
        """
        Build the graph for a pushdown automata class object
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

        loop_string = ""

        for input_tuple in self.transitions:
            state = input_tuple[0]
            input_symbol = input_tuple[1]
            pop_symbol = input_tuple[2]

            output = self.transitions[input_tuple]

            for o_tuple in output:
                go_to_state = o_tuple[0]
                push_symbol = o_tuple[1]

                if input_symbol == "epsilon":
                    input_symbol = 'ε'
                if pop_symbol == "epsilon":
                    pop_symbol = 'ε'
                if push_symbol == "epsilon":
                    push_symbol = 'ε'

                label_string = ""
                label_string += input_symbol + ","
                label_string += pop_symbol + "->"
                label_string += push_symbol

                if state == "q_Loop" and go_to_state == "q_Loop":
                    loop_string += label_string + "\n"
                else:
                    self.graph.edge(state, go_to_state, label=label_string)

        self.graph.edge("q_Loop", "q_Loop", label=loop_string)
        # Makes a pdf with name nfa.graph.pdf and views the pdf
        self.graph.render('pda', view=True)
