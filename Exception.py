class AgeExceptions(Exception):
    
    
    def __init__(self, age, message="Age must be above 18 years to vote"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def chk_age_election(self):
        
        if self.age >= 18:
            print("You can cast your vote")
        else:
            raise AgeExceptions(self.age, self.message)

try:
    age = int(input("Kindly enter your age: "))
    age_check = AgeExceptions(age)
    age_check.chk_age_election()
except AgeExceptions as e:
    print(f"Custom Exception: {e}")


    

