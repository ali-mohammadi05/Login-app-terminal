from base_functions import *



main_menu = {
    '1': {
        'description': 'Login',
        'function': login
    },
    '2': {
        'description': 'Sign up',
        'function': sign_up
    },
    '3': {
        'description': 'Forgot password',
        'function': forgot_password
    },
    'e': {
        'description': 'Exit',
        'function': quit
    }
}


dashboard_menu = {
    '1': {
        'description': 'Profile',
        'function': show_profile
    },
    '2': {
        'description': 'Edit Profile',
        'function': edit_profile
    },
    '3':{
        'description': 'logs',
        'function': logs
    },
    '4':{
        'description': 'delete account',
        'function': delete_account
    },
    'e': {
        'description': 'Logout',
        'function': logout
    }
}


edit_profile_menu = {
    '1': {
        'description': 'Change Firstname',
        'function': change_firstname
    },
    '2': {
        'description': 'Change Lastname',
        'function': change_lastname
    },
    '3':{
        'description': 'Change Username',
        'function': change_username
    },
    '4': {
        'description': 'Change Password',
        'function': change_password
    },
    '5':{
        'description': 'Change phone number',
        'function': change_phone_number
    },
    'e':{
       'description': 'Back',
        'function': back
    }
}


signup_prompt = """

                 \033[32mYOUR SIGNUP WAS SUCCESSFUL!\033[0m
                 
                 """


login_prompt = """

                \033[32mWELCOME TO YOUR ACCOUNT!\033[0m
                
                """


forgot_pass_prompt = """

                 \033[32mYOUR PASSWORD HAS CHANGED!\033[0m
                 
                 """
                 

logout_prompt =  """

                 \033[32mYOU LOGGED OUT FROM YOUR ACCOUNT!\033[0m
                 
                 """


change_prompt = """
                
                \033[32mCHANGE HAS SUCCESSFULLY APPLIED!\033[0m
                
                """


delete_account_prompt = """

                 \033[32mTHE ACCOUNT WAS REMOVED.\033[0m
                 
                 """