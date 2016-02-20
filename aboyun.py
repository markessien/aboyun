print ("Welcome To Aboyun App")
print ("We are here to help you have a healthy pregnancy. :) ")
firsttrimester=["Nausea","Morning Sickness", "strange food cravings", "Unusual tiredness"]
secondtrimester=["swelling of feet or hands","dizziness","skin changes"]
thirdtrimester=["false labour contractions,back ache","bleeding"]

trimester=input("Enter your trimester?")
if trimester=="1":
	print("Congratulations! You are in your first trimester")
	print("You should be experiencing the following symptoms;" )
	print (firsttrimester)
elif trimester=="2":
	print("Way to go! You are in your second trimester")
	print("You should be experiencing the following symptoms;" )
	print(secondtrimester)
elif trimester=="3":
	print("You are in your third trimester. Baby's almost here")
	print("You should be experiencing the following symptoms;" )
	print(thirdtrimester)
else:
	print ("I'm not sure")
