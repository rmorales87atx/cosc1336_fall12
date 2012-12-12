# COSC 1336, Lab 12, Problem 1
# Robert Morales

class Employee:
    def __init__(self, name, idnum, dept, title):
        self.__name = name
        self.__idnum = idnum
        self.__dept = dept
        self.__title = title

    def dept(self):
        return self.__dept

    def __str__(self):
        return "{:<20} {:<7} {:<20} {:<20}".format(self.__name, self.__idnum,
                                                   self.__dept,  self.__title)

def main():
    data = [Employee('Mark Jones', 39119, 'IT', 'Programmer'),
            Employee('Arielle Lopez', 21345, 'IT', 'System Administrator'),
            Employee('Susan Meyers', 47899, 'Accounting', 'Vice President'),
            Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer'),
            Employee('Sirin Safar', 52341, 'Accounting', 'CPA')]

    dept = input("Enter a department (or blank to quit): ")
    while dept != "":
        results = [emp for emp in data if dept.lower() == emp.dept().lower()]

        if len(results) > 0:
            for emp in results:
                print(emp)
        else:
            print("No results.")

        print()
        dept = input("Enter a department (or blank to quit): ").lower()

main()
