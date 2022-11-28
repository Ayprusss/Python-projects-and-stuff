name = str(input('What is your name?: '))
transfer = float(input('How much money do you want to transfer?: '))
recipient = str(input('Who is the recipient?: '))
question = str(input('What is your security question?: '))
answer = str(input("What is the security question's answer?: "))

print(name+',','you received', transfer, 'from', name, 'via e-transfer. Do you accept?: [Answer Y/N]')
response = str((input('')))
if response == 'Y' or response == 'y':
    print('Security Question:', question)
    response2 = str(input(''))
    if response2 == answer or response2 == answer.lower():
        print(name,'The security question is correct. The money is deposited in your account.')
        quit()
    if response2 != answer and response2 == answer.lower():
        print('Sorry, the security question is wrong. the money was returned to', name)
        quit()
    elif response2 != answer:
        print('Sorry, the security question is wrong. the money was returned to', name)
        quit()
else:
    print(name + ',' ,'your e-transfer was declined by', recipient)



