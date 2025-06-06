def stringManipulationExercise():
    string = input("Enter a string : ")
    target = input("Enter a target string : ")
    print("The count of the target string in inputted string is " + str(string.lower().count(target)))

def listAndLoopExercise():
    list = []
    user_input = input("Enter numbers : ")
    list = [
        int(s.strip()) for s in user_input.split(' ') if s.strip()
    ]
    print(f'Original list : {list}')
    print("Numbers divisible by 5 : ")
    index = 0
    while index < len(list):
        if  list[index] % 5 == 0:
            print(list[index])
        index+=1

stringManipulationExercise()
listAndLoopExercise()
