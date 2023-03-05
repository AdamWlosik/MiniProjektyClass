import random
import string


class CommendPasswordGenerator:
    @staticmethod
    def main_generator_hasel_komenda():
        password_length = int(input("Jak długie ma być hasło? "))
        password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits)
                            for _ in range(password_length)])
        print(password)
