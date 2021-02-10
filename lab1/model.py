class Alternative:
    def __init__(self, name) -> None:
        self.name = name

class Expert:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades

class TaskData:
    def __init__(self, alternatives, experts) -> None:
        self.alternatives = alternatives
        self.experts = experts