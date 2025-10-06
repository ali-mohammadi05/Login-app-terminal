import datetime
from database import *



def save_logs(email,username,id,function):
    user_log = [f"{str(email)},{str(username)},{str(id)},{function.__name__},{datetime.datetime.today().replace(microsecond=0)}\n"]
    with open("logs.csv" , mode="a") as logbase:
        logbase.writelines(user_log)


def user_logs(unique_field):
    with open("logs.csv") as logbase:
        lines_list = logbase.readlines()
    lines_list = [item.strip().split(',') for item in lines_list]
    show_list = list()
    for line in lines_list:
        if unique_field in line:
            show_list.append(line)
    show_list = [" -- ".join(item) for item in show_list]
    return show_list


def show_logs(logs_list):
    print(f"{'email':>15}{'username':>22}{'id':>25}{'function':>25}{'time':>20}")
    print("-" * 120)
    for log in logs_list:
        print(f"{log:>20}")
        print("-" * 120)