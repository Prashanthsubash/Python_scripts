class Bank_details:
    
    def __init__(self,Acc_number,Acc_name,Acc_type):
        self.Acc_number= Acc_number
        self.Acc_name= Acc_name
        self.Acc_type= Acc_type
    
    def display_info(self):
        print(f"Bank_details: Acc_number: {self.Acc_number}, Acc_name:{self.Acc_name}, Acc_type {self.Acc_type}")

My_Bank_details = Bank_details(123456,"Prashanth","Savings")
My_Bank_details.display_info()