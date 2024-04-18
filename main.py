from models.data import users
from utils.crud import show_users



if __name__ == "__main__":
    print("Witaj użytkowniku")
    while True:
        print("Menu:")
        print("0. zakończ program")
        print("1. Wyświetl co u znajomych")
        print("2. dodaj użytkownika")
        menu_option: str = input("dokonaj wyboru:")
        if menu_option == "0":
            print("program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)
        if menu_option == "2":
            add_new_user(users)