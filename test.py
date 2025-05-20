import locality

manetin = locality.Locality("Manetin", 0.8)
brno = locality.Locality("Brno", 3)

zem_pozemek = locality.Estate(manetin, locality.Estate_type.LAND, 900)
print(zem_pozemek)

house = locality.Residence(manetin, 120, False)
print(house)

office = locality.Residence(brno, 90, True)
print(office)

priznani = locality.TaxReport("Franta Novak", [house, zem_pozemek])

print(priznani.calculate_tax())