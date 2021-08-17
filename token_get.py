token = 'Bearer '

with open('token.txt', 'r') as f:
    token += f.read()
