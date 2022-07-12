class Customer:
    """La clase Customer sirve para crear objetos que reflejen los datos de la tabla de 
    clientes de la base de datos de Chikkins."""

    def __init__(self, cedula, nombre, whatsapp, email):
        """Método constructor de la clase Customer."""
        self.cedula = cedula
        self.nombre = nombre
        self.whatsapp = whatsapp
        self.email = email

    def to_JSON(self):
        """Método que devuelve un formato transformable a JSON de la clase Customer.
        
        Returns:
        dict(str, str): Diccionario transformable a formato JSON. 
        """
        return {
            'cedula' : self.cedula,
            'name' : self.nombre,
            'whatsapp' : self.whatsapp,
            'email' : self.email
        }
