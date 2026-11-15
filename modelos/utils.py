def leer_numero(msg: str) -> int:
    while True:    
        try:
            return int(input(msg))
        except ValueError:
            print("intenta ingresando un numero")

def confirmar(mensaje: str) -> bool:
    while True:
        resp = input(f"{mensaje} (si/no): ").strip().lower()
        if resp in ("si", "no"):
            return resp == "si"
        print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")
