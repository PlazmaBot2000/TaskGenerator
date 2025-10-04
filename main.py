import random

#Parameters
questions_count = 3
obj_count = 5
questions = []
obj = []
actions = []

#Functions
def gen_obj():
    for i in range(obj_count):
        obj.append(chr(ord('@')+(i+1)) + ' ')
        actions.append("true")
        print(obj[i] + "is " + actions[i])

def gen_questions():
    obj_for_questions = obj
    for i in range(questions_count):

        index = random.randint(0, (len(obj_for_questions) - 1)) 
        if random.randint(1, 3) == 1:
            prefix = "is not "
        else:
            prefix = ""
        
        questions.append(obj_for_questions[index] + prefix + actions[index])
        obj_for_questions.pop(index)

        print(questions[i])

def gen_obj_act_pair():
    index = random.randint(0, obj_count - 1) 
    print(index)
    if random.randint(1, 3) == 1:
        prefix = "is not "
    else:
        prefix = "is "
        
    return obj[index] + prefix + actions[index]

#Main
print("Objects:")
gen_obj()
print("Правда ли что:")
gen_questions()
