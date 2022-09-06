class SingleAddress:
    def __init__(self,firstname, lastname,  streetaddress, city, state, country, postalcode):
        self.firstname=firstname
        self.lastname = lastname
        self.streetaddress=streetaddress
        self.city=city
        self.state=state
        self.country=country
        self.postalcode=postalcode

    def addres(self):
        return self.firstname+" "+self.lastname+" "+self.streetaddress+" "+self.city+" "+self.state+" "+self.country+" "+self.postalcode

addr1=SingleAddress("naveen","kumar","j.p nagar","bangalore","karnataka","India","560068")
aadr2=SingleAddress("yeshwanth","p","bannerghatta","bangalore","karnataka","India","560068")

