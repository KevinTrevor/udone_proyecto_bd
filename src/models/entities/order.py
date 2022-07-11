class Order:
    """La clase Order sirve para crear objetos que reflejen los datos de la tabla de 
    pedidos de la base de datos de Chikkins."""

    def __init__(
            self, id, cedula, cantidad, monto_delivery,
            total, modo_pago, screenshot, estado, fecha, 
            hora, ciudad, municipio, observaciones):
        """Método constructor de la clase Order."""
        self.id = id
        self.cedula = cedula
        self.cantidad = cantidad
        self.monto_delivery = monto_delivery
        self.total = total
        self.modo_pago = modo_pago
        self.screenshot = screenshot
        self.estado = estado
        self.fecha = fecha
        self.hora = hora
        self.ciudad = ciudad
        self.municipio = municipio
        self.observaciones = observaciones

    def to_JSON(self):
        """Método que devuelve un formato transformable a JSON de la clase Order.
        
        Returns:
        dict(str, Any): Diccionario transformable a formato JSON. 
        """
        return {
            'quantity' : self.cantidad,
            'payment_method' : self.modo_pago,
            'remarks' : self.observaciones,
            'city' : self.ciudad,
            'municipality' : self.municipio,
            'cedula' : self.cedula,
            'total' : f"${self.total}",
            'payment_screenshot' : self.screenshot,
            'status' : self.estado,
            'delivery_amount' : f"${self.monto_delivery}",
            'order_number' : self.id,
            'datetime' : f"{self.fecha} {self.hora}"
        }