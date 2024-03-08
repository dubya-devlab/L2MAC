import hashlib


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()


def register_user(name, email, password):
    user = User(name, email, password)
    # Save user data securely


if __name__ == '__main__':
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    register_user(name, email, password)
    print('User registered successfully.')