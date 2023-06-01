import json


class Quiz:

    def __init__(self):
        self.points = 0

    def show_question(self, question):
        print()
        print(question["pytanie"])
        print("a:", question["a"])
        print("b:", question["b"])
        print("c:", question["c"])
        print("d:", question["d"])
        print()

        answer = input("Którą odpowiedź wybierasz? ")

        if answer == question["prawidlowa odpowiedz"]:
            self.points += 1
            print("To prawidłowa odpowiedź, brawo masz ", self.points, "punktów")

        else:
            print("To błędna odpowiedź, prawidłową odpowiedzią jest ", question["prawidlowa odpowiedz"])

    def quiz_main(self):
        with open(r"C:\Users\adamw\OneDrive\Pulpit\stary pi\Python\MiniProjekty\Quiz\quiz.json") as json_file:
            questions = json.load(json_file)

            for i in range(0, len(questions)):
                Quiz.show_question(self, questions[i])

        print("Uzyskałeś", self.points, "punktów")
