import locality

#nejprve vytvorim 2 lokality
manetin = locality.Locality("Manetin", 0.8)
brno = locality.Locality("Brno", 3)

#zemedelsky pozemek v Manetine
zem_pozemek = locality.Estate(manetin, locality.Estate_type.LAND, 900)
print(zem_pozemek)

#dum v Manetine
house = locality.Residence(manetin, 120, False)
print(house)

#kancelar v Brne
office = locality.Residence(brno, 90, True)
print(office)

#danove priznani Franty Novaka
priznani = locality.TaxReport("Franta Novak", [house, zem_pozemek, office])
print(priznani)