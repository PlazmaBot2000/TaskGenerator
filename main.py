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


def select_statement(usage_c, statements_a):
    index = random.randint(0, (len(statements_a) - 1))
    if usage_c[index] == 1:
        del usage_c[index]
        return statements_a.pop(index)
    else:
        usage_c[index] -= 1
        return statements_a[index]


def subtract(l1, l2):
    result = []
    for i in l1:
        if not (i in l2):
            result.append(i)
    return result






def get_from_file(): 
    objects_from_file, actions_from_file = file_to_array(config['objects_file_name']), file_to_array(config['actions_file_name'])

    result_array = []

    for _ in range(config['objects_count']):
        f = lambda a: a.pop(random.randint(0, len(a) - 1))
        result_array.append([f(objects_from_file), ' ', f(actions_from_file)])
        
    return result_array


def gen_pairs(pairs_array, count):
    result_array = []

    for _ in range(count):
        index = random.randint(0, (len(pairs_array) - 1))
        result_array.append((pairs_array[index][0], random.choice([" ", " не "]), pairs_array.pop(index)[2]))

    return result_array


def gen_conditions(statements_array, questions_array):
    random.shuffle(questions_array)
    usage_count = [random.randint(config['reuse_count'][0], config['reuse_count'][1])] * len(statements_array)
    result = []

    for i in questions_array:
        if random.randint(0,1) and len(statements_array) > 1: 
            first, second = select_statement(usage_count, statements_array), select_statement(usage_count, statements_array)

            result.append((first, random.choice([" и ", " или "]), second if second != first else ('')*3, (i[0],random.choice([" ", " не "]), i[2])))
        else:
            result.append((select_statement(usage_count, statements_array), '', ('')*3, (i[0],random.choice([" ", " не "]), i[2])))

        statements_array.append(i)
        usage_count.append(random.randint(*config['reuse_count']))
    random.shuffle(result)
    return result


def new_task():
    objects_and_actions = get_from_file()
    statements, questions = gen_pairs(objects_and_actions, config['statements_count']), gen_pairs(objects_and_actions, config['questions_count'])
    extra_pairs = gen_pairs(objects_and_actions, max(config['conditions_count'] - config['questions_count'], 0))
    conditions = gen_conditions(statements.copy(), questions.copy() + extra_pairs)

    for i in statements:
        print("  ", *i, sep="", end=".\n")
 
    print()
    for i in conditions:
        print("  Если " + "".join(i[0]).lower() + i[1] + "".join(i[2]).lower() + ", то " + "".join(i[3]).lower() + ".")

    print()
    for i in questions:
        print(" ", (i[1].replace(" ", "")+" "+(i[2] + " ").replace(" ", " ли ", 1)).strip().capitalize(), i[0].lower(), end="?\n")
#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|
for i in range(1, config['tasks_count'] + 1):
    print("\n=============== Вариант ", i, "===============")
    new_task()
