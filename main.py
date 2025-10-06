from fixtures import *
from io_functions import clear
from logs_base import save_logs



class Main:
    def __init__(self, menu:dict):
        self.menu = menu
        
    def show_menu(self):
        for key in self.menu:
            print(f"{key}. {self.menu[key]['description']}")
    
    def get_choice(self):
        while True:
            choice = input("Select an option: ")
            if choice in self.menu.keys():
                return choice
            else:
                print("ERROR: Please select the correct option.")
    
    def start(self):
        self.show_menu()
        self.choice = self.get_choice()
        self.func = self.menu[self.choice]['function']
        self.response = self.func()
        self.main_menu_handler()
        

    def dashboard_start(self , user_dict:dict):
        self.show_menu()
        self.choice = self.get_choice()
        self.func = self.menu[self.choice]['function']
        self.response = self.func(user_dict)           
        self.dashboard_menu_handler()
        
    
    def main_menu_handler(self):
        while True:
            if self.func == sign_up:
                if not self.response:
                    main.start()
                clear()
                save_logs(self.response["email"] ,self.response["username"] , self.response["id"],self.func)
                print(signup_prompt)
                main.start()
            elif self.func == login and self.response["authentication"] == "True" or self.func == forgot_password and not self.response:
                clear()
                save_logs(self.response["email"] ,self.response["username"] , self.response["id"],self.func)
                print(login_prompt)
                main2.dashboard_start(self.response)
                break
            elif self.func == forgot_password:
                clear()
                save_logs(self.response["email"] ,self.response["username"] , self.response["id"],self.func)
                print(forgot_pass_prompt)
                main.start()
            elif self.func == quit and not self.response:
                main.start()
                
                
    def dashboard_menu_handler(self):
        while True:
            if self.func == show_profile:
                clear()
                main2.dashboard_start(self.response)
            elif self.func == edit_profile:
                clear()
                main3.dashboard_start(self.response)
            elif self.func == logs:
                clear()
                main2.dashboard_start(self.response)
            elif self.func == delete_account:
                if not self.response:
                    print(delete_account_prompt)
                    main.start()
                    break
                else:
                    main2.dashboard_start(self.response)
            elif self.func == back:
                clear()
                main2.dashboard_start(self.response)
            elif self.func == logout:
                if not self.response:
                    print(logout_prompt)
                    main.start()
                    break
                main2.dashboard_start(self.response)
            else:
                self.edit_profile_menu_handler()
                
    def edit_profile_menu_handler(self):
        clear()
        print(change_prompt)
        main3.dashboard_start(self.response)
                

if __name__ == "__main__":
    main = Main(main_menu)
    main2 = Main(dashboard_menu)
    main3 = Main(edit_profile_menu)
    main.start() 