import user
from user import runtime_user_dict


def extract_user(username):
    if username in runtime_user_dict:
        print(runtime_user_dict[username])
        temp_user = user.User(runtime_user_dict[username]['email'], runtime_user_dict[username]['username'],  runtime_user_dict[username]['mast_password'])
        print(temp_user)
        return temp_user


extract_user("mikee")

