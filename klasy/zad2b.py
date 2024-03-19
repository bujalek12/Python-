class cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


cake01 = cake("Vanilla Cake", "cake", "vanilla", ["chocolade", "nuts"], "cream")
cake02 = cake("Chocolade Muffin", "muffin", "chocolade", ["chocolade"], "")
cake03 = cake("Super Sweet Maringue", "meringue", "very sweet", [], "")

bakery_offer = [cake01, cake02, cake03]

for c in bakery_offer:
    print("{} = ({}) main taste: {} with additives of {}, filled with {}".format( c.name, c.kind, c.taste, c.additives, c.filling))


#pamietaj że przw woływaniu trzeba dac w tym przypadku np c. i nazwa czego chce wywolać


