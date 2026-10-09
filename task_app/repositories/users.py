from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import hash_password
from models.users import User


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_user(self, username: str, email, password: str):
        user = User(
            username=username,
            email=email,
            hashed_password=hash_password(password),
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(
            User.username == username
        ).first()

    def edit_user(self, username: str, upd_data: dict):
        user = self.get_user_by_username(username)

        if "email" in upd_data:
            user.email = upd_data["email"]

        if "password" in upd_data:
            user.hashed_password = hash_password(upd_data["password"])

        self.db.commit()
        self.db.refresh(user)

        return user

    def delete_user(self, username: str):
        user = self.get_user_by_username(username)

        self.db.delete(user)
        self.db.commit()