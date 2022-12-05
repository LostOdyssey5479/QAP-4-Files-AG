#program for One Stop insurance company               By Alex Gillespie

import datetime

CustNum = 0
while True:
    ReqDate = datetime.datetime.now()
    CustFirName = input("What is your first name?: ").title()
    CustLastname = input("What is your last name?: ")
    CustAdd = input("What is your street address?: ")
    CustCity = input("What city do you live in?: ")
    CustPoCode = input("What is your postal code?: ")
    PhoNum = input("What is your phone number?: ")
    NumCars = input("How many cars will you be insuring today?: ")
    NumCars = int(NumCars)
    Liability = input("Would you like extra Liability coverage? Please respond with (Y/N): ").upper()
    GlassAns = input("Would you like glass coverage? Please respond with (Y/N): ").upper()
    LoanCarAns = input("Would you like an optional loaner car? please respond with (Y/N): ").upper()
    FullOrMon = input("Would you like to pay in full or monthly? Please respond with (F/M): ").upper()

    f = open("OSICDef.dat", "r")
    POLICY_NUM = int(f.readline())
    BASIC_RATE = float(f.readline())
    ADD_CAR_DIS = float(f.readline())
    EXT_LIAB = float(f.readline())
    GLASS_COV = float(f.readline())
    LOAN_CAR = float(f.readline())
    HST_RATE = float(f.readline())
    PROC_FEE_MON_PAY = float(f.readline())
    f.close()

    POLICY_NUM += 1
    g = open("Policies.dat", "a")
    g.write("{}".format(POLICY_NUM))
    g.write(", {}".format(CustFirName))
    g.write(", {}".format(CustLastname))
    g.write(", {}".format(CustAdd))
    g.write(", {}".format(CustCity))
    g.write(", {}".format(CustPoCode))
    g.write(", {}".format(PhoNum))
    g.write(", {}".format(NumCars))
    g.write(", {}".format(Liability))
    g.write(", {}".format(GlassAns))
    g.write(", {}".format(LoanCarAns))
    g.write(", {}".format(FullOrMon))

    if Liability == "Y":
        LiabPrint = "Yes"
        LiabilityCost = EXT_LIAB * NumCars
    else:
        LiabilityCost = 0
        LiabPrint = "No"

    if GlassAns == "Y":
        GlassCost = GLASS_COV * NumCars
        GlassPrint = "Yes"
    else:
        GlassCost = 0
        GlassPrint = "No"

    if LoanCarAns == "Y":
        LoanCarCost = LOAN_CAR * NumCars
        LoanPrint = "Yes"
    else:
        LoanCarCost = 0
        LoanPrint = "No"
    TotalExtra = LiabilityCost + GlassCost + LoanCarCost

    if NumCars > 1:
        TotCarsForDisc = (NumCars - 1)
        CarDisc = (TotCarsForDisc * BASIC_RATE) * ADD_CAR_DIS
        TotPrice = CarDisc + BASIC_RATE
    else:
        TotPrice = BASIC_RATE

    TotPricedsp = "${:,.2f}".format(TotPrice)
    TotInsPremium = TotPrice + TotalExtra
    TotInsPremiumHST = TotInsPremium * HST_RATE
    AltogetPrice = TotInsPremium + TotInsPremiumHST
    AltogetPricedsp = "${:,.2f}".format(AltogetPrice)

    if FullOrMon == "F":
        FullOrMonPrint = "Full"
        PaymentPrint = ""
    else:
        FullOrMonPrint = "Monthly"
        PaymentPrint = (TotInsPremiumHST + PROC_FEE_MON_PAY) / 8
        PaymentPrint = float(PaymentPrint)

    PaymentPrintdsp = "${:,.2f}".format(PaymentPrint)
    print("                          One Stop Insurance                 ")
    print("                           Company Receipt")
    print("="*64)
    print("")
    print(f"Customer Name: {CustFirName}            Customer Address: {CustAdd}")
    print(f"               {CustLastname}                             {CustCity}")
    print(f"Customer Phone:{PhoNum}        Customer Postal Code: {CustPoCode}  ")
    print("="*64)
    print(f"Number of Cars being insured: {NumCars}                  | {TotPricedsp} |")
    print(f"Liability Options?:                              | {LiabPrint} |")
    print(f"Glass Coverage?:                                 | {GlassPrint} |")
    print(f"Loan Car?:                                       | {LoanPrint} |")
    print("                                                 =================")
    print(f"Total:                                           | {AltogetPricedsp} |")
    print("="*64)
    print(f"Payment Method:                                  | {FullOrMonPrint} |")
    if FullOrMonPrint == "Monthly":
        print(f"Price per month:                                 | {PaymentPrintdsp} |")
    print("="*64)
    print(f"Date of admission: {ReqDate}")



    Answer = input("Would you like to create another policy? Please answer with (Y/N): ").upper()
    if Answer == "N":
        break