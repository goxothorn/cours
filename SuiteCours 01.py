print ("ceci est un test d'écriture afin de voir si mon Github est bien configuré")

def test ():
    a = input("entrez votre nom")
    return a
a= test()
print (a)

print ("test")

class DicoOrdonne:

    def __init__(self, base = {}, **data):
        self.key = []
        self.value = []

        for cle in base:
            self.key.append(cle)

        for values in base.values():
            self.value.append(values)




test= {"pomme" : 5, "poire" : 10}
test
for cle in test:
    print (cle)

for valeur in test.values():
    print (valeur)