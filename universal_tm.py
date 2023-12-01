"""
file: universal_tm.py
author: Matthew Morrison msm8275

main file that implements a Universal Turing Machine (UTM).
a UTM takes a description of a Turing Machine and an input string,
to which it runs the TM and accepts or rejects based on the simulation of the
TM
"""

import sys

from Class_Structures import turing_machine as tm
import ast


def construct_tm(input_file):
    """
    construct the turing machine given an input file that describes the
    turing machine
    :param input_file: the inputted file to convert to a TM
    :return: a newly generated TM
    """

    # initialize the TM
    turing_machine = tm.TM(accept_state="", start_state="", reject_state="",
                           states=set(), input_alphabet=[], tape_alphabet=[],
                           transitions={})
    try:
        # open the file
        with open(input_file, "r", encoding="utf-8") as tm_file:
            lines = tm_file.readlines()
            # read every line in the file
            for line in lines:
                # update certain symbols to unicode chars or to blank spaces to
                # prevent errors
                line = line.replace("\n", "").replace("⊔", "\\u2294")\
                    .replace("epsilon", "\\u03B5")
                # this is the start state
                if line.startswith("Start:"):
                    split_line = line.split(":")
                    s_state = split_line[1].strip()
                    turing_machine.start_state = s_state
                # this is the accept state
                elif line.startswith("Accept:"):
                    split_line = line.split(":")
                    a_state = split_line[1].strip()
                    turing_machine.accept_state = a_state
                # this is the reject state
                elif line.startswith("Reject:"):
                    split_line = line.split(":")
                    r_state = split_line[1].strip()
                    turing_machine.reject_state = r_state
                # any other line input is a transition
                else:
                    line = ast.literal_eval(f'"{line}"')
                    # turn line to a tuple and remove unnecessary characters
                    tuple_line = list(line)
                    tuple_line = [item for item in tuple_line if item not in ('(', ')', ',', ' ')]

                    # construct the transition (states get separated)
                    tuple_line = [
                        tuple_line[0] + tuple_line[1],
                        tuple_line[2],
                        tuple_line[3] + tuple_line[4],
                        tuple_line[5],
                        tuple_line[6]
                    ]
                    # add relevant information to the TM
                    turing_machine.states.add(tuple_line[0])
                    turing_machine.input_alphabet.append(tuple_line[1])
                    turing_machine.tape_alphabet.append(tuple_line[1])
                    turing_machine.states.add(tuple_line[2])
                    turing_machine.tape_alphabet.append(tuple_line[3])
                    tm_input = (tuple_line[0], tuple_line[1])
                    output = (tuple_line[2], tuple_line[3], tuple_line[4])
                    turing_machine.transitions[tm_input] = output
    # file could not open, throw an error and end the program
    except OSError:
        print("Could not open file: ", input_file)
        sys.exit()

    # if the file did not contain necessary info, raise an exception and end
    if turing_machine.start_state is None:
        raise Exception("File did not include a start state")
    if turing_machine.accept_state is None:
        raise Exception("File did not include an accept state")
    if turing_machine.reject_state is None:
        raise Exception("File did not include a reject state")

    # remove any duplicates
    turing_machine.tape_alphabet = list(set(turing_machine.tape_alphabet))
    turing_machine.input_alphabet = list(set(turing_machine.input_alphabet))

    return turing_machine


def main(turing_machine_desc, input_string):
    """
    main function that runs the program.
    given a file and input string, construct a TM and simulate it
    :param turing_machine_desc: a file that describes a TM
    :param input_string: the input string to test on
    """
    turing_machine = construct_tm(turing_machine_desc)

    turing_machine.run_tm(input_string)


if __name__ == "__main__":
    file1 = "C:\\Users\\msmch\\IdeaProjects\\CS-Theory-Honors\\Test_Files\\UTM_Example_files\\palindromes.txt"
    main(file1, "bbbbbbbbbbbb")

