print ("ceci est un test d'écriture afin de voir si mon Github est bien configuré")

def test ():
    a = input("entrez votre nom")
    return a
a= test()
print (a)

print ("test")

class DicoOrdonne:

    def __init__(self, base = {}, **data):
        self.cle = []
        self.data = []

        for cle in base:
            self.cle.append(cle)

        for values in base.values():
            self.data.append(values)

    def __setitem__(self, key, value):

        i=0
        exist = False
        for cle in self.cle:
            if key == self.cle[i]:
                exist = True
                break
            else:
                i += 1
                exist = False
        if exist == True:
            self.data [i]= value
        else:
            self.cle.append(key)
            self.data.append(value)

    def __getitem__(self, item):

        i=0
        for cle in self.cle:
            if item == self.cle[i]:
                exist = True
                break
            else:
                i+=1
                exist = False

        if exist == True:
            print ("la valeur de {} est égal à {}".format(self.cle[i], self.data[i]))
        else:
            print("Erreur, l'objet {} ne contient pas la clé {}".format(self, item))


            print ()

    def __repr__(self):
        backbone = ""
        debut = "{"
        fin = "}"
        i=0
        l= len(self.cle)-1
        for cle in self.cle:
        if i == 0:
            backbone="{}{}: {}".format(debut, self.cle[i], self.data[i])
            i += 1
        elif i == 0 and l == 0:
            backbone = "{}{}: {}{}".format(debut, self.cle[i], self.data[i], fin)
            i += 1
        elif i != 0 and i != l:
            backbone = "{}, {}: {}".format(backbone, self.cle[i], self.data[i])
            i += 1
        elif i == l:
            backbone = "{}, {}: {}{}".format(backbone, self.cle[i], self.data[i], fin)
            i += 1

        return backbone

    def __add__(self, other):
        type_other = type (other)
        if type_other != DicoOrdonne:
            typeOk = False
            print("le type de l'objet à ajouter n'est pas bon, l'objet doit être un DicoOrdonne")
        else:
            typeOk = True

        if typeOk == True:
            i = 0
            for cle in other.cle:
                self.cle.append(other.cle[i])
                self.data.append(other.data[i])
                i+=1
        else:
            print("error type 2em objet n'est pas le meme que type 1er objet")

    def __len__(self):
        lenght = len(self.cle)
        return lenght

    def __delitem__(self, key):
        i = 0
        for cle in self.cle:
             if key == self.cle[i]:
                del self.cle[i]
                del self.data[i]
            else:
                i += 1






test2= DicoOrdonne({"pomme":10})
test2.cle
test2.data
test2["pomme"]=20
test2["tomate"]=3
test2 ["tomate"]
test2
test3= DicoOrdonne()
test3["courgette"]=10
test3["oignon"]=15
test3
test4 = test2 + test3
test= {"pomme" : 5, "poire" : 10}
test



for cle in test:
    print (cle)

for valeur in test.values():
    print (valeur)
i=0
for key in test2.cle:
    if key == test2.cle[i]:
        exist = True
        break
    else:
        i += 1
        exist = False
if exist == True:
    test2.data[i] = value
else:
    test2.cle.append(key)
    test2.data.append(value)

def intervalle (inf, sup):
    inf +=1
    while inf < sup:
        yield inf
        inf +=1