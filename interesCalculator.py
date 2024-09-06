class interesCalculator:
    def __init__(self):
        # Este es el método constructor. Se ejecuta cuando se crea una nueva instancia de la clase.
        self.montoDeposito = float(input("Inserte monto de dinero a calcular: "))

    def calculaInteres(self):
        print("Calculando interes para un año")
        if self.montoDeposito <= 10000:
            monto = self.montoDeposito * (1 + 0.03)
            print(f"Interes en un año es S/{monto} usando el 3%")
        else:
            monto = self.montoDeposito * (1 + 0.04)
            print(f"Interes en un año es S/{monto} usando el 4%")


