

def greetings (prompt):
    val = f'my name is {prompt}'

    return val

a = input('\n Enter a name:')
b = input('\n Enter the name of your highschool:')


def highschool(name):
    hs = f'the name of my highschool is {name}'
    return hs

def main():
    def surname(surname_string):
        s = f'my surname is {surname_string}'
        n = f'{greetings(a)}'+ ' ' + 'and' + ' ' + s + ' ' 'and' + ' ' + f'{highschool(b)}' + '\n'
        return n
    print(surname(input('\n Enter your surname:')))

if __name__ == "__main__":
    main()




