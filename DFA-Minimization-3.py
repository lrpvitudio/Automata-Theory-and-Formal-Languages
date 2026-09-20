def dfa_ex1(s):
    t = {
        'A':  {'0': 'A',  '1': 'B'},
        'B':  {'0': 'C',  '1': 'B'},
        'C':  {'0': 'A',  '1': 'DE'},
        'DE': {'0': 'DE', '1': 'DE'}
    }
    state = 'A'
    for c in s:
        state = t[state][c]
    return state == 'DE'

# 4 Inputs: 2 Accepted, 2 Rejected
tests = [
    ("101",   True),   
    ("01101", True),   
    ("1001",  False),  
    ("11000", False)   
]

print("--- Example 1: Substring '101' ---")
for string, _ in tests:
    res = "Accepted" if dfa_ex1(string) else "Rejected"
    print(f"Input: {string:<8} -> {res}")