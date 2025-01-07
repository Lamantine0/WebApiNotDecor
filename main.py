from DataBase.database import Table_user
from Setting_DB.settings_db import setting


class User:

    def __init__(self, username : str = None , email : str = None):

        self.username = username

        self.email = email



    def create_user(self, username : str, email: str):

        with setting.CreateSession() as db:

            user_create = Table_user(
                
                username = username,

                email = email
            )

            db.add(user_create)
            db.commit()
            db.refresh(user_create)

            return user_create  


    def input_user():

        create_new_user = User()

        username_input = input("Введите имя пользователя: ")

        email_input = input("Введите email: ")

        user = create_new_user.create_user(username_input, email_input)

        print(f"Пользователь создан : {user.username} | {user.email} ")

        print("\n")   

        print("="*30 + "\n")   


    def get_all_users():

        with setting.CreateSession() as db:

            user_list = []

            get_user = db.query(Table_user).all()

            for user in get_user:

              user_list.append({

                    "username" : user.username,

                    "email" : user.email
                    
                })
                    
        for user in user_list:
            print(f"Имя пользователя: {user['username']}, Email: {user['email']}")

            print("="*30 + "\n")        







            

User.input_user()


User.get_all_users()
         


