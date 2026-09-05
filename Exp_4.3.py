#Safe Division Kiosk
def divide_money():
        print("-----Banking Kiosk:Split Bill-----")
        while True:
                try:
                        total=float(input("Enter total amount:"))
                        people=int(input("Enter number of people:"))
                        
                        per_p=total/people
                        print(f"Each person pays:{per_p:.2f}")
                        break
                
                except ZeroDivisionError:
                        print("ERROR:You cannot divide by zero people!")
                except ValueError:
                        print("Error:Please enter numberss only!")
                        
divide_money()