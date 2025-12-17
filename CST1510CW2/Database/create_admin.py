from database.security import register_user


if __name__ == "__main__":
    success = register_user(
        username="admin",
        password="admin123",
        role="admin"
    )

    if success:
        print("Admin user created.")
    else:
        print("Admin user already exists.")
