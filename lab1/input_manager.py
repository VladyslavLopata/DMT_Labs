from lab1.model import Alternative, Expert, TaskData
import json

def get_task_data(json_data):

    experts = []
    for expert in json_data['experts']:
        experts.append(Expert(name=expert['name'], grades=expert['grades']))

    alternatives = []
    for alternative in json_data['alternatives']:
        alternatives.append(Alternative(name=alternative))

    return TaskData(alternatives=alternatives, experts=experts)



