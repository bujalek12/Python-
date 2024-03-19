from unittest import result
import datetime

def CreateFunctionWithWrapper_logtofile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args,**kwargs):
            file = open(logFilePath, 'a')
            file.write('Function {} started at {}\n'.format(func.__name__, datetime.datetime.now().isoformat()))
            file.write('following arguments were used:\n')
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k,v) for k,v in kwargs.items()))
            file.write("\n")
            result = func(*args,**kwargs)
            file.write('Function returned: {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_logtofile(r'C:\Users\48530\Desktop\visual\pomoc\change_salary_log.txt')
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print('Changing salary for {} to {}'.format(emp_name, new_salary))
    return new_salary  

@CreateFunctionWithWrapper_logtofile(r'C:\Users\48530\Desktop\visual\pomoc\change_position_log.txt')
def ChangePosition(emp_name, new_position):
    print('Changing position for {} to {}'.format(emp_name, new_position))
    return new_position
print(ChangeSalary('John', 10000,True))
print(ChangeSalary('John', 2000,is_bonus = True))
print(ChangePosition('John', 'Manager'))
print(ChangePosition('anke', 'manager'))
