'''
Models representing Alternative, Expert and Task Data
'''


class Alternative:
    '''
    Alternative object. Has single field [name]
    '''

    def __init__(self, name) -> None:
        self.name = name


class Expert:
    '''
    Expert objejct. Has [name -> str] and [grades -> list[int]]
    '''

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


class TaskData:
    '''
    TaskData object. Contains alternatives and experts
    '''

    def __init__(self, alternatives, experts):
        self.alternatives = alternatives
        self.experts = experts
