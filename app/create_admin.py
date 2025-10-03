from sqlalchemy.orm import Session
from app.database import SessionLocal
from .models.user import User, UserRole
from .utils.auth import get_password_hash

def create_admin():
    """Create first admin user"""
    db = SessionLocal()
    try:
        admin_email = input("Enter admin email: ")
        admin_name = input("Enter admin name: ")
        admin_password = input("Enter admin password: ")
        
        # Check if admin exists
        existing = db.query(User).filter(User.email == admin_email).first()
        if existing:
            print(f"User with email {admin_email} already exists")
            return
        
        admin = User(
            name=admin_name,
            email=admin_email,
            password_hash=get_password_hash(admin_password),
            role=UserRole.ADMIN
        )
        db.add(admin)
        db.commit()
        print(f"Admin created successfully: {admin_email}")
    except Exception as e:
        print(f"Error creating admin: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()