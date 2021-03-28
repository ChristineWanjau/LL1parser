

# (LEXEME, r'regex string')
lexemes = [
    # main function
    ('MAIN', r'main'),                      

    # comment
    ('COMMENT', r'\/\/'),                     

    # data types
    ('INT', r'int'),                        # int
    ('FLOAT', r'float'),                    # float
    ('CHAR', r'char'),                      # float

    # control structures
    ('IF', r'if'),                          # if
    ('ELSE', r'else'),                      # else
    ('WHILE', r'while'),                    # while

    # other keywords
    ('RETURN', r'return'),                  # return

    # punctuators
    ('LBRACKET', r'\('),                    # (
    ('RBRACKET', r'\)'),                    # )
    ('LBRACE', r'\{'),                      # {
    ('RBRACE', r'\}'),                      # }
    ('COMMA', r','),                        # ,
    ('STMT_TERMINATOR', r';'),              # ;

    # relational operators
    ('EQ', r'=='),                          # ==
    ('NE', r'!='),                          # !=
    ('LE', r'<='),                          # <=
    ('GE', r'>='),                          # >=
    ('LT', r'<'),                           # <
    ('GT', r'>'),                           # >

    # logical operators
    ('OR', r'\|\|'),                        # ||
    ('AND', r'&&'),                         # &&
    # NOT?

    # assignment operator
    ('ASSIGNMENT', r'\='),                        # =

    # arithmetic operators
    ('PLUS_ASSIGN', r'\+='),                        # +
    ('MINUS_ASSIGN', r'-='),                        # -
    ('MULT_ASSIGN', r'\*='),                        # *
    ('DIV_ASSIGN', r'\/='),                         # /

    # shorthand assignment operators
    ('PLUS', r'\+'),                        # +=
    ('MINUS', r'-'),                        # -=
    ('MULT', r'\*'),                        # *=
    ('DIV', r'\/'),                         # /=

    # identifiers
    ('ID', r'[a-zA-Z]\w*'),

    # literals
    ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # float literal
    ('INTEGER_CONST', r'\d(\d)*'),          # int literal
    ('STRING_CONST', r'".*"'),              # string literal

    # other chars
    ('NEWLINE', r'\n'),                     # new line
    ('WHITESPACE', r'[ \t]+'),              # space and tabs
    ('ANY', r'.'),                          # any char
]