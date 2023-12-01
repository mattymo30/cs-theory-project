"""
file: turing_machine.py
author: Matthew Morrison msm8275

contains class structure for a Turing Machine and relevant functions to
run a Turing machine
"""

from dataclasses import dataclass
from graphviz import Digraph


def move_left(tape, write_symbol, new_head_pos):
    """
    Move left on the tape after a given transition move on
    :param tape: the Turing Machine's tape
    :param write_symbol: the symbol to write on the tape
    :param new_head_pos: the new head position of the Turing Machine
    :return: the update tape of the Turing Machine
    """
    old_head_pos = new_head_pos + 1

    if write_symbol != "ε":
        tape[old_head_pos] = write_symbol

    return tape


def move_right(tape, write_symbol, new_head_pos):
    """
    Move right on the tape after a given transition move on
    :param tape: the Turing Machine's tape
    :param write_symbol: the symbol to write on the tape
    :param new_head_pos: the new head position of the Turing Machine
    :return: the update tape of the Turing Machine
    """
    old_head_pos = new_head_pos - 1

    if write_symbol != "ε":
        tape[old_head_pos] = write_symbol

    return tape


def print_tape(tape, head_pos, state, curr_state):
    """
    print the current tape of the Turing Machine
    :param curr_state: the current state of the tape machine to print
    (always to the left of the current head position)
    :param tape: the tape of the Turing Machine
    :param head_pos: the current position of the read/write tape head
    :param state: the current state of the Turing Machine
    """
    print("State: " + state)
    tape_string = ""
    head_str = ""
    counter = 0
    head_pos += 1

    tape_with_state = []
    right_of_state = tape[curr_state:]
    left_of_state = tape[:curr_state]

    for char in left_of_state:
        tape_with_state.append(char)
    tape_with_state.append(state)
    for char in right_of_state:
        tape_with_state.append(char)

    for symbol in tape_with_state:
        length = len(tape_with_state[counter])
        tape_string += symbol + " "
        if length == 1 and counter != head_pos:
            head_str += "  "
        elif length != 1 and counter != head_pos:
            for x in range(length):
                head_str += " "
            head_str += " "
        if counter == head_pos:
            if length == 1:
                head_str += "^  "
            else:
                head_str += "^  "
                for x in range(length):
                    head_str += " "
        counter += 1

    if "^" not in head_str:
        head_str += "^ "
        tape_string += "⊔ "

    print(tape_string)
    print(head_str)
    print()


def single_transition(tm, curr_state, read_symbol):
    """
    Get the transition of the Turing Machine, provided with what is
    being read from the TM
    :param tm: the Turing Machine
    :param curr_state: the current state of the Turing Machine
    :param read_symbol: the symbol being read on the Turing Machine
    :return:
    """
    transition = tm.transitions[(curr_state, read_symbol)]
    new_state = transition[0]
    write_symbol = transition[1]
    movement = transition[2]

    return new_state, write_symbol, movement


@dataclass
class TM:
    """General class that contains the structure of
    a Turing Machine"""
    states: set
    input_alphabet: list[str]
    tape_alphabet: list[str]
    start_state: ''
    accept_state: ''
    reject_state: ''
    transitions: dict
    movements = ['R', 'L']
    end_of_tape = "⊔"

    graph = Digraph

    def empty_init(self):
        self.input_alphabet = []
        self.tape_alphabet = []
        self.accept_state = ""
        self.reject_state = ""
        self.transitions = {}
        self.start_state = ""
        self.states = set()
        self.graph = Digraph()

    def init(self, states, start_state, accept_state, reject_state, transitions,
             input_alphabet, tape_alphabet):
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.transitions = transitions
        self.start_state = start_state
        self.states = states
        self.graph = Digraph()

    def run_tm(self, input_string):
        """
        Run the Turing Machine on a given string and state if it is
        accepted or rejected
        :param input_string: the string to be tested on the Turing Machine
        """
        # initialize the TM's tape with the start state and string
        tape = []
        for char in input_string:
            tape.append(char)
        tape.append(self.end_of_tape)
        # head position starts at 1, so it doesn't start at the state
        head_position = 0
        # hold state position to update for tape printing
        state_pos = 0

        curr_state = self.start_state

        while curr_state != self.reject_state and curr_state != self.accept_state:
            read_symbol = tape[head_position]
            # print the tapes current state
            print_tape(tape, head_position, curr_state, state_pos)

            # perform a single movement using the TM's transitions
            new_state, write_sym, movement = single_transition(
                self, curr_state, read_symbol)
            if movement == "R":

                head_position += 1
                tape = move_right(tape, write_sym, head_position)
                state_pos += 1
            else:
                head_position -= 1
                tape = move_left(tape, write_sym, head_position)
                state_pos -= 1

            curr_state = new_state

        print("Final Tape: ")
        print_tape(tape, head_position, curr_state, state_pos)

        if curr_state == self.accept_state:
            print("Input Accepted")
        else:
            print("Input Rejected")
