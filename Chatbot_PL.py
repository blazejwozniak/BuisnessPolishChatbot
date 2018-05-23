
import time
import unidecode
import re


#Baza danych słów-kluczy i odpowiedzi do nich

Przywitanie = ["witam", "czesc", "hej", "hey", "elo", "bry","siema", "siemano","hejka" ]
Odp_Przywitanie = "Dzień dobry"

Nastroj = ["humor", "slychac","samopoczucie", "czujesz"]
Odp_Nastroj = "Wszystko w porządku, dziękuję"

Godziny_Otwarcia = ["otwarty","otwarcie","czynne","czynny","godzinach","godzinie","otwarcia"]
Odp_Godziny_Otwarcia = "Szczegółowe rozpiski dotyczące godzin otwarcia i zamknięcia naszej firmy znajdują się w zakładce Godziny Otwarcia. (www.nazwafirmy.pl/Godziny_Otwarcia)"

Cennik = ["koszt", "cena","drogo","ceny","kosztuje","cene","cennik"]
Odp_Cennik = "Wszystkie koszty naszych usłóg i towarów znajdują się w zakładce Cennik.  (www.nazwafirmy.pl/Cennik)"

Negocjacje = ["negocjowalny","negocjowanie","negocjowalna","negocjacje","negocjowac","renegocjowac","renegocjowalne","renegocjowlny"]
Odp_Negocjacje = "Dla niestandardowych ofert czy też negocjacji sprawa powinna być uzgadniana z kierownictwem. W zależności od oferty jesteśmy w stanie podjąć rozmowy negocjacyjne."

Praca = ["praca","pracy","pracowac","staz","staze","praktyki","wakat","wakaty","prace","zatrudnic"]
Odp_Praca = "Dziękujemy za zainteresowanie i chęć pracy w naszej firmie. Wszystkie aktualne oferty pracy i praktyk oraz wymagania dla poszczególnych ofert znajdują się w zakładce Praca. (www.nazwafirmy.pl/Praca) "

Siedziba = ["siedziba","siedziby"]
Odp_Siedziba = "Nasza siedziba mieści się we Wrocławiu przy ulicy składowej 5. "

Onas = ["zajmujecie", "krajach" ,"adres",]
Odp_Onas = "Szczegółowe informacje o naszej firmie znjadują się w zakładce O nas. (www.nazwafirmy.pl/Onas)"

Odp_Do_Kogo = "Proszę skontaktować się z naszym sekretariatem w celu omówienia szczegółów"

Przyszlosc = ["przyszle", "przyszlosc", "przyszlosci"]
Odp_Przyszlosc = "Wszystkie jawne plany na przyszlosc naszej firmy są umieszczane na bierząco w zakladce Plany na Przyszłość. (www.nazwafirmy.pl/Plany_na_Przyszlosc)"

Aktualnosci = ["nowosci","aktualnosci","nowosc"]
Odp_Aktualnosci = "Wszystkie aktualnośc oraz nowości dotyczące naszej firmy są na bieżąco załączane w zakładce Nowości. (www.nazwafirmy.pl/Nowości)"

Komentarz_Firmy = ["komentarz","obrone","skomentuja","powiedzenia","skomentuje"]
Odp_Komentarz_Firmy = "W takich sprawach prosze kontaktować się z naszym rzecznikiem prasowym, który odpowiada za pośrednictow w kontaktach z mediami. Zakładka dla Mediów. (www.nazwafirmy.pl/Dla_Mediow)"

Spotkania =["spotkac","widziec","zobaczyc","porozmawiac"]
Odp_Spotkania = "Wszelkie spotkania z naszymi pracownikami są za pierwszym razem umawiane za pośrednictwem sekretariatu, który rozpatruje słuszność spotkania jak i stara się najlepiej dopasować odpowiednika po naszej stronie do wymaganej sprawy. Strona sekretariatu znajduje się w zakładce Kotakt. (www.nazwafirmy.pl/Kontakt)"

Telefon = ["zadzwonic", "numer", "telefon", "telefonu", "kontakt","skontaktowac","kontaktowac","dzwonic","telefonu","email","maila","mail","emaila"]
Odp_Telefon = "Wszystkie informacje na ten temat znajdują się w zakładce kontakt. Brak podania numerów do wszystkich oznacza konieczność inicjacji pierwszej rozmowy czy też spotkania za pośrednictwem sekretariatu, który weryfikuje słuszność sprawy. (www.nazwafirmy.pl/Kontakt)"

Podziekowanie = ["dziekuje","dzieki","thx"]
Odp_Podziekowanie = "Cała przyjemnośc po naszej stronie."

Niezrozumiale = "Przykro mi, ale nie rozumiem pytania. Czy mógłbym prosić o przeformułowanie?"

Rabat = ["rabat", "lojalnosciowy", "lojalnosciowe", "rabaty", "upust", "upusty","rabatow"]
Odp_Rabat = "Oczywiście udzielamy rabatów. Są one ustalane indywidualnie, w zalezności od składanej oferty. Sprawy tego typu proszę kierować do naszego sekretariatu, który skieruje zapytanie do odpowiedniej osoby."


Zamowienia = ["zamowic", "zamawiac", "zamowienie", "zamowiony", "zamawiany", "zamowienia"]
Odp_Zamowienia = "W celu uzyskania szczegółowych informacji proszę kierować się do zakładki Zamówienia. (www.nazwafirmy.pl/Zamowienia)"

Wspolpraca = ["wspolpracy","kooperowac","wspolpracowac","kooperacji","wspoldzialac","wspoltworzyc","wspolprace"]
Odp_Wspolpraca = "Tematy współpracy proszę kierować do naszego sekretariatu. Sprawa zostanie skierowana do odpwoeidnich ludzi po zapoznaniu się ze szczegółami oferty."

Przetargi = ["przetargi" , "przetargach" , "przetargow"]
Odp_Przetargi = "Lista ogłaszanych przez nas przetargów znajduje się w zakładce Przetargi. (www.nazwafirmy.pl/Przetargi)"



# SPRAWDZACZ ELEMENTÓW DWÓCH LIST A i B

def Sprawdzacz(a, b):
    for i in a:
       if i in b:
          return True
    return False


# INSTRUKCJA

print("-------------------------------------------------------------------------------")
print("Na Czacie prosimy o formułowanie różnych zapytań w różnych wiadmościach. ")
print("Zapewni to szybszą i precyzyjniejszą odpowiedź z naszej strony.")
print("--------------------------------------------------------------------------------")
print("Czat online:  ")

# Konwersacja




while True:

	# CZYSZCZENIE I UJEDNOLICENIE WARTOSCI WEJSCIOWYCH
	zdanie = input(">>> ")
	bez_polskich_znakow = unidecode.unidecode(zdanie)
	mala_litera = bez_polskich_znakow.lower()
	slowa_klucze = re.split(r'\W+', mala_litera)
	dlugosc_zdania = len(zdanie)
	
	#parametry testowe:
	#print(dlugosc_zdania)
	#print(slowa_klucze)



	if Sprawdzacz(slowa_klucze,Przywitanie) or ("dzien" and "dobry" in slowa_klucze) or ("dobry" and "wieczor" in slowa_klucze):
		time.sleep(2.5)
		print(Odp_Przywitanie)
		if Sprawdzacz(slowa_klucze,Nastroj) or ("jak" and "sie" and "masz" in slowa_klucze) or ("co" and "tam" in slowa_klucze):
			time.sleep(2.5)
			print(Odp_Nastroj)
		elif Sprawdzacz(slowa_klucze,Godziny_Otwarcia):
			time.sleep(2.5)
			print(Odp_Godziny_Otwarcia)
		elif Sprawdzacz(slowa_klucze,Negocjacje):
			time.sleep(2.5)
			print(Odp_Negocjacje)
		elif Sprawdzacz(slowa_klucze,Cennik):
			time.sleep(2.5)
			print(Odp_Cennik)
		elif Sprawdzacz(slowa_klucze,Praca):
			time.sleep(2.5)
			print(Odp_Praca)
		elif Sprawdzacz(slowa_klucze,Przyszlosc):
			time.sleep(2.5)
			print(Odp_Przyszlosc)
		elif Sprawdzacz(slowa_klucze,Aktualnosci):
			time.sleep(2.5)
			print(Odp_Aktualnosci)
		elif Sprawdzacz(slowa_klucze,Telefon):
			time.sleep(2.5)
			print(Odp_Telefon)
		elif Sprawdzacz(slowa_klucze,Spotkania):
			time.sleep(2.5)
			print(Odp_Spotkania)
		elif Sprawdzacz(slowa_klucze,Podziekowanie):
			time.sleep(2.5)
			print(Odp_Podziekowanie)
		elif ("do" and "kogo" in slowa_klucze) or ("z" and "kim" in slowa_klucze):
			time.sleep(2.5)
			print(Odp_Do_Kogo)	
		elif Sprawdzacz(slowa_klucze,Siedziba):
			time.sleep(2.5)	
			print(Odp_Siedziba)		
		elif Sprawdzacz(slowa_klucze,Wspolpraca):
			time.sleep(2.5)	
			print(Odp_Wspolpraca)
		elif Sprawdzacz(slowa_klucze,Rabat):
			time.sleep(2.5)	
			print(Odp_Rabat)
		elif Sprawdzacz(slowa_klucze,Zamowienia):
			time.sleep(2.5)	
			print(Odp_Zamowienia)		
		elif Sprawdzacz(slowa_klucze,Przetargi):
			time.sleep(2.5)	
			print(Odp_Przetargi)
		elif Sprawdzacz(slowa_klucze,Komentarz_Firmy):
			time.sleep(2.5)	
			print(Odp_Komentarz_Firmy)
		elif Sprawdzacz(slowa_klucze,Onas) or (("profil" and "dzialalnosci" in slowa_klucze) or ("czym" and "zajmuje" and "firma" in slowa_klucze)):
			time.sleep(2.5)	
			print(Odp_Onas)	
	elif Sprawdzacz(slowa_klucze,Nastroj) or ("jak" and "sie" and "masz" in slowa_klucze):
		time.sleep(2.5)
		print(Odp_Nastroj)
	elif Sprawdzacz(slowa_klucze,Godziny_Otwarcia):
		time.sleep(2.5)
		print(Odp_Godziny_Otwarcia)
	elif Sprawdzacz(slowa_klucze,Negocjacje):
		time.sleep(2.5)
		print(Odp_Negocjacje)	
	elif Sprawdzacz(slowa_klucze,Cennik):
		time.sleep(2.5)
		print(Odp_Cennik)
	elif Sprawdzacz(slowa_klucze,Praca):
		time.sleep(2.5)
		print(Odp_Praca)
	elif Sprawdzacz(slowa_klucze,Przyszlosc):
		time.sleep(2.5)
		print(Odp_Przyszlosc)
	elif Sprawdzacz(slowa_klucze,Aktualnosci):
		time.sleep(2.5)
		print(Odp_Aktualnosci)
	elif Sprawdzacz(slowa_klucze,Telefon):
		time.sleep(2.5)
		print(Odp_Telefon)
	elif Sprawdzacz(slowa_klucze,Spotkania):
		time.sleep(2.5)
		print(Odp_Spotkania)
	elif Sprawdzacz(slowa_klucze,Podziekowanie):
		time.sleep(2.5)
		print(Odp_Podziekowanie)
	elif ("do" and "kogo" in slowa_klucze) or ("z" and "kim" in slowa_klucze):
		time.sleep(2.5)
		print(Odp_Do_Kogo)	
	elif Sprawdzacz(slowa_klucze,Siedziba):
		time.sleep(2.5)	
		print(Odp_Siedziba)
	elif Sprawdzacz(slowa_klucze,Wspolpraca):
		time.sleep(2.5)	
		print(Odp_Wspolpraca)	
	elif Sprawdzacz(slowa_klucze,Rabat):
		time.sleep(2.5)	
		print(Odp_Rabat)
	elif Sprawdzacz(slowa_klucze,Zamowienia):
		time.sleep(2.5)	
		print(Odp_Zamowienia)
	elif Sprawdzacz(slowa_klucze,Przetargi):
		time.sleep(2.5)	
		print(Odp_Przetargi)
	elif Sprawdzacz(slowa_klucze,Komentarz_Firmy):
		time.sleep(2.5)	
		print(Odp_Komentarz_Firmy)
	elif Sprawdzacz(slowa_klucze,Onas) or ("czym" and "zajmuje" and "firma" in slowa_klucze):
		time.sleep(2.5)	
		print(Odp_Onas)
	else:
		time.sleep(2.5)
		print(Niezrozumiale)
		
		# WSZYSTKIE BRAKI ODPOWIEDZI ZAPISYWAC W PLIKU TEKSTOWYM
		
		Errata = open('Errata.txt', 'a')
		Errata.write(">>> " + zdanie + "\n" + "\n")
		Errata.close()
