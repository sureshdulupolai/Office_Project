Company_Pin = input('Enter Company Area Pin : ').upper()
# 7 Number
Company_Code = input("Enter Company Code : ")
CC = ''
for CC_Check in Company_Code:
    if CC_Check != ' ':
        CC += CC_Check

lstOfCompanyCodeOffice = ['AND1012890', 'BOR8970768', 'DR09009267']

if Company_Pin:
    if len(CC) >= 7:
        CPCC = Company_Pin + CC
        C1 = 0
        for CCO in lstOfCompanyCodeOffice:
            if CPCC == CCO:
                C1 += 1
                break
            else:
                continue
        
        if C1 == 0:
            print("You Can Keep Company Code : {}".format(CPCC))
        else:
            print("Company Code is Already Exist")
    else:
        print("Len of Company Code is More Then 6 Digit")
else:
    print("Enter proper Company Area Pin")