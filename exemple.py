nbr = 1

while nbr <= 11:
    if nbr % 2 == 0:
        print(nbr)
    nbr += 1


persone={"nom":"fouzi","age":24,"ville":"paris"}
print(persone["nom"])
prenom ="sarah"
nom="khiter"
nom_complet= prenom + " " + nom
print (nom_complet)

nom = input("Entrez votre nom de famille en majuscule : ")
prenom = input("Entrez votre prénom : ")
age = input("Entrez votre âge : ")
taille = input("Entrez votre taille  : ")
fruits = input("Entrez une liste de fruits préférés  : ").split()
message = "Bonjour "+ prenom +" "+nom +"! Vous avez " +age +" ans et mesurez " +taille+"cm"
print(message)
print("Liste des fruits préférés :")
for f in fruits:
    print(f)