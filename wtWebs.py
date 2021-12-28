import time

print("""
░██╗░░░░░░░██╗████████╗░██╗░░░░░░░██╗███████╗██████╗░░██████╗
░██║░░██╗░░██║╚══██╔══╝░██║░░██╗░░██║██╔════╝██╔══██╗██╔════╝
░╚██╗████╗██╔╝░░░██║░░░░╚██╗████╗██╔╝█████╗░░██████╦╝╚█████╗░
░░████╔═████║░░░░██║░░░░░████╔═████║░██╔══╝░░██╔══██╗░╚═══██╗
░░╚██╔╝░╚██╔╝░░░░██║░░░░░╚██╔╝░╚██╔╝░███████╗██████╦╝██████╔╝

       weakness of all small websites in the world.
""")

while True:
	i = 0
	pw = input("Password(hint: sm_l_w__kn__s): ")
	if pw == "smallweakness":
		web = input("Enter Website name(e.g www.website.com): ")
		print("searching website...")
		time.sleep(3)
		print("Force accessing website...")
		time.sleep(5)
		print("looking for weakness...")
		time.sleep(6)
		for i in range(1, 101, 1):
			print("hacking...", str(i) + "%")
			i += 1
			time.sleep(0.1)
		print("Website Hacked!")
		continue
	
	else:
		print("WRONG PASSWORD!")
		continue
