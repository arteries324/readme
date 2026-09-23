class lab:
    def __init__(self,room):
        self.room=room
class tech:
    def __init__(self,name):
        self.name=name
        self.lab=None
    def assign_lab(self,lab):
        self.lab=lab
if __name__=="__main__":
    chem=lab("302")
    tch=tech("Mr. Cruz")
    tch.assign_lab(chem)
    print("Technician:",tch.name)
    print("Assigned room:",tch.lab.room)