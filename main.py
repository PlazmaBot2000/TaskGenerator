import random

#Parameters
    #Comment: questions_count should be < than obj_count
    #Comment: statements_count should be < than obj_count
statements_count = 2
questions_count = 3
obj_count = 5
    #Comment: files should be not empty
objects_file_name = "objects.txt"
actions_file_name = "actions.txt"

obj = []
actions = []
questions = []
statements = []
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



def print_array_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(len(result)):
            print(result[i])
        
        return result
    return wrapper



#                                                        _____ _   _ _   _  ____ _____ ___ ___  _   _ ____  
#                                                       |  ___| | | | \ | |/ ___|_   _|_ _/ _ \| \ | / ___| 
#=======================================================| |_  | | | |  \| | |     | |  | | | | |  \| \___ \==========================================
#=======================================================|  _| | |_| | |\  | |___  | |  | | |_| | |\  |___) |=========================================
#                                                       |_|    \___/|_| \_|\____| |_| |___\___/|_| \_|____/ 

#@print_array_decorator
def readfile_to_array(data):
    with open(data, 'r') as file:
        lines = file.readlines()
        processed_data = [item.strip() for item in lines]
    return processed_data




#@print_array_decorator
def gen_obj():
    obj_for_generation = readfile_to_array(objects_file_name)
    for i in range(obj_count):
        index = random.randint(0, (len(obj_for_generation) - 1)) 
        obj.append(obj_for_generation[index])
        obj_for_generation.pop(index)
    return obj


#@print_array_decorator
def gen_actions():
    actions_for_generation = readfile_to_array(actions_file_name)
    for i in range(obj_count):
        index = random.randint(0, (len(actions_for_generation) - 1)) 
        actions.append(actions_for_generation[index])
        actions_for_generation.pop(index)
    return actions



@print_array_decorator
def gen_questions():
    obj_for_questions = obj.copy()
    actions_for_questions = actions.copy()
    for i in range(questions_count):

        index = random.randint(0, (len(obj_for_questions) - 1)) 
        if random.randint(1, 3) == 1:
            prefix = " is not "
        else:
            prefix = " "
        
        questions.append(obj_for_questions[index] + prefix + actions_for_questions[index])
        obj_for_questions.pop(index)
        actions_for_questions.pop(index)

    return questions



@print_array_decorator
def gen_statements():
    obj_for_statements = obj.copy()
    actions_for_statements = actions.copy()
    for i in range(statements_count):

        index = random.randint(0, (len(obj_for_statements) - 1)) 
        if random.randint(1, 2) == 1:
            prefix = " is not "
        else:
            prefix = " "
        
        statements.append(obj_for_statements[index] + prefix + actions_for_statements[index])
        obj_for_statements.pop(index)
        actions_for_statements.pop(index)
    return statements
    





#                                                                __  __    _    ___ _   _ 
#                                                               |  \/  |  / \  |_ _| \ | |
#===============================================================| |\/| | / _ \  | ||  \| |===========================================================
#===============================================================| |  | |/ ___ \ | || |\  |===========================================================
#                                                               |_|  |_/_/   \_\___|_| \_|
gen_obj()
gen_actions()
print("Утверждения:")
gen_statements()
print("Правда ли что:")
gen_questions()
