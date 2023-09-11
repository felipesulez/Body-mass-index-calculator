

def greetings (prompt):
    val = f'my name is {prompt}'

    return val

a = input('\n Enter a name:')

print(greetings(a))



def surname(surname_string):
    s = f'my surname is {surname_string}'
    n = f'{greetings(a)}'+ ' ' + s 
    return n
print(surname(input('\n Enter your surname:')))
