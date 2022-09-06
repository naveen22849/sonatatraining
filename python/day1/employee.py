class employee:
    def __init__(self, fname, lname, address):
        self.firstname=fname
        self.lastname=lname
        self.address=address

    def getfullname(self):
        return self.firstname[0]+ " " +self.lastname[0]+ " "+ self.address

    def address(self):
        return self.address


address=["Bengalore","JP Nagar"]
emp=employee("naveen","kumar",str(address))
print(emp.getfullname())

