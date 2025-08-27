# input("Enter input String: ")

states = {'a', 'b', 'c'}
alphabet = {'0','1'}
transitions = {
    ('a', '0'): 'a',
    ('a', '1'): 'b',
    ('b', '0'): 'c',
    ('b', '1'): 'a',
    ('c', '0'): 'b',
    ('c', '1'): 'c'
}

start_state = 'a'
accept_states = {'c'}

def checkState(input_string):
    current_state = start_state

    for symbol in input_string:
        if (current_state, symbol) not in transitions:
            return "No valid transition"
        current_state = transitions[(current_state, symbol)]

    if current_state in accept_states:
        return "Accept"
    return "Reject"
    
print("NUMBER 1:")
# THREE ACCEPTED
print("ACCEPTED: ")
print(f"#1 String('10100'): {checkState('10100')}")
print(f"#2 String('101'): {checkState('101')}")
print(f"#3 String('1010011'): {checkState('1010011')}")

# THREE REJECTED
print("REJECTED: ")
print(f"#1 String('0110'): {checkState('0110')}")
print(f"#2 String('11100'): {checkState('11100')}")
print(f"#3 String('10110'): {checkState('10110')}")


states2 = {'q0', 'q1', 'q2', 'q3'}
alphabet2 = {'a','b'}
transitions2 = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q0',
    ('q3', 'a'): 'q2',
    ('q3', 'b'): 'q1'
}
start_state2 = 'q0'
accept_states2 = {'q0', 'q3'}

def checkState2(input_string):
    current_state = start_state2

    for symbol in input_string:
        if (current_state, symbol) not in transitions2:
            return "No valid transition"
        current_state = transitions2[(current_state, symbol)]

    if current_state in accept_states2:
        return "Accept"
    return "Reject"

print("\nNUMBER 2:")
# THREE ACCEPTED
print("ACCEPTED: ")
print(f"#1 String('aaba'): {checkState2('aaba')}")
print(f"#2 String('bbbaaa'): {checkState2('bbbaaa')}")
print(f"#3 String('ababab'): {checkState2('ababab')}")

# THREE REJECTED 
print("REJECTED: ")
print(f"#1 String('aab'): {checkState2('aab')}")
print(f"#2 String('bbaaa'): {checkState2('bbaaa')}")
print(f"#3 String('abababa'): {checkState2('abababa')}")