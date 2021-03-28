import sys
import itertools

#list of Terminals in the grammar
T = {';','{','}','ID','(',')','int','void','binary','decimal',',','[',']','{','}','read','write','string','=','&&','||','==','!=','>'
     ,'>=','<','<=','while','return','break','continue','+','-','*','/','number','print','if'}
#list of Non-Terminals in the grammar
NT = {'program','data_decls','func_list','func','func_decl','func1','type_name','parameter_list','non_empty_list','non_empty_list1','id_list','id_list1','id','id1','expression','block_statements','statements','statement','assignment','func_call','if_statement','while_statement','return_statement','break_statement'\
      ,'continue_statement','expr_list','non_empty_expr_list','non_empty_expr_list1','condition_expression','condition_expression1','condition_op','condition','comparison_op','return_statement1','expression1','term','factor','term1','mulop','factor1','addop','parameter_list1','program1','program2','program3','program4','assignment1','statement1'}

#start,empty and end of file symbols
S = 'program'
empty = {'empty'}
eof = {'eof'}

#open and read the grammar file to get all the production rules
f_grammar = open('C:\\Users\\hp\\Downloads\\python-scanner-main\\python-scanner-main\\grammar.txt','r')
P = []
for line in f_grammar:
    P.append(line.strip('\n'))


#list of valid reserved keywords supported
reserve_word_list = ["int","void","if","while","return","read","write","print","continue","break","binary","decimal"]

#list of all valid symbols supported(except / as its checked seperately)
symbol_list = ["(",")","{","}","[","]",",",";","+","-","*","==","!=",">=","<=","<",">","=","&&","||"]


#computing first sets for all the symbols in the grammar
first = {}
prev_first = {}

for t in (T | empty | eof):
    first[t] = {t}

for nt in NT:
    first[nt] = set()

firstset_change = True

while(firstset_change):
 for p in P:
   A = p.split("->")[0]
   beta = p.split("->")[1]
   if(beta.count("||") >=1):
     beta = beta.split('|',maxsplit=1)
   else:
     beta = beta.split('|')
   rhs = set()
   for b in beta:
      b = b.split(' ')
      k = len(b) - 1
      rhs  = first[b[0]] - empty
      i = 0
      while('empty' in first[b[i]] and i<= k - 1 ):
          rhs = rhs | (first[b[i+1]] - empty)
          i += 1
      if(i == k and 'empty' in first[b[k]]):
          rhs = rhs | empty
      first[A] = first[A] | rhs
 if(prev_first == first):
       firstset_change = False
 prev_first = first.copy()


#computing follow sets for all the symbols in the grammar
follow = {}
prev_follow = {}

for nt in NT:
    follow[nt] = set()

follow[S] = follow[S] | eof

followset_change = True

while(followset_change):
 for p in P:
        A = p.split("->")[0]
        beta = p.split("->")[1]
        if(beta.count("||") >=1):
          beta = beta.split('|',maxsplit=1)
        else:
          beta = beta.split('|')
        trailer = set()
        for b in beta:
           b = b.split(' ')
           k = len(b) - 1
           trailer = follow[A]
           for i in range(k,-1,-1):
               if(b[i] in NT):
                   follow[b[i]] = follow[b[i]] | trailer
                   if('empty' in first[b[i]]):
                       trailer = trailer | (first[b[i]] - empty)
                   else:
                       trailer = first[b[i]]
               else:
                   trailer = first[b[i]]
 if(prev_follow == follow):
      followset_change = False
 prev_follow = follow.copy()

#computing First+ sets using the first and follow sets
first_plus  = {}

for p in P:
        A = p.split("->")[0]
        beta = p.split("->")[1]
        if(beta.count("||") >=1):
          beta = beta.split('|',maxsplit=1)
        else:
          beta = beta.split('|')
        for item in beta:
           b = item.split(' ')
           key = A + '->' + item
           if('empty' not in first[b[0]]):
               first_plus[key] = first[b[0]]
           else:
               first_plus[key] = first[b[0]] | follow[A]

#checking for LL(1) grammar condition using First+ sets
for p in P:
        A = p.split("->")[0]
        beta = p.split("->")[1]
        if(beta.count("||") >=1):
          beta = beta.split('|',maxsplit=1)
        else:
          beta = beta.split('|')
        if(len(beta)) > 1:
             for i, j in itertools.combinations(beta, 2):
                     k1 = A + '->' + i
                     k2 = A + '->' + j
                     if(first_plus[k1] & first_plus[k2]):
                         print('this grammar is not LL(1)')
                         exit()

        
print(first_plus)
# #creating the LL(1) parser table using the First+ sets
table = {}

for nt in NT:
    for t in T:
        table[(nt,t)] = 'error'
    for p in P:
        A = p.split("->")[0]
        beta = p.split("->")[1]
        if(beta.count("||") >=1):
          beta = beta.split('|',maxsplit=1)
        else:
          beta = beta.split('|')
        for item in beta:
            key = A + '->' + item
            for t in T:
             if t in first_plus[key]:
                 table[(A,t)] = key
             if('eof' in first_plus[key]):
                 table[(A,'eof')] = key

print(table)
