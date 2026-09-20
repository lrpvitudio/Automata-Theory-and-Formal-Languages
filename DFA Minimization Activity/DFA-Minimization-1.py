def dfa_board1(s):
    t = {
        'AC': {'0': 'B',  '1': 'AC'},
        'B':  {'0': 'B',  '1': 'D'},
        'D':  {'0': 'B',  '1': 'E'},
        'E':  {'0': 'B',  '1': 'AC'}
    }
    state = 'AC'
    for c in s:
        state = t[state][c]
    return state == 'E'

# 4 New Inputs: 2 Accepted, 2 Rejected
tests_b1 = [
    ("011",    True),   
    ("10011",  True),   
    ("01",     False),  
    ("000",    False)   
]

print("--- Board 1 Tests ---")
for s, _ in tests_b1:
    print(f"{s:<6} -> {'Accepted' if dfa_board1(s) else 'Rejected'}")