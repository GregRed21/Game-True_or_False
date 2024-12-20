class GameResult:
    def __init__(self, total_questions: int, mistakes: int, is_winner: bool):
        self.total_questions = total_questions  # Общее количество вопросов
        self.mistakes = mistakes  # Количество ошибок
        self.is_winner = is_winner  # Статус победы или поражения

    def __str__(self):
        result = "Победа!" if self.is_winner else "Поражение."
        return (f"{result}\n"
                f"Всего вопросов: {self.total_questions}\n"
                f"Ошибки: {self.mistakes}\n")

    @property
    def questions_passed(self):
        return self.total_questions

    @property
    def mistakes_made(self):
        return self.mistakes

    @property
    def won(self):
        return self.is_winner
