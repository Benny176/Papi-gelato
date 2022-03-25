import time



def stap3A():
	inp1 = input("Hier is uw hoorntje met {} bolletje(s). Wilt u nog meer bestellen? (Y/N)".format(hoeveel).lower())
	if inp1 == "Y":
		mainnn()
	else:
		print("Bedankt en tot ziens!")

def stap3B():
	inp = input("Hier is uw bakje met {} bolletje(s). Wilt u nog meer bestellen? (Y/N)".format(hoeveel).lower())
	if inp == "Y":
		mainnn()
	else:
		print("Bedankt en tot ziens!")
		quit()


def Stap2():
	met = input("Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje?".format(hoeveel).lower())
	if met == "a":
		stap3A()
	elif met == "b":
		stap3B()
	else:
		print("Sorry, dat snap ik niet...")
		Stap2()


def stap1():

	print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n')

	time.sleep(1)

	Stap2()

hoeveel = int(input('Hoeveel bolletjes wilt u?\n'))

def mainnn():
	print("Welkom bij Papi Gelato")
	if hoeveel < 4:
		for i in range(1,hoeveel+1):
			kk = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
		Stap2()
	elif hoeveel >5:
		if hoeveel <9:
			print("Dan krijgt u van mij een bakje met {} bolletjes".format(hoeveel))
			for i in range(1,hoeveel+1):
				kk = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
				Stap2()
	elif hoeveel >9:
		print("Sorry, zulke grote bakken hebben we niet")
	else:
		print("Sorry, dat snap ik niet...")
mainnn()

def bon():
	print("----------[Papi Gelato}-----------")
	

	
