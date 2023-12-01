"""
file: CFG_to_PDA.py
author: Matthew Morrison msm8275

main file that converts a provided Context-Free Grammar and turns it into
an equivalent Pushdown Automata machine
"""


from Class_Structures import PDA_class as PDA
from Class_Structures import CFG_class as CFG


def create_new_pda(cfg):
    """
    create the initial pushdown automata with relevant information
    from a provided context-free grammar
    :param cfg:  the context-free grammar to obtain info from
    :return: the newly created pda and the bottom stack symbol that
    is used when building the pda
    """
    states = set()

    # add the three main states of the pda
    states.add("q_Start")
    states.add("q_Loop")
    states.add("q_Accept")

    # add the cfg's alphabet for the pda
    stack_alphabet = [cfg.alphabet]

    # add the cfg's alphabet for the pda
    input_tape_alphabet = [cfg.alphabet]

    if '$' not in input_tape_alphabet:
        bottom_stack_str = "$"
        input_tape_alphabet.append("$")
    else:
        bottom_stack_str = "%"
        input_tape_alphabet.append("%")

    pda_transitions = {}

    start_var = cfg.start_var
    start_state = "q_Start"
    accept_state = "q_Accept"

    # add epsilon transitions to working state and accept state
    pda_transitions[(start_state, "epsilon", "epsilon")] = \
        {("q_Loop", start_var + "$")}
    pda_transitions[("q_Loop", "epsilon", "$")] = \
        {("q_Accept", "epsilon")}

    accept_states = set()
    accept_states.add(accept_state)

    new_pda = PDA.pda(states, start_state, accept_states,
                      pda_transitions, input_tape_alphabet, stack_alphabet)
    return new_pda, bottom_stack_str


def epsilon_prod(curr_pda, curr_prod):
    """
    helper function for pda_from_cfg. Constructs the transition for when
    there is no input (i.e. an epsilon production)
    :param curr_prod: the current production to create the key with
    :param curr_pda: the current pda to update
    """
    key = ("q_Loop", "epsilon", curr_prod[0])
    if key not in curr_pda.transitions:
        curr_pda.transitions[("q_Loop", "epsilon", curr_prod[0])] = set()

    curr_pda.transitions[("q_Loop", "epsilon", curr_prod[0])].add(
        ("q_Loop", "epsilon"))


def single_symbol_prod(curr_pda, curr_prod):
    """
    helper function for pda_from_cfg. Constructs the transition for when
    the current production is just a single symbol
    :param curr_prod: the current production to create the transition with
    :param curr_pda: the current pda to update
    """
    key = ("q_Loop", "epsilon", curr_prod[0])
    if key not in curr_pda.transitions:
        curr_pda.transitions[("q_Loop", "epsilon", curr_prod[0])] = set()

    curr_pda.transitions[("q_Loop", "epsilon", curr_prod[0])].add(
        ("q_Loop", curr_prod[1]))


def construct_states(curr_pda, curr_state_num, rev_string, curr_var):
    """
    Helper function for pda_from_cfg. Construct states for a single
    production of the CFG
    :param curr_var: the current variable of the transition
    :param rev_string: the reversed production string of the transition
    (the states are built with this, as it needs to push onto the stack
    bakcwards)
    :param curr_state_num: the current state number
    :param curr_pda: the pda to update
    :return: the updated state number
    """

    # split string up into individual characters
    split_str = [*rev_string]

    # pop the stack for the variable that starts this transition in the PDA
    pop_var = curr_var
    # for every symbol in the reversed production
    for index, symbol in enumerate(split_str):
        if index == 0:
            key = ("q_Loop", "epsilon", pop_var)
            if key not in curr_pda.transitions:
                curr_pda.transitions[key] = set()
            curr_pda.transitions[key].add(
                ("q_" + str(curr_state_num), symbol))
            curr_pda.states.add("q_" + str(curr_state_num))

        elif index == len(split_str) - 1:
            state_name = "q_" + str(curr_state_num)
            key = (state_name, "epsilon", "epsilon")
            if key not in curr_pda.transitions:
                curr_pda.transitions[key] = set()
            curr_pda.transitions[key].add(
                ("q_Loop", symbol))
            curr_pda.states.add(state_name)
            curr_state_num += 1

        else:
            old_state = "q_" + str(curr_state_num)
            curr_state_num += 1
            # make a new state
            state_name = "q_" + str(curr_state_num)

            key = (old_state, "epsilon", "epsilon")
            if key not in curr_pda.transitions:
                curr_pda.transitions[key] = set()

            curr_pda.transitions[key].add(
                (state_name, symbol))
            # set pop_var to epsilon, only the variable needs to be popped in stack
            curr_pda.states.add(state_name)
        pop_var = "epsilon"

    return curr_state_num


def pda_from_cfg(cfg):
    """
    Construct the pushdown automata from a given context-free grammar
    :param cfg: the provided context-free grammar to build from
    :return: an equivalent pushdown automata machine of the cfg
    """

    new_pda, bottom_stack_str = create_new_pda(cfg)

    # base cases for the loop transition, for each symbol in the CFG
    # alphabet, have a transition that pushes nothing to stack
    for symbol in cfg.alphabet:
        new_pda.transitions[("q_Loop", symbol, symbol)] = \
            {("q_Loop", "epsilon")}

    # counter to designate states inside q_Loop
    state_counter = 0
    # for every variable that the CFG has
    for variable in cfg.variables:
        # loop through all the productions in the CFG to see what the
        # variable produces string wise
        for cfg_prod in cfg.productions:
            # if the production matches the variable, add states
            # to the q_Loop
            if cfg_prod[0] == variable:
                if cfg_prod[1] == "epsilon":
                    epsilon_prod(new_pda, cfg_prod)
                elif len(cfg_prod[1]) == 1:
                    single_symbol_prod(new_pda, cfg_prod)
                else:
                    # get the string produced by the variable
                    res_str = cfg_prod[1]
                    # reverse the string to construct states with
                    reverse_res_str = res_str[::-1]
                    state_counter = construct_states(new_pda, state_counter,
                                                     reverse_res_str,
                                                     variable)

    return new_pda


if __name__ == "__main__":
    print("Test 1")

    variables1 = set()
    variables1.add("S")
    variables1.add("T")

    alphabet1 = ["a", "b"]

    productions1 = set()
    productions1.add(("S", "aTb"))
    productions1.add(("S", "b"))
    productions1.add(("T", "Ta"))
    productions1.add(("T", "epsilon"))

    start_var1 = "S"

    cfg1 = CFG.CFG
    cfg1.alphabet = alphabet1
    cfg1.start_var = start_var1
    cfg1.variables = variables1
    cfg1.productions = productions1

    print("CFG 1")
    print("Variables: " + str(cfg1.variables))
    print("Alphabet: " + str(cfg1.alphabet))
    print("Productions: ")
    for production in cfg1.productions:
        print(str(production))
    print("Start Variable: " + cfg1.start_var)

    pda = pda_from_cfg(cfg1)

    print("Equivalent PDA")
    print("States: " + str(pda.states))
    print("Start State: " + pda.start_state)
    print("Accept States: " + str(pda.accept_states))
    print("Input Tape Alphabet: " + str(pda.input_tape_alphabet))
    print("Stack Alphabet: " + str(pda.stack_alphabet))
    print("Transitions:")
    for transitions in pda.transitions:
        output = pda.transitions[transitions]
        print(str(transitions) + " -> " + str(output))

    pda.build_graph()
