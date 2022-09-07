jour = ""

lettre = input("Quelle lettre voulez-vous poster parmis les ; verte,prioritaire et eco : ")

if ((lettre == "verte") or (lettre =="prioritaire") or (lettre == "eco")):

    poids = input("Quelle est le poids de la lettre (en g) : ")
    poids = int(poids)
    if (0 < poids < 3000):

        

        sticker = input("Voulez vous un sticker de suivi ? ")

        OM1 = input("Voulez vous envoyez vers zone OM1 ? ")
        OM2 = input("Voulez vous envoyez vers zone OM2 ? ")


        if lettre == 'verte':
            if 0 < poids <= 20:
                prix = 1.16
            elif 20 < poids <= 100:
                prix = 2.32
            elif 100 < poids<= 250:
                prix = 4
            elif 250 < poids<= 500:
                prix = 6
            elif 500 < poids<= 1000:
                prix = 7.50
            elif 1000 < poids<= 3000:
                prix = 10.50

            jour = "2"
            OM1prix = 0.05 * (poids/10)
            OM2prix = 0.11 * (poids/10)

        if lettre == 'prioritaire':

            if 0 < poids <= 20:
                prix = 1.43
            elif 20 < poids <= 100:
                prix = 2.86
            elif 100 < poids<= 250:
                prix = 5.26
            elif 250 < poids<= 500:
                prix = 7.89
            elif 500 < poids<= 3000:
                prix = 11.44

            jour = "1"
            OM1prix = 0.05 * (poids/10)
            OM2prix = 0.11 * (poids/10)

        if lettre == 'eco':
            
            if 0 < poids <= 20:
                prix = 1.14
            elif 20 < poids <= 100:
                prix = 2.28
            elif 100 < poids<= 250:
                prix = 3.92

            jour = "4"
            OM1prix = 0.02 * (poids/10)
            OM2prix = 0.5 * (poids/10)



        stickerprix = prix +0.5
        OM1total = prix + OM1prix
        OM2total = prix + OM2prix
        stickerOM1 = OM1total + 0.5
        stickerOM2 = OM2total + 0.5




        print("Voici le type de lettre choisie : ",lettre,"et mettra",jour,"jour(s)")
        print("Voici le poids de votre lettre : ",poids,"g")
        print("Voici le prix total de l'affranchissement sans les compléments : ",prix,"€")

        if sticker == 'oui':
            print("Voici le prix total de l'affranchissement avec sticker : ",stickerprix,"€")

        if OM1 == 'oui':
            print("Prix total pour zone OM1 : ",OM1total,"€")

        if OM2 == 'oui':
            print("Prix total pour zone OM2 : ",OM2total,"€")
        
        if sticker == 'oui':
            if OM1 == 'oui':
                print("Prix total avec compléments",stickerOM1,"€")
        
        if sticker == 'oui':
            if OM2 == 'oui':
                print("Prix total avec compléments",stickerOM2,"€")


            




    else:
        print("ERREUR : le poids doit être compris entre 0 et 3000g")
        
else:
    print("ERREUR : vous devez obligatoirement choisir entre les 3 options.")