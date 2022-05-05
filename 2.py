long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
f = open("11.txt")  

line = f.readline()

# while line:
#     print(line)
#     line = f.readline()
#
#     data={"name":}
data = []
dict = {}
dict = {"name": line}
line = f.readline()
dict['lei'] = line
line = f.readline()
# dict={'lei':line}
liebiao5 = []
isin = []
sub_fund = {}
lin1=line
line = f.readline()
i=0
# print(dict)
while line:
    try:
        line = f.readline()
        if line[0] == "L" and line[1] == "U":
            isin.append(line)
            # print(isin)
        else:

            sub_fund['title'] = lin1
            lin1=line
            sub_fund["isin"] = isin

            isin = []
            # print(sub_fund)
    except:
        liebiao5.append(sub_fund)

        i=i+1

    sub_fund['title'] = lin1
    lin1 = line
    sub_fund["isin"] = isin
    liebiao5.append(sub_fund)

print(liebiao5)
f.close()


dict['sub_fund'] = liebiao5
print(dict)