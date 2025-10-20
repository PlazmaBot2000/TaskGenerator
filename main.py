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


def gen_conditions(statements_array, questions_array):
    result = []
    
    for i in questions_array:
        if random.randint(1,2) == 1 and len(statements_array) > 1:
            result.append(((statements_array.pop(random.randint(0, (len(statements_array) - 1))), random.choice([" и ", ", или "]), statements_array.pop(random.randint(0, (len(statements_array) - 1)))), (i[0],random.choice([" ", " не "]), i[2])))
        else:
            result.append(((statements_array.pop(random.randint(0, (len(statements_array) - 1))), '', ''), (i[0],random.choice([" ", " не "]), i[2])))
        statements_array.append(i)

    return result


def new_task():
    objects_and_actions = generate_from_file()

    statements = gen_pairs(objects_and_actions, config['statements_count'])
    questions = gen_pairs(objects_and_actions.copy(), config['questions_count'])
    random.shuffle(questions)
    conditions = gen_conditions(statements.copy(), questions.copy())

    for i in statements:
        print("  ", *i,sep="", end=".\n")

    random.shuffle(conditions)
    print()
    for i in conditions:
        print("  Если " + "".join(i[0][0]) + i[0][1] + "".join(i[0][2]) + ", то " + "".join(i[1]) + ".")

    print()
    for i in questions:
        print(" ", f"{i[1].replace(' ', '')} {i[2].replace(' ', '')}".lstrip().capitalize(), "ли", i[0].lower(), end="?\n")

#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|
for i in range(1, config['tasks_count'] + 1):
    print("\n=============== Вариант ", i, "===============")
    new_task()
