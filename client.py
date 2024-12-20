from game_result import GameResult

from game import Game
from game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f'Questions asked: {result.questions_passed}. Mistakes made:{result.mistakes_made}')
    print(f"You won!" if result.won else "You lost!")

game = Game("C:/Users/User29/Desktop/MacrosAutocad/КотЗина/Pop Cat icons/[Илья Фофанов] Полное руководство по Python 3 от новичка до специалиста (2020)/9. Движемся дальше/True_or_False/data/11.1 Questions.csv.csv", end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:

    q = game.get_next_question()
    print("Do you believe in the next statement or question? Enter 'y' or 'n'")
    print(q.text)

    answer = input()=="y"

    if q.is_true == answer:
        print("Good job! You`re right!")
    else:
        print("Oops, actually you`re mistaken. Here is the explanation:")
        print(q.explanation)

    game.give_answer(answer)
