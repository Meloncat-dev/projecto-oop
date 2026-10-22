def leer_numero(msg: str) -> int:
    while True:    
        try:
            return int(input(msg))
        except ValueError:
            print("intenta ingresando un numero")
