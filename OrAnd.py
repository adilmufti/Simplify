import re

# (p ∨ q) ∧ (p ∨ r) -> p ∨ (p ∧ r)
'''
p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r) DONE
p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) DONE
p ∨ (p ∧ q) ≡ p DONE
p ∧ (p ∨ q) ≡ p DONE
p ∧ p = p DONE
p ∨ p = p DONE
p ∨ q ≡ ¬p → q DONE
p ∧ q ≡ ¬(p → ¬q) DONE
¬(¬p) = p DONE
¬(p ∨ q) = Nothing DONE
'''

#1 (p ∨ q) ∧ (p ∨ r) -> p ∨ (p ∧ r)
def num1():
    pattern = r"\([a-z] ∨ [a-z]\) ∧ \([a-z] ∨ [a-z]\)"
    string = "(p ∨ q) ∧ (p ∨ r)"

    print(string)
    if re.search(pattern, string):
        print("check 1: passed")

        lb, rb = string.split(" ∧ ")

        lb_1 = lb[1]
        lb_2 = lb[-2]
        rb_1 = rb[1]
        rb_2 = rb[-2]

        print("letters:", lb_1, lb_2, rb_1, rb_2)

        if lb_1 == rb_1:
            print("check 2: passed")

            print(f"{lb_1} ∨ ({lb_2} ∧ {rb_2})")
    else:
        print("check 1: failed")


#2 p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
def num2():
    pattern = r"\([a-z] ∧ [a-z]\) ∨ \([a-z] ∧ [a-z]\)"
    string = "(p ∧ q) ∨ (p ∧ r)"

    print(string)
    if re.search(pattern, string):
        print("check 1: passed")

        lb, rb = string.split(" ∧ ")

        lb_1 = lb[1]
        lb_2 = lb[-2]
        rb_1 = rb[1]
        rb_2 = rb[-2]

        print("letters:", lb_1, lb_2, rb_1, rb_2)

        if lb_1 == rb_1:
            print("check 2: passed")

            print(f"{lb_1} ∨ ({lb_2} ∧ {rb_2})")
    else:
        print("check 1: failed")
