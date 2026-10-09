from fastapi import Depends

from repositories.users import UserRepository
from schemas.users import CreateUserRequest, UpdateUserRequest


class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    def create_user(self, raw_user: CreateUserRequest):
        if self.repository.get_user_by_username(raw_user.username):
            return {
                "success": False,
                "message": f"User {raw_user.username} already exists."
            }
        else:
            user = self.repository.create_user(
                raw_user.username,
                raw_user.email,
                raw_user.password,
            )

            return {
                "success": True,
                "username": user.username,
                "email": user.email,
            }

    def get_all_users(self):
        users = self.repository.get_all_users()

        result = {}
        for user in users:
            result[user.username] = {
                "username": user.username,
                "email": user.email,
            }

        return result

    def get_user_by_username(self, username: str):
        user = self.repository.get_user_by_username(username)

        if user:
            return {
                "success": True,
                "username": user.username,
                "email": user.email,
            }
        else:
            return {"success": False, "message": "User not found."}

    def edit_user(self, username: str, upd_data: UpdateUserRequest):
        if not self.repository.get_user_by_username(username):
            return {"success": False, "message": "User not found."}
        else:
            upd_data = upd_data.model_dump()
            clear_dict = {}

            for k, v in upd_data.items():
                if v:
                    clear_dict[k] = v

            user = self.repository.edit_user(username, clear_dict)

            return {
                "success": True,
                "username": user.username,
                "email": user.email,
            }

    def delete_user(self, username: str):
        if not self.repository.get_user_by_username(username):
            return {"success": False, "message": "User not found."}
        else:
            self.repository.delete_user(username)

            return {"success": True, "message": "User was deleted."}