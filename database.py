def user_dict(unique_field) -> dict:
    with open("data.csv") as database:
        lines = database.readlines()
    header_list = lines[0].strip().split(',')
    lines = [item.strip().split(',') for item in lines]
    lines.pop(0)
    for items in lines:
        if unique_field in items:
            user_list = items 
            break
    return dict(zip(header_list , user_list))


def remove_account(user:dict):
    with open("data.csv") as database:
        lines = database.readlines()
    lines = [item.split(',') for item in lines]
    for index,line in enumerate(lines):
        if user['id'] in line:
            user_line = lines.pop(index)
            break
    lines = [','.join(item) for item in lines]
    with open('data.csv' , mode='w') as database:
        database.writelines(lines)
    user_line = ','.join(user_line)
    with open('deleted_accounts.csv' , mode='a') as delbase:
        delbase.write(user_line)


def get_user_by(pattern_header , wanted_header ,pattern_value):
    pattern_header_list = get_column(pattern_header)
    index = pattern_header_list.index(pattern_value)
    wanted_header_list = get_column(wanted_header)
    return wanted_header_list[index]


def change_data(user_data , header , new_value):
    with open("data.csv") as database:
        lines = database.readlines()
    header_list = lines[0].strip().split(',')
    target_index = header_list.index(header)
    lines =[item.split(',') for item in lines] 
    for line in lines:
        if user_data in line:
            line[target_index] = new_value
            break
    lines = [','.join(items) for items in lines]
    with open("data.csv" , "w") as file:
        file.writelines(lines)


def get_column(header_name) -> list:
    with open("data.csv") as database:
        lines_list = database.readlines()
    header = lines_list[0].split(',')
    index_num = header.index(header_name)
    lines_list = [item.strip() for item in lines_list]
    lines_list = [item.split(',') for item in lines_list]
    header_name_data = []
    for i in range(len(lines_list)):
        header_name_data.append(lines_list[i][index_num])
    header_name_data.pop(0)
    return header_name_data