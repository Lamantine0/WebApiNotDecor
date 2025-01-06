from Setting_DB.settings_db import Base
from sqlalchemy.orm import Mapped, mapped_column
from Setting_DB.settings_db import setting



class Table_user(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(unique=True, nullable=False)



Base.metadata.create_all(setting.CreateEngine())