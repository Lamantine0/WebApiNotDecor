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


                
create_new_user = User()

user = create_new_user.create_user("ASas", "ASas@aa.vv")

print(f"username : {user.username} email {user.email}")




         


