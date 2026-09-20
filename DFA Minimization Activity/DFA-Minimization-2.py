def dfa_board2(s):
    t = {
        'AB':  {'0': 'AB',  '1': 'CDE'},
        'CDE': {'0': 'CDE', '1': 'F'},
        'F':   {'0': 'F',   '1': 'F'}
    }
    state = 'AB'
    for c in s:
        state = t[state][c]
    return state == 'CDE'

# 4 New Inputs: 2 Accepted, 2 Rejected
tests_b2 = [
    ("001",    True),   
    ("00100",  True),   
    ("101",    False),  
    ("0000",   False)   
]

print("\n--- Board 2 Tests ---")
for s, _ in tests_b2:
    print(f"{s:<6} -> {'Accepted' if dfa_board2(s) else 'Rejected'}")