class Animal:
    def __init__(self, pelo, patas, raca, som):
        self.pelo = pelo
        self.patas = patas
        self.raca = raca
        self.som_animal = som
        
    def __str__(self):
        return self.raca
    
    def som(self):
        return self.som_animal
        

gato = Animal('curto', 4, 'gato', 'miau')
cachorro = Animal('longo', 3, 'cachorro', 'auau')
cachorro2 = Animal('curto', 4, 'cachorro 2', 'auau')

print(gato, cachorro, cachorro2)
print(f"O {gato}, tem o pelo {gato.pelo}, tem {gato.patas} patas, e o gato faz {gato.som()}")
print(f"O {cachorro}, tem o pelo {cachorro.pelo}, tem {cachorro.patas} patas, e o cachorro faz {cachorro.som()}")
print(f"O {cachorro2}, tem o pelo {cachorro2.pelo}, tem {cachorro2.patas} patas, e o cachorro 2 faz {cachorro2.som()}")
