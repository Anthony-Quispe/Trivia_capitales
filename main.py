import random
import time

ruptura = False
while True:

    countries = [
        "Peru", "Rusia", "China", "Alemania", "Argelia", "Austria", "Paraguay"
    ]
    CorretAnswers = ["b", "c", "c", "a", "a", "b", "c"]
    answersqu = [["A) Napoleon", "B) Lima", "C) Callao"],
                 ["A) Priviet", "B) Estambul", "C) Moscu"],
                 ["A)italia", "B) roma", "C) Pekin"],
                 ["A) Berlin", "B) Bayern", "C) Hessen"],
                 ["A) Argel", "B) Yemen", "C) Estonia"],
                 ["A) Ghana", "B) Viena", "C) Estocolmo"],
                 ["A) Uruguay", "B) Defuncion", "C) Asuncion"]]
    ScoreAnswer = []
    score = 50
    vuelta = 0
    validacion = ("a", "b", "c", "d", "admin")

    def answer(n):
        while n.lower() not in validacion:
            n = str(input("error dame una respuesta valida (a-b-c-d)\n"))

    print("Bienvenido a la trivia de capitales, disfruta mi juego")
    time.sleep(4)
    for country in countries:
        print("\nEscribe la letra de la alternativa correcta\n")
        print(f"¿Cual es la capital de {country}?")

        scoreQ = 0
        for element in answersqu[vuelta]:
            print(element)
        res = str(input("\n"))
        answer(res)

        if res.lower() == "admin":
            scoreQ += random.randint(1, 550)
            print("saludos mi general, respuesta correcta.\n")
        elif res.lower() not in CorretAnswers[vuelta]:
            if scoreQ >= 0:
                scoreQ -= random.randint(150, 370)
            else:
                scoreQ = scoreQ
            print("\nQue mal, respuesta incorrecta")
        elif res.lower() in CorretAnswers[vuelta]:
            scoreQ += random.randint(120, 141)
            print("\nfelicidades acertaste en la respuesta!")
        else:
            print("\nha ocurrido un error, contacte con soporte al usuario\n")

        ScoreAnswer.insert(vuelta, scoreQ)
        score += scoreQ
        vuelta += 1
        time.sleep(2)

    ruleta = str(input("\ndeseas probar nuestra ruleta de puntos? Y/N : "))
    if ruleta.upper() == "Y":
        print(
            "tu score sera actualizado por nuestra ruleta entre 0 y poco mas de 1000 puntos\n"
        )
        score = random.randint(0, 1000 + score)
        time.sleep(7)

    print(f"tu score por pregunta fue: {ScoreAnswer}")
    print(f"tu score total es: {score}\n")
    cerrar = input("\n¿Quieres seguir jugando? Y/N: ")

    while True:
        if not (cerrar.upper() == "Y" or cerrar.upper() == "N"):
            cerrar = str(input("Debes escribir Y/N : "))
        elif cerrar.upper() == "N":
            ruptura = True
            break
        elif cerrar.upper() == "Y":
            print("¡Está decidido! Volveremos a jugar, prepárate.")
            break

    if ruptura == True:
        break
