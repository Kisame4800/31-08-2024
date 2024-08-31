meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "FUNAR": "Denuncia publica de muchas personas hacia alguien",
            "WTF": "Abreviación the What The Fuck",
            "ROTO/A": "Algo o alguien en un juego cuyas habilidades son muy altas y superiores",
            "NERFEAR": "Bajar de nivel de poder o habilidad algo o alguien que tenía poder muy alto"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict)
else:
    print("Escribe bien")
