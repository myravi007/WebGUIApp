FILENAME_PATH = "learningfile.txt"


def file_read(file_name_var=FILENAME_PATH):
    with open(file_name_var, "r") as f_local:
        lst_action_local = f_local.readlines()
    return lst_action_local


def file_write(lst_action_var, file_name_var=FILENAME_PATH):
    with open(file_name_var, "w") as f_local:
        f_local.writelines(lst_action_var)


print(__name__)
if __name__ == "__main__":
    print("Hello")
