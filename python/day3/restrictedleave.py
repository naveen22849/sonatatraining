from leave import Leave
class RestrictedLeave:
    def __init__(self, employeeid, name, leavebalance, Reasonforapplyingleave, DateOfBirth):
        self.eid = employeeid
        self.name = name
        self.lbalance = leavebalance
        self.rfal = Reasonforapplyingleave
        self.DOB = DateOfBirth

    def applyleave(self):
        return self.eid + " " + self.name + " " + self.lbalance + " " + self.rfal + " " + self.DOB


emp = RestrictedLeave("22849", "Naveen", "25", "Fever", "20/03/2000")
