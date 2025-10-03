from sqlalchemy.orm import Session
from ..models.user import User, UserRole
from ..schemas.user import UserCreate
from ..schemas.auth import UserRegister

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserRegister, password_hash: str) -> User:
        user = User(
            name=user_data.name,
            email=user_data.email,
            password_hash=password_hash,
            role=user_data.role
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def update(self, user: User, update_data: dict) -> User:
        for field, value in update_data.items():
            if value is not None:
                setattr(user, field, value)
        self.db.commit()
        self.db.refresh(user)
        return user
