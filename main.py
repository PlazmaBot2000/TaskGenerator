import random
import yaml

with open("config.yml", 'r') as cfg:
    config = yaml.load(cfg, Loader=yaml.SafeLoader)




#                                                        _____ _   _ _   _  ____ _____ ___ ___  _   _ ____  
#                                                       |  ___| | | | \ | |/ ___|_   _|_ _/ _ \| \ | / ___| 
#=======================================================| |_  | | | |  \| | |     | |  | | | | |  \| \___ \==========================================
#=======================================================|  _| | |_| | |\  | |___  | |  | | |_| | |\  |___) |=========================================
#                                                       |_|    \___/|_| \_|\____| |_| |___\___/|_| \_|____/ 
def generate_from_file():
 
    with open(config['objects_file_name'], 'r') as objects_file:
        objects_from_file = [item.strip() for item in objects_file.readlines()]
    with open(config['actions_file_name'], 'r') as actions_file:
        actions_from_file = [item.strip() for item in actions_file.readlines()]

    result_array = []

    for _ in range(config['objects_count']):
        result_array.append(([objects_from_file.pop(random.randint(0, (len(objects_from_file) - 1))), ' ', actions_from_file.pop(random.randint(0, (len(actions_from_file) - 1)))]))
        
    return result_array



def gen_pairs(pairs_array, count):

    result_array = []

    for _ in range(count):
        index = random.randint(0, (len(pairs_array) - 1))
        result_array.append((pairs_array[index][0], random.choice([" ", " не "]), pairs_array.pop(index)[2]))

    return result_array


def gen_condition(statements_array):

    if random.randint(1,2) == 1 and len(statements_array) > 1:
        return (statements_array.pop(random.randint(0, (len(statements_array) - 1))), random.choice([" и ", " или "]), statements_array.pop(random.randint(0, (len(statements_array) - 1))))
    else:
        return (statements_array.pop(random.randint(0, (len(statements_array) - 1))), '', '')


def print_pairs(a):
    for i in a:
        print("  " + i[0] + i[1] + i[2])
    print()




def new_task():
    objects_and_actions = generate_from_file() 
    statements = gen_pairs(objects_and_actions.copy(), config['statements_count'])
    questions = gen_pairs(objects_and_actions.copy(), config['questions_count'])

    print("Утверждения:")
    print_pairs(statements)
    print(gen_condition(statements.copy()))
    print("Правда ли что:")
    print_pairs(questions)

#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|
for i in range(1, config['tasks_count'] + 1):
    print('Вариант ', i)
    new_task()
