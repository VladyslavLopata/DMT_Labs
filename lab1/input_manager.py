from model import Alternative, Expert, TaskData


def get_task_data():
    exp1 = Expert(name = 'Vasia', grades=[1,2,3])
    exp2 = Expert(name = 'Petia', grades=[3,2,3])

    alt1 = Alternative(name='UWU')
    alt2 = Alternative(name='OWO')

    return TaskData(alternatives=[alt1, alt2], experts=[exp1, exp2])
