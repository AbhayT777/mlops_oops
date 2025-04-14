class chatbook:
    def __init__(self):
        self.username = ' '
        self.password = ' '
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""welcome to chatbook !! how would you like to proceed?" 
                               1. press 1 to sign up
                               2. press 2 to log in 
                               3. press 3 to write a post
                               4. press 4 to message a friend
                               5. press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.loggin()
        elif user_input == "3":
            pass 
        elif user_input == "4":
            pass 
        else:
            exit()


    def signup(self):
        email = input("please enter yor email --> ")
        pw = input("enter a valid password  --> ")
        self.username = email 
        self.password = pw
        print("you have succesfully signed up !!")
        print("\n")
        self.menu()
        

    def loggin(self):
        if self.username == '' and self.password == '':
            print("please sign up first ")
        else:
            uname = input("enter your email/username : ")
            p = input("enter your password : ")
            if self.username == uname and self.password == p:
                print("you have successfully logged in !!")
                self.loggedin = True 
            else:
                print("you have entered incorrect password , pleas enter correct username/password")
            print("\n")
            self.menu()



obj = chatbook()
