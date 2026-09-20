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

# Test
print("011011:", "Accepted" if dfa_board1("011011") else "Rejected")
print("0110:  ", "Accepted" if dfa_board1("0110") else "Rejected")