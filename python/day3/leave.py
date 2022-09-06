class Leave:
    def __init__(self, employeeid, name, leavebalance):
        self.eid = employeeid
        self.name = name
        self.lbalance = leavebalance

    def applyleave(self):
        return self.eid + " " + self.name + " " + self.lbalance


emp = Leave("22849", "Naveen", "25")
