diccionario_vacio = dict()
mete_el_archivo = input("Enter the file name: ")
leelo = open(mete_el_archivo,"r")
for line_to_line in leelo:
    slice = line_to_line.split()        
    for palabra_en_palabra in slice:
        diccionario_vacio[palabra_en_palabra] = diccionario_vacio.get(palabra_en_palabra,0) + 1
Bigword = None
Bigcount = None
for word,count in diccionario_vacio.items():
    if Bigcount is None or count > Bigcount:
        Bigcount = count
        Bigword = word
print(Bigword,Bigcount)


