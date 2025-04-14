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
                               5. press any other key to exit
                                    -->   """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.loggin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.msg() 
        else:
            exit()


    def signup(self):
        email = input("please enter yor email --> ")
        pw = input("enter a valid password  --> ")
        self.username = email 
        self.password = pw
        print("\n")
        print("you have succesfully signed up !!")
        print("\n")
        self.menu()
        

    def loggin(self):
        if self.username == '' and self.password == '':
            print("please sign up first ")
        else:
            uname = input("enter your email/username : ")
            p = input("enter your password : ")
            print("\n")
            if self.username == uname and self.password == p:
                print("you have successfully logged in !!")
                self.loggedin = True 
            else:
                print("you have entered incorrect password ")
                print("please enter correct username/password or sign up first")
            print("\n")
            self.menu()

    def post(self):
        if self.loggedin == True:
            ps = input("write a post here : ")
            print("you have posted : " + ps)
        else:
            print("please logg in first by clicking 2")
        print("\n")
        self.menu()

    def msg(self):
        if self.loggedin == True:
            ms = input("enter your msg : ")
            fr = input("to whom you want to send this msg : ")
            print(f"msg sent to {fr}  successfully !!")
        else:
            print("please logg in first by clicking 2 ")
        print("\n")
        self.menu()



user1 = chatbook()
