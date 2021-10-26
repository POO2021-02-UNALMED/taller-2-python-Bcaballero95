class Asiento :

    def __init__ (self, color, precio, registro) :
        self.registro = registro
        self.precio = precio
        self.color = color

    def cambiarColor (self, color) :
        if color == "blanco" or color == "rojo" or color == "amarillo" or color == "negro" or color == "verde" :
            self.color = color


class Motor :

    def __init__ (self, numeroCilindros, tipo, registro) :
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegsitro (self, r) :
        self.registro = r

    def asignarTipo (self, tipo) :
        if tipo == "normal" or tipo == "electrico" :
            self.tipo = tipo


class Auto :
    cantidadCreados = 0

    def __init__ (self, modelo, precio, asientos, marca, motor, registro) :
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos (self) :
        c = 0
        for i in self.asientos :
            if isinstance (self.asientos[i], Asiento) :
                c += 1
        return c

    def verificarIntegridad (self) :
        ok = False
        if self.motor.registro == self.registro :
            for i in self.asientos :
                if isinstance (self.asientos[i], Asiento) and self.asientos[1].registro == self.registro :
                    ok = True
                else :
                    ok = False
                    break
        if ok == False :
            print ("Las piezas no son originales")
        else :
            print ("Auto original")
