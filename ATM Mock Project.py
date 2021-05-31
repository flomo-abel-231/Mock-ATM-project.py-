


name = input ( " what's your name? /n ")
AllowedUsers = [ 'Abel', ' Grace', 'Mogana']
AllowedPassword = [ 'passwordAbel', 'passwordGrace', ' passwordMogana']
UserID = AllowedUsers.index(name)
amount = 100 


if ( name in AllowedUsers):
    Password = input ( " Your password? /n ")
    
    if ( Password == AllowedPassword[UserID]) : 
        print ( " Welcome %s" % name) 
        import datetime 
        today = datetime.datetime.now()
        print('Date:', today)
        print('1. Withdrawal ')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. Other services') 




        def menu():
                print("Date: ", today)
                print('1. Withdrawal ')
                print('2. Cash Deposit')
                print('3. Complaint')
                print('4. Other services') 

        SelectedOption = int(input( ' Please select an option: '))
        
        while SelectedOption != 0:
                 if(SelectedOption == 1):
                   print('you selected %s' % SelectedOption )
                   print("withdraw")
                   input( 'How much will you like to withdraw: ')
                   print('Take your cash, Transaction successful')

                   print()
                   menu()
                   SelectedOption = int(input( ' Please select an option: ')) 
        
                 elif(SelectedOption == 2):
                    print('You selected %s' % SelectedOption)
                    print('Deposit')
                    input('How much would like to deposit: ')
                    Balance = (''' 15000 USD ''')
                    print(" your current balance is:", Balance )

                    print()
                    menu()
                    SelectedOption = int(input( 'Please select an option: '))

                 elif (SelectedOption == 3):
                    print( " you selected %s" % SelectedOption)
                    input('What issue will you like to report: ') 
                    print( 'Thank you for contacting us, Stay safe')  

                    print()
                    menu()
                    SelectedOption = int(input( ' Please select an option: '))

                 elif ( SelectedOption == 4 ):
                     print("you selected %s" % SelectedOption) 
                     
                     print() 
                     menu() 
                     SelectedOption = int(input ( ' please select an option:  ')) 

        else: 
                print( """Selected invalid, please try again. Thank you""" )        

    else:
        print( 'Password incorrect, please try again')

else: 
   print( ' Name not found, please try again') 
   
            
            

                


        
