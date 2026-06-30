class amount():
    
    def getvalues(self, bill):
        bill = int(input("enter your total bill: "))
        if bill > 1000:
            discount = bill * (15 / 100)
            print("you got a discount :", discount)
            return bill  
        else:
            print("you are not elegible for discount")
            return bill

    def calculate_gst(self):
        total_bill = self.getvalues(0) 
        gst1 = int(total_bill * (12 / 100))
        final_bill = total_bill + gst1
        print("your bill with gst is ", final_bill)
        return final_bill

d = amount()
d.calculate_gst()