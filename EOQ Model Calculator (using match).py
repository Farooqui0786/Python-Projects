def main():
    # Get user input
    print("Select EOQ Model:")
    print("1. Model 1")
    print("2. Model 2")
    print("3. Model 3")
    choice = int(input("Enter choice (1-3): "))

    match choice:
        case 1:
            print("\nModel_1")
            lmd = float(input("Enter demand rate (units per year): "))
            A = float(input("Enter ordering cost per order: "))
            Ic = float(input("Enter holding cost per unit per year: "))
            
            # Calculate EOQ for Model 1
            EOQ1 = ((2 * A * lmd) / Ic) ** 0.5
            print(f"\nThe Economic Order Quantity (EOQ) is: {EOQ1:.2f} units")
        
        case 2:
            print("\nModel_2")
            lmd = float(input("Enter demand rate (units per year): "))
            A = float(input("Enter ordering cost per order: "))
            Ic = float(input("Enter holding cost per unit per year: "))
            Xi = float(input("Enter production rate: "))
            
            # Check if production rate is greater than demand rate
            if Xi <= lmd:
                print("ERROR, Demand should be less than production")
            else:
                # Calculate EOQ for Model 2
                EOQ2 = (((2 * A * lmd) / Ic) * (Xi / (Xi - lmd))) ** 0.5
                print(f"\nThe Economic Order Quantity (EOQ) is: {EOQ2:.2f} units")
        
        case 3:
            print("\nModel_3")
            lmd = float(input("Enter demand rate (units per year): "))
            A = float(input("Enter ordering cost per order: "))
            Ic = float(input("Enter holding cost per unit per year: "))
            Pi = float(input("Enter shortage cost per cycle per unit time: "))
            
            # Calculate EOQ for Model 3
            EOQ3 = (((2 * A * lmd) / Ic) * ((Ic + Pi) / Pi)) ** 0.5
            print(f"\nThe Economic Order Quantity (EOQ) is: {EOQ3:.2f} units")
        
        case _:
            print("Wrong Input")


if __name__ == "__main__":
    main()