import tokenize

reader = open('amina.py').readline
tokens = tokenize.generate_tokens(reader)

print(next(tokens))

print(next(tokens))
