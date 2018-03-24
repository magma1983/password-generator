import random

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
,'r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'
,'R','S','T','U','V','W','X','Y','Z']
nums = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['.','-','_','!','?']
pw = []
for i in range(2):
 pw.append(lowercase[random.randint(0,len(lowercase)-1)])
 pw.append(lowercase[random.randint(0,len(lowercase)-1)])
 pw.append(nums[random.randint(0,len(nums)-1)])
 pw.append(uppercase[random.randint(0,len(uppercase)-1)])
 pw.append(uppercase[random.randint(0,len(uppercase)-1)])
 pw.append(symbols[random.randint(0,len(symbols)-1)])
print(''.join(pw))
