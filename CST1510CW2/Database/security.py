import bcrypt
from database.db_manager import DatabaseManager

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    )


def register_user(username: str, password: str, role: str) -> bool:
    db = DatabaseManager()

    existing = db.execute(
        "SELECT id FROM users WHERE username = ?",
        (username,),
        fetchone=True
    )

    if existing:
        return False

    password_hash = hash_password(password)

    db.execute(
        """
        INSERT INTO users (username, password_hash, role)
        VALUES (?, ?, ?)
        """,
        (username, password_hash, role),
        commit=True
    )

    return True


def authenticate_user(username: str, password: str):
    db = DatabaseManager()

    user = db.execute(
        """
        SELECT id, username, password_hash, role
        FROM users
        WHERE username = ?
        """,
        (username,),
        fetchone=True
    )

    if not user:
        return None

    user_id, uname, password_hash, role = user

    if verify_password(password, password_hash):
        return {
            "id": user_id,
            "username": uname,
            "role": role
        }

    return None
