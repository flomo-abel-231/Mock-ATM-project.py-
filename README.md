name = input ( " what's your name? /n ")
AllowedUsers = [ 'Abel', ' Grace', 'Mogana']
AllowedPassword = [ 'passwordAbel', 'passwordGrace', ' passwordMogana']
UserID = AllowedUsers.index(name)


if ( name in AllowedUsers):
    Password = input ( " Your password? /n ")
    
    if ( Password == AllowedPassword[UserID]) : 
        print ( " Welcome %s" % name)
        print('1. Withdrawal ')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. Other services') 

        SelectedOption = int(input( ' Please select an option: '))
        
        if(SelectedOption == 1):
            print('you selected %s' % SelectedOption )

        elif(SelectedOption == 2):
                print('You selected %s' % SelectedOption)

        elif (SelectedOption == 3):
                print( " you selected %s" % SelectedOption)  

        elif ( SelectedOption == 4 ):
                print("you selected %s" % SelectedOption)  

        else: 
                print( """Selected invalid, please try again. Thank you""" )        

    else:
        print( 'Password incorrect, please try again')

else: 
   print('Name not found, please try again') 
