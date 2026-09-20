def dfa_ex2(s):
    t = {
        'q0':  {'0': 'q1',  '1': 'q2'},
        'q1':  {'0': 'q0',  '1': 'q35'},
        'q2':  {'0': 'q35', '1': 'q0'},
        'q4':  {'0': 'q35', '1': 'q0'},
        'q35': {'0': 'q2',  '1': 'q4'}
    }
    state = 'q0'
    for c in s:
        state = t[state][c]
    return state == 'q35'

# 4 Inputs: 2 Accepted, 2 Rejected
tests = [
    ("01",     True),   
    ("10",     True),   
    ("00",     False),  
    ("111",    False)   
]

print("--- Example 2: Parity DFA ---")
for string, _ in tests:
    res = "Accepted" if dfa_ex2(string) else "Rejected"
    print(f"Input: {string:<8} -> {res}")