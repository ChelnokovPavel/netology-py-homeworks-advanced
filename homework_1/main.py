import datetime
from homework_1.application.salary import calculate_salary
from homework_1.application.people import get_employees

if __name__ == '__main__':
    print(datetime.datetime.now())
    calculate_salary()
    get_employees()
