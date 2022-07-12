from datetime import datetime

class DateTimeFormat:
    
    @classmethod
    def format_date(self, date):
        """Función que toma una fecha y cambia su formato.
        
        Returns:
            str: Fecha con formato YYYY-MM-DD.
        """
        return datetime.strftime(date, '%Y-%m-%d')

    @classmethod
    def format_time(self, date):
        """Función que devuelve la hora actual en un formato especifico.
        
        Returns:
            str: Hora sin zona horaria con formato HH:MM:SS.
        """
        return datetime.strftime(date, '%H:%M:%S')
class Money:
    
    @classmethod
    def get_delivery_amount(self, municipality):
        """Función que determina el monto de delivery dependiendo del municipio donde se
        haga el pedido.
        
        Returns:
            float: Monto del delivery.
        """
        if municipality == 'Maneiro':
            return 0.0
        return 2.0

    @classmethod
    def get_total_amount(self, quantity, delivery_amount):
        """Función que determina monto total en base a la cantidad de hamburguesas y el monto 
        de delivery.
        
        Returns:
            float: Monto total del pedido.
        """
        return float((quantity * 5) + delivery_amount)

class FileExtension:
    ALLOWED_EXTENSION = set(['png', 'jpg'])

    @classmethod
    def is_allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSION