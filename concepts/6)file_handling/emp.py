class Employee():
    def __init__(self, ename, estatus, eid):
        self.ename = ename
        self.estatus = estatus
        self.eid = eid
    def display(self):
        print(self.ename, self.estatus, self.eid)
