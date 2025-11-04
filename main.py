import random
import yaml
import sys

with open("config.yml", 'r') as cfg: config = yaml.load(cfg, Loader=yaml.SafeLoader)
if config['output_file_name'] != "": sys.stdout = open(config['output_file_name'], 'w', encoding='utf-8')


#                                                        _____ _   _ _   _  ____ _____ ___ ___  _   _ ____  
#                                                       |  ___| | | | \ | |/ ___|_   _|_ _/ _ \| \ | / ___| 
#=======================================================| |_  | | | |  \| | |     | |  | | | | |  \| \___ \==========================================
#=======================================================|  _| | |_| | |\  | |___  | |  | | |_| | |\  |___) |=========================================
#                                                       |_|    \___/|_| \_|\____| |_| |___\___/|_| \_|____/ 

def file_to_array(filename):
    with open(filename, 'r') as file: return [item.strip() for item in file.readlines()]

def generate_from_file():
 
    objects_from_file, actions_from_file = file_to_array(config['objects_file_name']), file_to_array(config['actions_file_name'])

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


def select_statement(usage_count, statements_array):
    index = random.randint(0, (len(statements_array) - 1))
    if usage_count[index] == 1:
        del usage_count[index]
        return statements_array.pop(index)
    else:
        usage_count[index] -= 1
        return statements_array[index]


def gen_conditions(statements_array, questions_array):
    result = []
    usage_count = [random.randint(config['reuse_count'][0], config['reuse_count'][1])] * len(statements_array)

    for i in questions_array:
        if random.choice([True, False]) and len(statements_array) > 1: 
            result.append((select_statement(usage_count, statements_array), random.choice([" и ", ", или "]), select_statement(usage_count, statements_array), (i[0],random.choice([" ", " не "]), i[2])))
        else:
            result.append((select_statement(usage_count, statements_array), '', ('', '', ''), (i[0],random.choice([" ", " не "]), i[2])))

        statements_array.append(i)
        usage_count.append(random.randint(config['reuse_count'][0], config['reuse_count'][1]))
 
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
        print("  Если " + "".join(i[0]).lower() + i[1] + "".join(i[2]).lower() + ", то " + "".join(i[3]).lower() + ".")

    print()
    for i in questions:
        print(" ", (i[1].replace(" ", "")+" "+(i[2] + " ").replace(" ", " ли ", 1)).lstrip().rstrip().capitalize(), i[0].lower(), end="?\n")
#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|
for i in range(1, config['tasks_count'] + 1):
    print("\n=============== Вариант ", i, "===============")
    new_task()
