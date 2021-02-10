class Alternative:
    def __init__(self, name: str) -> None:
        self.name = name

class Expert:
    def __init__(self, name: str, grades: list[int]) -> None:
        self.name = name
        self.grades = grades

class TaskData:
    def __init__(self, alternatives: list[Alternative], experts: list[Expert]) -> None:
        self.alternatives = alternatives
        self.experts = experts