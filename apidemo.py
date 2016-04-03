from urllib2 import urlopen

#url = "http://lorempixel.com/g/500/500/"
url = "http://lorempixel.com"
tipos = ["abstract" , "animals" , "business" , "cats" , "city",
         "food" , "nightlife" , "fashion" , "people","nature" , "sports" ,
         "technics" , "transport"]

ancho = raw_input("Cual es el ancho? ")
alto = raw_input("Cual es el alto? ")
print tipos
tipo = raw_input("Cual es el tipo? ")

for img in range(10):
    url_req = "%s/%s/%s/%s/%d" % (url,ancho, alto , tipos[int(tipo)],img)

    placeholder = urlopen(url_req)

    lectura = placeholder.read()

    f = open("holder_%d.jpg" % img , "wb")
    f.write(lectura)
    f.close()