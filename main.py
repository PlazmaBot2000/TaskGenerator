import random
import yaml

with open("config.yml", 'r') as cfg:
    config = yaml.load(cfg, Loader=yaml.SafeLoader)



#                                                      ____  _____ ____ ___  ____      _  _____ ___  ____  ____  
#                                                     |  _ \| ____/ ___/ _ \|  _ \    / \|_   _/ _ \|  _ \/ ___| 
#=====================================================| | | |  _|| |  | | | | |_) |  / _ \ | || | | | |_) \___ \====================================
#=====================================================| |_| | |__| |__| |_| |  _ <  / ___ \| || |_| |  _ < ___) |===================================
#                                                     |____/|_____\____\___/|_| \_\/_/   \_\_| \___/|_| \_\____/ 



def print_result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper



#                                                        _____ _   _ _   _  ____ _____ ___ ___  _   _ ____  
#                                                       |  ___| | | | \ | |/ ___|_   _|_ _/ _ \| \ | / ___| 
#=======================================================| |_  | | | |  \| | |     | |  | | | | |  \| \___ \==========================================
#=======================================================|  _| | |_| | |\  | |___  | |  | | |_| | |\  |___) |=========================================
#                                                       |_|    \___/|_| \_|\____| |_| |___\___/|_| \_|____/ 



def print_array(A):
    for i in range(len(A)):
        print("  " + A[i])
    print()



#@print_result_decorator
def generate_from_file(file_name, count):
    result_array = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        items_for_generation = [item.strip() for item in lines]

    for i in range(count):
        index = random.randint(0, (len(items_for_generation) - 1)) 
        result_array.append(items_for_generation[index])
        items_for_generation.pop(index)
    return result_array
    


#@print_result_decorator
def gen_pairs(object_for_generation, actions_for_generation, count):
    obj_for_result = object_for_generation.copy()
    actions_for_result = actions_for_generation.copy()
    result_array = []
    for i in range(count):

        index = random.randint(0, (len(obj_for_result) - 1)) 
        if random.randint(1, 3) == 1:
            prefix = " не "
        else:
            prefix = " "
        
        result_array.append(obj_for_result[index] + prefix + actions_for_result[index])
        obj_for_result.pop(index)
        actions_for_result.pop(index)

    return result_array


def new_task():
    obj = generate_from_file(config['objects_file_name'], config['objects_count'])
    actions = generate_from_file(config['actions_file_name'], config['objects_count'])

    print("Утверждения:")
    print_array(gen_pairs(obj, actions, config['statements_count']))
    print("Правда ли что:")
    print_array(gen_pairs(obj, actions,  config['questions_count']))
#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|
for i in range(1, config['tasks_count']):
    print('Вариант ', i)
    new_task()
