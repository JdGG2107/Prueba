my_dict = {"SILLY": "Something out of place in a funny manner, or goofy",
          "IDK": "I dont know",
          "DW": "dont worry",
          }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print (my_dict[word])
else:
    print ("La palabra no está en el diccionario")
          
