# Clase
class Coffee:
    def __init__(self, nombre, tipo_grano, ID, tipo_temperatura, precio):
        self.__nombre = nombre
        self.__tipo_grano = tipo_grano
        self.__ID = ID
        self.__tipo_temperatura = tipo_temperatura
        self.__precio = precio

# Getters
def get_nombre(self):
        return self.__nombre

def get_tipo_grano(self):
        return self.__tipo_grano

def get_ID(self):
        return self.__ID

def get_tipo_temperatura(self):
        return self.__tipo_temperatura

def get_precio(self):
        return self.__precio

# Setters
def set_nombre(self, nombre):
       self.__nombre = nombre

def set_tipo_grano(self, tipo_grano):
       self.__tipo_grano = tipo_grano

def set_ID(self, ID):
       self.__ID = ID

def set_tipo_temperatura(self, tipo_temperatura):
       self.__tipo_temperatura = tipo_temperatura

def set_precio(self, precio):
       self.__precio = precio

# Metodo 1
def aplicar_descuento(self, porcentaje):
        descuento = self.__precio * (porcentaje / 100)
        self.__precio -= descuento

# Metodo 2
def cambiar_temperatura(self, nueva_temp):
        self.__tipo_temperatura = nueva_temp
        return f"La bebida ahora es {self.__tipo_temperatura}"

# Metodo info
def info(self):
       print(f"Nombre: {self.__nombre}")
       print(f"Tipo de grano: {self.__nombre}")
       print(f"ID: {self.__nombre}")
       print(f"Temperatura: {self.__nombre}")
       print(f"precio: {self.__precio}")
