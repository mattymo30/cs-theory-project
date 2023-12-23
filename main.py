"""
file: main.py
author: Matthew Morrison msm8275

The main file that is able to call all four main files
(NFA_TO_DFA, reg_exp_to_NFA, CFG_to_PDA, universal_tm)
and allow users to choose test files to use.
"""


def call_nfa_to_dfa():
    return

def call_re_to_nfa():
    return

def cfg_to_pda():
    return

def call_utm():
    return


def main():

    while True:
        option = input("Select what function you want to test:\n"
              "0: NFA to DFA\n"
              "1: Regular Expression to NFA\n"
              "2: CFG to PDA\n"
              "3: Universal TM\n"
              "4: Quit")


        function = int
        match option:
            case "0":
            case "1":
            case "2":
            case "3":
            case "4":
                print("Goodbye!\n")
                break
            case _:
                print("Not a viable option!\n")
                continue
