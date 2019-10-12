import math
Dict1={"H":"Hydrogen", "C":"Carbon", "N":"Nitrogen", "O":"Oxygen", "P":"Phosphorous", "S":"Sulfur"}
names=["H", "C", "N", "O", "P", "S"]
masses=[1.00794, 12.0107, 14.00674, 15.9994, 30.973761, 32.066]
molemass="HCNOPS"
for i in range(len(molemass)):
    Dict1[names[i]]=masses[i]
print(Dict1)