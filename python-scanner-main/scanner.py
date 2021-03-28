
import re
from lexemes import lexemes as rules
from typing import NamedTuple

class Token(NamedTuple):
    type: str
    value: str
    line: int

program_path = 'C:\\Users\\hp\\Downloads\\python-scanner-main\\python-scanner-main\\program.c'
lexemes_regex = '|'.join('(?P<%s>%s)' % pair for pair in rules)

def tokenize(code):
    line_count = 0
    tokens = []
    lexemes = []

    for mo in re.finditer(lexemes_regex, code):
        kind = mo.lastgroup
        value = mo.group()

        # elif kind == 'ID' and value in keywords:
        #     kind = value

        # if kind == 'INT':
        #     value = int(value)

        # elif kind == 'FLOAT':
        #     value = float(value)

        if kind == 'NEWLINE':
            line_count += 1
            continue

        elif kind == 'WHITESPACE':
            continue

        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_count}')

        yield(Token(kind, value, line_count))

# open in read mode
with open(program_path, 'r') as fd:
    code = fd.read()

    for token in tokenize(code):
        print(token)    


# reference - https://docs.python.org/3/library/re.html#writing-a-tokenizer