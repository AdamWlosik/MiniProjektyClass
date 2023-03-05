import random
import string
import sys


class PasswordGenerator:

    def __init__(self):
        self.password = []
        self.password_length = int(input("Jak długie ma być hasło? "))
        self.characters_left = None

    def update_characters_left(self, number_of_characters):

        if number_of_characters > self.characters_left or number_of_characters < 0:
            print("Liczba znaków z poza przedziału 0, .", self.characters_left)
            sys.exit(0)
        else:
            print("jestem")
            self.characters_left = self.characters_left - number_of_characters
            print("Pozostało znaków: ", self.characters_left)

    def main_generator_hasel(self):

        if self.password_length < 5:
            print("Hasło musi ieć minimum 5 znaków, spróbuje jeszcze raz.")
            sys.exit(0)
        else:
            self.characters_left = self.password_length

        lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
        PasswordGenerator.update_characters_left(self, lowercase_letters)

        uppercase_letter = int(input("Ile dużych liter ma mieć hasło? "))
        PasswordGenerator.update_characters_left(self, uppercase_letter)

        special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
        PasswordGenerator.update_characters_left(self, special_characters)

        digits = int(input("Ile cyfr ma mieć hasło? "))
        PasswordGenerator.update_characters_left(self, digits)

        if self.characters_left > 0:
            print("Nie wszystkie znaki zostały wykorzystane hasło zostanie uzupełnione małymi literami")
            lowercase_letters += self.characters_left

        print()
        print("Długość hasła: ", self.password_length)
        print("Małe litery: ", lowercase_letters)
        print("Duże litery: ", uppercase_letter)
        print("Znaki specjalne: ", special_characters)
        print("Cyfry: ", digits)

        for _ in range(self.password_length):
            if lowercase_letters > 0:
                self.password.append(random.choice(string.ascii_lowercase))
                lowercase_letters -= 1
            if uppercase_letter > 0:
                self.password.append(random.choice(string.ascii_uppercase))
                uppercase_letter -= 1
            if special_characters > 0:
                self.password.append(random.choice(string.punctuation))
                special_characters -= 1
            if digits > 0:
                self.password.append(random.choice(string.digits))
                digits -= 1

        random.shuffle(self.password)
        print("Wygenerowane hasło: ", "".join(self.password))
