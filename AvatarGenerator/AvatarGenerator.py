import random
import requests


class AvatarGenerator:

    @staticmethod
    def avatar_generator():
        response = requests.get(f"https://avatars.dicebear.com/api/male/{random.random()}.svg")

        # file = open("avatar.svg", "wb")
        # file.write(response.content)
        # file.close()
        # w starym pythonie trzeba było zamknąć plik txt
        # w nowym:
        with open("avatar.svg", "wb") as file:
            file.write(response.content)
