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

# Test
print("01: ", "Accepted" if dfa_board2("01") else "Rejected")
print("11: ", "Accepted" if dfa_board2("11") else "Rejected")