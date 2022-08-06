class user:
    def __init__(self):
        print("Use Class")
    
    def input(self):
        self.email=input("Enter email")
        self.password=input("Enter a Passwod")

class doctor(user):
    def doc_input(self):
        self.specification=input("Ente a specification")
    
    def display(self):
        print("Doctor Email= ",self.email)
        print("Doctor Password= ",self.password)
        print("Specification = ",self.specification)

class patient(user):
    def patient_input(self):
        self.specification=input("Ente a specification")
    
    def pat_display(self):
        print("Patient Email= ",self.email)
        print("Patient Password= ",self.password)
        print(" Patient Specification = ",self.specification)


note="""
1.doct
2.patient
"""
choice=int(input("enter a choice"))
if choice==1:
    doctor=doctor()
    doctor.input()
    doctor.doc_input()
    doctor.display()
elif choice==2:
    patient=patient()
    patient.input()
    patient.patient_input()
    patient.pat_display()