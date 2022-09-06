from leave import Leave
class BasketOfLeave:
    def __init__(self, employeeid, name, leavebalance, Reasonforapplyingleave):
        self.eid = employeeid
        self.name = name
        self.lbalance = leavebalance
        self.rfal = Reasonforapplyingleave

    def applyleave(self):
        return self.eid + " " + self.name + " " + self.lbalance + " " + self.rfal


emp = BasketOfLeave("22849", "Naveen", "25", "Fever")
