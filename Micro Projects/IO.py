def append_to_file(text):
    try:
        f = open('Employees.txt','a')
        f.writelines('\n' + text)
    except IOError:
        print('Error: Could not find file or read data')
    else:
        print('Content posted successfully!\n')
        f.close()

def read_file():
    try:
        f = open('Employees.txt','r')
        for line in f:
            print(line,end='')
    except:
        print('Error: Could not find file or read data')
    else:
        f.close()

while True:
    user_input = input('Add a new employee:\n')
    append_to_file(user_input)
    read_prompt = input('Would you like to read the files content? Enter yes or no\n')
    if read_prompt.lower()[0]=='y':
        read_file()
    elif read_prompt.lower()[0]=='n':
        print('No problem.')
    reprompt = input('\nWould you like to add another employee? Enter yes or no\n')
    if reprompt.lower()[0]=='y':
        continue
    else:
        break
        

