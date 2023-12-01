"""
file: reg_exp_to_NFA.py
author: Matthew Morrison msm8275

main file that converts a provided regular expression and turns it into
an equivalent Non-Deterministic Finite Automata machine
"""


from Class_Structures import NFA, reg_exp_class as re


def union_operator(exp1, exp2, st_counter):
    """
    perform the union operation on the regular expression
    i.e. (a+b) = L(a) U L(b)

    :param exp1: the nfa representation of the first regular expression
    :param exp2: the nfa representation of the second regular expression
    :param st_counter: the current state in the counter to create accommodating
    states for the operator
    :return: a newly formatted nfa with the two expressions
    """
    new_nfa = NFA.new_nfa(set(), "", set(), dict(), exp1.alphabet)

    # add all their states together for the new nfa
    new_nfa.states.update(exp1.states)
    new_nfa.states.update(exp2.states)

    subscript = chr(0x2080 + st_counter)
    # add the new start state and new final state
    new_nfa.states.add("q" + subscript)
    new_nfa.states.add("f" + subscript)

    new_nfa.start_state = "q" + subscript
    new_nfa.accept_states = {"f" + subscript}

    # add new epsilon transitions to the new NFA
    new_nfa.transitions = dict()

    new_nfa.transitions.update(exp1.transitions)
    new_nfa.transitions.update(exp2.transitions)

    exp1_start_state = str(exp1.start_state)
    exp2_start_state = str(exp2.start_state)

    # build the epsilon transition for the new start state
    new_nfa.transitions["q" + subscript] = {}
    new_nfa.transitions["q" + subscript]["epsilon"] = {exp1_start_state, exp2_start_state}
    for letter in exp1.alphabet:
        new_nfa.transitions["q" + subscript][letter] = {}

    # get both RE's final state
    exp1_final_state = exp1.accept_states
    exp2_final_state = exp2.accept_states

    exp1_final_state = exp1_final_state.pop()
    exp2_final_state = exp2_final_state.pop()

    new_nfa.transitions[exp1_final_state] = {}
    new_nfa.transitions[exp2_final_state] = {}

    # update their epsilon transition to the new final state
    new_nfa.transitions[exp1_final_state]["epsilon"] = {"f" + subscript}
    new_nfa.transitions[exp2_final_state]["epsilon"] = {"f" + subscript}

    # initialize final state's transitions to go nowhere
    new_nfa.transitions["f" + subscript] = {}
    new_nfa.transitions["f" + subscript]["epsilon"] = {}
    for letter in exp1.alphabet:
        new_nfa.transitions["f" + subscript][letter] = {}

    return new_nfa


def concat_operator(exp1, exp2):
    """
    perform the dot/concat operation on the regular expression
    i.e. (ab) = L(a) ○ L(b)
    :param exp1: the nfa representation of the first regular expression
    :param exp2: the nfa representation of the second regular expression
    :return: a newly formatted nfa with the two expressions
    """
    new_nfa = NFA.new_nfa(set(), "", set(), dict(), exp1.alphabet)

    # add all their states together for the new nfa
    new_nfa.states.update(exp1.states)
    new_nfa.states.update(exp2.states)

    # add new epsilon transitions to the new NFA
    new_nfa.transitions = dict()

    new_nfa.transitions.update(exp1.transitions)
    new_nfa.transitions.update(exp2.transitions)

    # get the start and end states for both expressions
    exp1_start_state = exp1.start_state
    exp2_start_state = exp2.start_state
    exp1_final_state = ""
    exp2_final_state = ""

    for fs in exp1.accept_states:
        exp1_final_state = fs
    for fs in exp2.accept_states:
        exp2_final_state = fs

    new_nfa.start_state = exp1_start_state
    new_nfa.accept_states = {exp2_final_state}

    # add the epsilon transition from exp1 to exp2
    new_nfa.transitions[exp1_final_state]["epsilon"] = {exp2_start_state}
    new_nfa.transitions[exp2_final_state]["epsilon"] = {}

    return new_nfa


def kleene_star_operations(nfa, st_counter):
    """
    perform any of the kleene star operations, which include the following:
    a^*, a^+, a^n where n is a natural number
    :param nfa: the nfa representation of the expression to update
    :param st_counter: the current state in the counter to create accommodating
    states for the operator
    :return: an updated nfa of the expression
    """

    subscript = chr(0x2080 + st_counter)
    # create the new start and final state
    nfa.states.add("q" + subscript)
    nfa.states.add("f" + subscript)

    nfa_start = nfa.start_state
    nfa_final = nfa.accept_states

    nfa.start_state = "q" + subscript
    nfa.accept_states = {"f" + subscript}

    # update the transitions from the original expression to account for the
    # newly added states
    nfa.transitions["q" + subscript] = {}
    nfa.transitions["q" + subscript]["epsilon"] = {nfa_start, "f" + subscript}

    for final_state in nfa_final:
        nfa.transitions[final_state]["epsilon"] = {nfa_start, "f" + subscript}

    # initialize final state's transitions to go nowhere
    nfa.transitions["f" + subscript] = {}
    nfa.transitions["f" + subscript]["epsilon"] = {}
    for letter in nfa.alphabet:
        nfa.transitions["f" + subscript][letter] = {}

    return nfa


def empty_set(nfa, alphabet):
    """
    construct the NFA when it is just the empty set Φ (unicode \u03A6)
    :param nfa: the nfa representation of the expression
    :param alphabet: the alphabet of the regular expression
    """

    nfa.states.add("q\u2080")
    nfa.states.add("f\u2080")
    nfa.start_state = "q\u2080"
    nfa.accept_states.append("f\u2080")

    nfa.alphabet = alphabet
    nfa.transitions["q\u2080"] = {}
    nfa.transitions["q\u2080"]["epsilon"] = {}

    for letter in alphabet:
        nfa.transitions["q\u2080"][letter] = {}

    nfa.transitions["f\u2080"] = {}
    nfa.transitions["f\u2080"]["epsilon"] = {}
    for letter in alphabet:
        nfa.transitions["f\u2080"][letter] = {}


def epsilon_expression(nfa, alphabet):
    """
    construct the NFA when it is just the empty string ε (unicode \u03B5)
    :param nfa: the nfa representation of the expression
    :param alphabet: the alphabet of the regular expression
    """
    nfa.states.add("q\u2080")
    nfa.start_state = "q\u2080"
    nfa.accept_states.append("q\u2080")

    nfa.alphabet = alphabet
    nfa.transitions["q\u2080"] = {}
    nfa.transitions["q\u2080"]["epsilon"] = {}
    for letter in alphabet:
        nfa.transitions["q\u2080"][letter] = {}


def single_symbol_expression(nfa, expression, alphabet, st_counter):
    """
    construct the NFA when it is just a letter σ in alphabet Σ of the expression
    :param nfa: the nfa representation of the expression
    :param expression: the current regular expression (should be a symbol)
    :param alphabet: the alphabet of the regular expression
    :param st_counter: the current state in the counter to create accommodating
    states for the nfa
    """
    subscript = chr(0x2080 + st_counter)

    nfa.states.add("q" + subscript)
    nfa.states.add("f" + subscript)
    nfa.start_state = "q" + subscript
    nfa.accept_states.append("f" + subscript)

    nfa.alphabet = alphabet

    nfa.transitions["q" + subscript] = {}
    nfa.transitions["q" + subscript]["epsilon"] = {}

    for letter in alphabet:
        if letter == expression:
            nfa.transitions["q" + subscript][letter] = {"f" + subscript}
        else:
            nfa.transitions["q" + subscript][letter] = {}

    nfa.transitions["f" + subscript] = {}
    nfa.transitions["f" + subscript]["epsilon"] = {}
    for letter in alphabet:
        nfa.transitions["f" + subscript][letter] = {}


def read_expression(nfa, reg_exp, st_counter):
    """
    Read the expression and create a nfa representation of it
    :param nfa: the current state of the nfa for the expression
    :param reg_exp: the regular expression
    :param st_counter: the current state counter to accommodate for
    any new states generated
    :return: the nfa representation of the regular expression
    """
    exp = reg_exp.expression

    exp_stack = []

    # build up the expression left to right
    counter = 0
    while counter < len(reg_exp.expression):
        curr_char = exp[counter]

        if curr_char in nfa.alphabet:
            single_symbol_expression(nfa, curr_char, nfa.alphabet, st_counter)
            st_counter += 1
            exp_stack.append(nfa)
        elif curr_char in re.RegularExpression.reg_exp_symbols:
            # Perform the appropriate operation
            # kleene star has the highest precedence, so just compute the expression
            if curr_char == '*':
                operand1 = exp_stack.pop()
                operand1 = kleene_star_operations(operand1, st_counter)
                st_counter += 1
                exp_stack.append(operand1)
            # concat has the second highest precedence
            elif curr_char == '.':
                operand1 = exp_stack.pop()
                # first check for any kleene star first
                curr_index = counter + 1
                right_most_index = counter + 1
                operand2 = NFA.new_nfa(set(), "", [], dict(), nfa.alphabet)
                right_reg_exp = exp[curr_index:]

                if len(right_reg_exp) == 1 and right_reg_exp in nfa.alphabet:
                    single_symbol_expression(operand2, right_reg_exp, nfa.alphabet, st_counter)
                    st_counter += 1
                    counter = right_most_index
                else:
                    for symbol in right_reg_exp:
                        # if there is a kleene star, it has higher precedence, construct
                        # its nfa first before the concat operator
                        if symbol == '*':
                            right_reg_exp = exp[curr_index:right_most_index + 1]
                            reg_exp2 = re.RegularExpression(alphabet=nfa.alphabet)
                            reg_exp2.expression = right_reg_exp
                            right_nfa = NFA.new_nfa(set(), "", [], dict(), nfa.alphabet)
                            operand2, st_counter = read_expression(right_nfa, reg_exp2, st_counter)
                            counter = right_most_index
                            break
                        # any other symbol does not have higher precedence,
                        # treat as a single symbol and just
                        elif symbol == "." or symbol == "+":
                            right_reg_exp = exp[curr_index:right_most_index + 1]
                            single_symbol_expression(operand2, right_reg_exp, nfa.alphabet, st_counter)
                            break
                        elif symbol == "(":
                            start_paren_counter = 1
                            curr_index = counter + 1
                            right_most_index = counter + 1
                            right_reg_exp = exp[curr_index:]
                            for symbol in right_reg_exp:
                                if symbol == ")":
                                    start_paren_counter -= 1
                                    if start_paren_counter == 0:
                                        right_reg_exp = exp[curr_index:right_most_index]
                                        inside_paren_exp = re.RegularExpression(alphabet=nfa.alphabet)
                                        inside_paren_exp.expression = right_reg_exp
                                        paren_nfa = NFA.new_nfa(set(), "", [], dict(), nfa.alphabet)
                                        operand1, st_counter = read_expression(paren_nfa, inside_paren_exp, st_counter)
                                        counter = right_most_index
                                        exp_stack.append(operand1)
                                        break
                                elif symbol == "(":
                                    start_paren_counter += 1
                                elif right_most_index >= len(reg_exp.expression):
                                    raise ValueError("Invalid expression: {}".format(reg_exp.expression))
                        right_most_index += 1
                operand1 = concat_operator(operand1, operand2)
                st_counter += 1
                exp_stack.append(operand1)
            elif curr_char == '+':
                operand1 = exp_stack.pop()
                # look for any operands after +, since it has lowest precedence
                curr_index = counter + 1
                right_most_index = counter + 1
                operand2 = NFA.new_nfa(set(), "", [], dict(), nfa.alphabet)
                right_reg_exp = exp[curr_index:]

                if len(right_reg_exp) == 1 and right_reg_exp in nfa.alphabet:
                    single_symbol_expression(operand2, right_reg_exp, nfa.alphabet, st_counter)
                    st_counter += 1
                    counter = right_most_index
                else:
                    for symbol in right_reg_exp:
                        # if there is
                        if symbol == '*' or symbol == '.':
                            right_reg_exp = exp[curr_index:right_most_index + 1]
                            reg_exp2 = re.RegularExpression(alphabet=nfa.alphabet)
                            reg_exp2.expression = right_reg_exp
                            right_nfa = NFA.new_nfa(set(), "", [], dict(), nfa.alphabet)
                            operand2, st_counter = read_expression(right_nfa, reg_exp2, st_counter)
                            counter = right_most_index
                            break
                        right_most_index += 1
                operand1 = union_operator(operand1, operand2, st_counter)
                st_counter += 1
                exp_stack.append(operand1)
        elif curr_char == "(":
            start_paren_counter = 1
            curr_index = counter + 1
            right_most_index = counter + 1
            right_reg_exp = exp[curr_index:]
            for symbol in right_reg_exp:
                if symbol == ")":
                    start_paren_counter -= 1
                    if start_paren_counter == 0:
                        right_reg_exp = exp[curr_index:right_most_index]
                        inside_paren_exp = re.RegularExpression(alphabet=nfa.alphabet)
                        inside_paren_exp.expression = right_reg_exp
                        paren_nfa = NFA.new_nfa(set(), "", [], dict(), nfa.alphabet)
                        operand1, st_counter = read_expression(paren_nfa, inside_paren_exp, st_counter)
                        counter = right_most_index
                        exp_stack.append(operand1)
                        break
                elif symbol == "(":
                    start_paren_counter += 1
                elif right_most_index >= len(reg_exp.expression):
                    raise ValueError("Invalid expression: {}".format(reg_exp.expression))

                right_most_index += 1
        else:
            # Handle the case where the binary operation is not followed by a symbol
            raise ValueError("Invalid expression: {}{}".format(curr_char, reg_exp[counter + 1:]))

        counter += 1

    # The final NFA is on top of the stack
    final_nfa = exp_stack.pop()

    # Update the states, start state, accept states, and transitions of the original NFA
    nfa.states = final_nfa.states
    nfa.start_state = final_nfa.start_state
    nfa.accept_states = final_nfa.accept_states
    nfa.transitions = final_nfa.transitions

    return nfa, st_counter


def construct_nfa(expression, alphabet):
    """
    costruct the NFA given a regular expression
    :param alphabet:
    :param expression: the str representation of the regular expression to use
    and convert with
    :return: a new NFA built from the regular expression
    """
    nfa = NFA.new_nfa(set(), "", [], dict(), alphabet)
    # perform the empty set operation if the user entered nothing
    if expression == "\u03A6":
        empty_set(nfa, alphabet)
    # perform the epsilon transition if the user entered "epsilon"
    elif expression == "\u03B5":
        epsilon_expression(nfa, alphabet)
    # if there is only a single symbol in the expression
    elif len(expression) == 1 and expression in alphabet:
        single_symbol_expression(nfa, expression, alphabet, 0)
    # all other cases (concat, union, kleene, and a combination of them
    else:
        # create the regular expression with reg_exp_class
        reg_exp = re.RegularExpression(alphabet=alphabet)
        reg_exp.expression = expression
        nfa, st_counter = read_expression(nfa, reg_exp, 0)

    return nfa
