def sustitucionVocales(sentence, character):

    #Minúsculas 
    sentence = sentence.replace("a", character)
    sentence = sentence.replace("e", character)
    sentence = sentence.replace("i", character)
    sentence = sentence.replace("o", character)
    sentence = sentence.replace("u", character)

    #Mayúsculas
    sentence = sentence.replace("A", character)
    sentence = sentence.replace("E", character)
    sentence = sentence.replace("I", character)
    sentence = sentence.replace("O", character)
    sentence = sentence.replace("U", character)

    #Acentos Minúsculas
    sentence = sentence.replace("á", character)
    sentence = sentence.replace("é", character)
    sentence = sentence.replace("í", character)
    sentence = sentence.replace("ó", character)
    sentence = sentence.replace("ú", character)

    #Acentos Mayúsculas
    sentence = sentence.replace("Á", character)
    sentence = sentence.replace("É", character)
    sentence = sentence.replace("Í", character)
    sentence = sentence.replace("Ó", character)
    sentence = sentence.replace("Ú", character)

    return sentence


def main():
    #Pedir frase y caracter
    print("================================================================ ")
    frase = input("Dime una frase : ")
    caracter = input("Dime un caracter : ")

    #Sustituír y devolver la frase cambiada
    print(f"La nueva frase es : {sustitucionVocales(frase, caracter)}")
    print("================================================================ ")



if __name__ == "__main__":
    main()