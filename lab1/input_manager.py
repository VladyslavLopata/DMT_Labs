from lab1.model import Alternative, Expert, TaskData


def ask_alternatives():
    number = int(input('Введіть число альтернатив: '))
    alternatives = []
    for i in range(0, number):
        alternatives.append(Alternative(name = input(f"Введіть назву альтернативи {i}: ")))
    return alternatives

def ask_experts():
    number = int(input('Введіть число експертів: '))
    experts = []
    for i in range(0, number):
        experts.append(Expert(name = input(f"Введіть ім'я експерта {i}: "), grades=[]))
    return experts

def ask_grade_value():
    return int(input('Введіть максимальне значення оцінки: '))

def ask_dominance(experts, alternatives, grade_value):
    for expert in experts:
        expert.grades = []
        for alternative in alternatives:
            expert.grades.append(input(f'Експерт {expert.name}, введіть оцінку альтернативи {alternative.name}: '))


def get_task_data():
    alternatives = ask_alternatives()
    experts = ask_experts()
    grade_value = ask_grade_value()
    experts = ask_dominance(experts, alternatives, grade_value)

    return TaskData(alternatives=alternatives, experts=experts)



