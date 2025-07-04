def Model_1(A, lmd, Ic):
    EOQ1 = ((2 * A * lmd) / Ic) ** 0.5
    return EOQ1
    
def Model_2(A, lmd, Ic, Xi):
    EOQ2 = (((2 * A * lmd) / Ic) * (Xi / (Xi - lmd))) ** 0.5
    return EOQ2
    
def Model_3(A, lmd, Ic, Pi):
    EOQ3 = (((2 * A * lmd) / Ic) * ((Ic + Pi) / Pi)) ** 0.5
    return EOQ3


def main():
    # Get user input
    print("Select EOQ Model:")
    print("1. Model 1")
    print("2. Model 2")
    print("3. Model 3")
    choice = int(input("Enter choice (1-3): "))

    if choice == 1:
        print("\nModel_1")
        lmd = float(input("Enter demand rate (units per year): "))
        A = float(input("Enter ordering cost per order: "))
        Ic = float(input("Enter holding cost per unit per year: "))
        
        EOQ1 = Model_1(A, lmd, Ic)
        print(f"\nThe Economic Order Quantity (EOQ) is: {EOQ1:.2f} units")
    
    elif choice == 2:
        print("\nModel_2")
        lmd = float(input("Enter demand rate (units per year): "))
        A = float(input("Enter ordering cost per order: "))
        Ic = float(input("Enter holding cost per unit per year: "))
        Xi = float(input("Enter production rate: "))
        
        # Check if production rate is greater than demand rate
        if Xi <= lmd:
            print("ERROR, Demand should be less than production")
        else:
            EOQ2 = Model_2(A, lmd, Ic, Xi)
            print(f"\nThe Economic Order Quantity (EOQ) is: {EOQ2:.2f} units")
        
    elif choice == 3:
        print("\nModel_3")
        lmd = float(input("Enter demand rate (units per year): "))
        A = float(input("Enter ordering cost per order: "))
        Ic = float(input("Enter holding cost per unit per year: "))
        Pi = float(input("Enter shortage cost per cycle per unit time: "))
        
        EOQ3 = Model_3(A, lmd, Ic, Pi)
        print(f"\nThe Economic Order Quantity (EOQ) is: {EOQ3:.2f} units")
    else:
        print("Wrong Input")


if __name__ == "__main__":
    main()