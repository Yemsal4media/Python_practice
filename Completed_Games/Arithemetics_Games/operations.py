# operations
import random 
import Arith

def Binary_operation():
    LHS= random.randint(min_guess, max_guess)
    RHS= random.randint(min_guess, max_guess)
    bin_oprtns = random.choice(bin_oprtn)

    expr = str(LHS) + " " + bin_oprtns + " " + str(RHS)
    answer = eval(expr)
    return expr, answer