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
    with open(filename, 'r', encoding=config['encoding']) as file: return [item.strip() for item in file.readlines()]


def calc_ans(s, p, a1, a2):
    if s == 0:
        return abs(p - (a1 * a2))
    else: 
        return abs(p - min(1, a1 + a2))
    

def select_statement(usage_c, statements_a, res):
    print(len(statements_a) - 1)
    print(statements_a)
    print(usage_c)
    print(res)
    index = random.randint(0, (len(statements_a)) - 1)
    print(index) 
    print()
    if usage_c[index] == 1:
        del usage_c[index]
        return (statements_a.pop(index), index)
    else:
        usage_c[index] -= 1
        return (statements_a[index], index)

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
    result_pairs = []
    result_answers = []

    for _ in range(count):
        index = random.randint(0, (len(pairs_array) - 1))
        answer = random.randint(0, 1)
        result_answers.append(answer)
        result_pairs.append((pairs_array[index][0], [" не ", " "][answer], pairs_array.pop(index)[2]))

    return result_pairs, result_answers


def gen_conditions(statements_array, answers, questions_array):
    random.shuffle(questions_array)
    usage_count = [random.randint(config['reuse_count'][0], config['reuse_count'][1])] * len(statements_array)
    result = []
    sta = []

    for i in questions_array:
        cons_prefix = random.choice([0, 1])
        first = select_statement(usage_count, statements_array, result)
        if random.randint(1,100) <= config['and_or_percent'] and len(statements_array) > 1: 
            second = select_statement(usage_count, statements_array, result)
            while first[1] == second[1]:
                second = select_statement(usage_count, statements_array, result)
            spacer = random.choice([0, 1]) 
            result.append((first[0], [" и ", " или "][spacer] , second[0], (i[0], [" ", " не "][cons_prefix], i[2])))
            answers.append(calc_ans(spacer, cons_prefix, answers[first[1]], answers[second[1]]))
        else:

            result.append((first[0], '', ('')*3, (i[0], [" ", " не "][cons_prefix], i[2])))
            answers.append(calc_ans(0, cons_prefix, answers[first[1]], 1))

        statements_array.append(i)
        usage_count.append(random.randint(*config['reuse_count']))
    random.shuffle(result)
    return result, answers 


def new_task():
    objects_and_actions = get_from_file()
    statements, statements_answers = gen_pairs(objects_and_actions, config['statements_count'])
    questions, qa = gen_pairs(objects_and_actions, config['questions_count'])
    extra_pairs, ea = gen_pairs(objects_and_actions, max(config['conditions_count'] - config['questions_count'], 0))
    conditions, ans = gen_conditions(statements.copy(), statements_answers, extra_pairs + questions.copy())

    for i in statements:
        print("  ", *i, sep="", end=".\n") 
  
    print()
    for i in conditions:
        print("  Если " + "".join(i[0]).lower() + i[1] + "".join(i[2]).lower() + ", то " + "".join(i[3]).lower() + ".")

    print()
    for i in questions:
        print(" ", (i[1].replace(" ", "")+" "+(i[2] + " ").replace(" ", " ли ", 1)).strip().capitalize(), i[0].lower(), end="?\n")

    print()
    n = 1
    print(ans)
    for i in ans[-config['questions_count']:]:
        print(i)
        print("  ", n, [". Нет", ". Да"][i], sep = '')
        n += 1
#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|
for i in range(1, config['tasks_count'] + 1):
    print("\n=============== Вариант ", i, "===============")
    new_task()
