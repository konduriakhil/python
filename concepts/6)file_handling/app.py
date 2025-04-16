import sys
sys.path.append("C:\\Users\\kondu\\OneDrive\\Desktop\\python\\concepts\\6)file_handling")
import emp
import pickle


# class Employee():
#     def __init__(self, ename, estatus, eid):
#         self.ename = ename
#         self.estatus = estatus
#         self.eid = eid
#     def display(self):
#         print(self.ename, self.estatus, self.eid)


with open('emd.dat', 'rb') as f:
    print('Employee details are: ')
    while True:
        try:
            obj = pickle.load(f)
            obj.display()
        except EOFError:
            print('All employees are completed')
            break
        