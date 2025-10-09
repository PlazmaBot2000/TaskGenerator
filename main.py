import random
import yaml

class object_pair:
    def __init__(self, object, prefix, action):
        self.object = object
        self.prefix = prefix
        self.action = action
    def view(self):
        return self.object + self.prefix + self.action

with open("config.yml", 'r') as cfg:
    config = yaml.load(cfg, Loader=yaml.SafeLoader)




#                                                        _____ _   _ _   _  ____ _____ ___ ___  _   _ ____  
#                                                       |  ___| | | | \ | |/ ___|_   _|_ _/ _ \| \ | / ___| 
#=======================================================| |_  | | | |  \| | |     | |  | | | | |  \| \___ \==========================================
#=======================================================|  _| | |_| | |\  | |___  | |  | | |_| | |\  |___) |=========================================
#                                                       |_|    \___/|_| \_|\____| |_| |___\___/|_| \_|____/ 

def print_pairs_array(a):
    for i in range(len(a)):
        print("  " + a[i].view())
    print()


def generate_from_file(objects_file_name, actions_file_name, count):

    result_array = []

    with open(objects_file_name, 'r') as obj_file:
        lines = obj_file.readlines()
        obj_for_generation = [item.strip() for item in lines]
    with open(actions_file_name, 'r') as actions_file:
        lines = actions_file.readlines()
        actions_for_generation = [item.strip() for item in lines]

    for _ in range(count):
        obj_index = random.randint(0, (len(obj_for_generation) - 1)) 
        actions_index = random.randint(0, (len(actions_for_generation) - 1)) 

        result_array.append(object_pair(obj_for_generation[obj_index], ' ', actions_for_generation[actions_index]))
        obj_for_generation.pop(obj_index)
        actions_for_generation.pop(actions_index)
    return result_array


def gen_pairs(objects_and_actions_array, count):
    result_array = []

    for _ in range(count):
        index = random.randint(0, (len(objects_and_actions_array) - 1))
        if random.randint(1, 3) == 1:
            objects_and_actions_array[index].prefix = " не "
        else:
            objects_and_actions_array[index].prefix = " "

        result_array.append(objects_and_actions_array[index])
        objects_and_actions_array.pop(index)
    return result_array


def new_task():
    objects_and_actions = generate_from_file(config['objects_file_name'], config['actions_file_name'], config['objects_count']) 
    statements = gen_pairs(objects_and_actions.copy(), config['statements_count'])
    questions = gen_pairs(objects_and_actions.copy(), config['questions_count'])
    print("Утверждения:")
    print_pairs_array(statements)
    print("Правда ли что:")
    print_pairs_array(questions)

#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|

for i in range(1, config['tasks_count']):
    print('Вариант ', i)
    new_task()
