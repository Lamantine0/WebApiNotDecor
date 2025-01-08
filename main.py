from DataBase.database import Table_user
from Setting_DB.settings_db import setting


class User:

    def __init__(self, username : str = None , email : str = None):

        self.username = username

        self.email = email



    def create_user(self, username : str, email: str):
        
        while True:

            with setting.CreateSession() as db:

                user_create = Table_user(
                
                    username = username,

                    email = email
            )

                db.add(user_create)
                db.commit()
                db.refresh(user_create)

                return user_create  


    def input_user(self):

        while True:

            create_new_user = User()

            username_input = input("Введите имя пользователя: (или 'exit' для выхода):")

            if username_input.lower() == "exit":
                
                break

            email_input = input("Введите email: ")

            user = create_new_user.create_user(username_input, email_input)

            return(f"Пользователь создан : {user.username} | {user.email} ")




    def get_all_users(self):

        while True:
                
            with setting.CreateSession() as db:

                user_list = db.query(Table_user).all()

            if not user_list:

                print("Нет пользователей в базе данных.")
                 
            for user in user_list:

                print(f"ID Пользователя: {user.id} Имя пользователя: {user.username}, Email: {user.email}")

                print("=" * 30 + "\n")

            break                
            

user_manager = User()

user_manager.input_user()

user_manager.get_all_users()



         


