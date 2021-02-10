from lab1.model import Alternative, Expert, TaskData

freader = open('text.txt', 'r')

def input_method(question):
    return freader.readline()

def ask_alternatives():
    number = int(input_method('Введіть число альтернатив: '))
    alternatives = []
    for i in range(0, number):
        alternatives.append(Alternative(name = input_method(f"Введіть назву альтернативи {i+1}: ")))
    return alternatives

def ask_experts():
    number = int(input_method('Введіть число експертів: '))
    experts = []
    for i in range(0, number):
        experts.append(Expert(name = input_method(f"Введіть ім'я експерта {i+1}: "), grades=[]))
    return experts

def ask_grade_value():
    return int(input_method('Введіть максимальне значення оцінки: '))

def ask_dominance(experts, alternatives, grade_value):
    updated_experts = []
    for expert in experts:
        updated_expert = Expert(name = expert.name, grades=[])
        for alternative in alternatives:
            updated_expert.grades.append(input_method(f'Експерт {expert.name}, введіть оцінку альтернативи {alternative.name}: '))
        updated_experts.append(updated_expert)
    return updated_experts


def get_task_data():
    alternatives = ask_alternatives()
    experts = ask_experts()
    grade_value = ask_grade_value()
    experts = ask_dominance(experts, alternatives, grade_value)

    return TaskData(alternatives=alternatives, experts=experts)



