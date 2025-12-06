import bcrypt
import os
import json
from datetime import datetime

class AuthenticationSystem:
    """User Authentication System Class"""
    
    def __init__(self, data_file="users.json"):
        """
        Initialize authentication system
        
        Args:
            data_file (str): User data storage file path
        """
        self.data_file = data_file
        self.users = {}
        self.valid_roles = ["cybersecurity", "data_science", "it_operations", "admin"]
        
        # Load existing users if data file exists
        if os.path.exists(data_file):
            self._load_users()
        else:
            print(f"Creating new user database: {data_file}")
            self._save_users()
    
    def _load_users(self):
        """Load user database JSON from file"""
        try:
            with open(self.data_file, 'r') as f:
                users_data = json.load(f)
                self.users = users_data
            print(f"Loaded {len(self.users)} users from {self.data_file}")
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Warning: Could not load users from {self.data_file}. Starting with empty database.")
            self.users = {}
    
    def _save_users(self):
        """Save user data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            print(f"Error saving users: {e}")
    
    def hash_password(self, password):
        """
        Hash password
        
        Args:
            password (str): Plain text password
            
        Returns:
            str: Hashed password
        """
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, plain_password, hashed_password):
        """
        Verify password
        
        Args:
            plain_password (str): Input plain text password
            hashed_password (str): Stored hashed password
            
        Returns:
            bool: Whether password matches
        """
        try:
            password_bytes = plain_password.encode('utf-8')
            hashed_bytes = hashed_password.encode('utf-8')
            return bcrypt.checkpw(password_bytes, hashed_bytes)
        except Exception as e:
            print(f"Error verifying password: {e}")
            return False
    
    def register_user(self, username, password, role="cybersecurity"):
        """
        Register new user
        
        Args:
            username (str): Username
            password (str): Password
            role (str): User role
            
        Returns:
            bool: Whether registration was successful
        """
        # Input validation
        if not username or not password:
            print("Error: Username and password cannot be empty.")
            return False
        
        if username in self.users:
            print(f"Error: Username '{username}' already exists.")
            return False
        
        if role not in self.valid_roles:
            print(f"Error: Invalid role. Valid roles are: {', '.join(self.valid_roles)}")
            return False
        
        # Hash password and create user
        hashed_password = self.hash_password(password)
        
        self.users[username] = {
            "password_hash": hashed_password,
            "role": role,
            "created_at": datetime.now().isoformat(),
            "last_login": None
        }
        
        # Save to file
        self._save_users()
        print(f"User '{username}' with role '{role}' registered successfully!")
        return True
    
    def login_user(self, username, password):
        """
        User login
        
        Args:
            username (str): Username
            password (str): Password
            
        Returns:
            tuple: (success, user_data) or (False, None)
        """
        if username not in self.users:
            print(f"Error: User '{username}' not found.")
            return False, None
        
        stored_hash = self.users[username]["password_hash"]
        
        if self.verify_password(password, stored_hash):
            # Update last login time
            self.users[username]["last_login"] = datetime.now().isoformat()
            self._save_users()
            
            user_data = {
                "username": username,
                "role": self.users[username]["role"],
                "created_at": self.users[username]["created_at"]
            }
            print(f"Login successful! Welcome {username} ({self.users[username]['role']})")
            return True, user_data
        else:
            print("Error: Invalid password.")
            return False, None
    
    def list_users(self):
        """List all users (admin function)"""
        print("\n=== Registered Users ===")
        for username, data in self.users.items():
            print(f"Username: {username}")
            print(f"  Role: {data['role']}")
            print(f"  Created: {data['created_at']}")
            if data['last_login']:
                print(f"  Last Login: {data['last_login']}")
            print("-" * 30)
    
    def delete_user(self, username):
        """
        Delete user (admin function)
        
        Args:
            username (str): Username to delete
            
        Returns:
            bool: Whether deletion was successful
        """
        if username not in self.users:
            print(f"Error: User '{username}' not found.")
            return False
        
        del self.users[username]
        self._save_users()
        print(f"User '{username}' deleted successfully.")
        return True


def command_line_interface():
    """Command Line Interface"""
    auth_system = AuthenticationSystem()
    
    print("=" * 50)
    print("MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("Authentication System - Week 7 Implementation")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Register new user")
        print("2. Login")
        print("3. List all users (admin only)")
        print("4. Delete user (admin only)")
        print("5. Test password hashing")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Register New User ---")
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            print("\nAvailable roles:")
            print("1. Cybersecurity Analyst")
            print("2. Data Scientist")
            print("3. IT Administrator")
            print("4. Admin")
            
            role_choice = input("Select role (1-4): ").strip()
            role_map = {
                "1": "cybersecurity",
                "2": "data_science",
                "3": "it_operations",
                "4": "admin"
            }
            
            role = role_map.get(role_choice, "cybersecurity")
            auth_system.register_user(username, password, role)
        
        elif choice == "2":
            print("\n--- Login ---")
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            success, user_data = auth_system.login_user(username, password)
            if success:
                print(f"\nLogin successful! Dashboard access granted for {user_data['role']}.")
        
        elif choice == "3":
            print("\n--- List All Users ---")
            auth_system.list_users()
        
        elif choice == "4":
            print("\n--- Delete User ---")
            username = input("Username to delete: ").strip()
            auth_system.delete_user(username)
        
        elif choice == "5":
            print("\n--- Test Password Hashing ---")
            test_password = input("Enter password to hash: ").strip()
            hashed = auth_system.hash_password(test_password)
            print(f"Original: {test_password}")
            print(f"Hashed: {hashed}")
            print(f"Hash length: {len(hashed)} characters")
            
            # Test verification
            verify_pass = input("\nEnter password to verify: ").strip()
            is_valid = auth_system.verify_password(verify_pass, hashed)
            print(f"Password match: {is_valid}")
        
        elif choice == "6":
            print("\nExiting authentication system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-6.")


if __name__ == "__main__":
    # Run command line interface
    command_line_interface()