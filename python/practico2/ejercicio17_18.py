"""
Cree una clase FuncionesPrograma y codifique una función estática getFechaString
que reciba como parámetro una fecha y retorne la fecha como una cadena literal.
Ejemplo recibo 15/10/1900, la salida debe ser
Quince de Octubre de mil novecientos.
Cree una clase Principal que contenga un método main y haga uso de la función
getFechaString.
"""

class FuncionesPrograma:

    @staticmethod
    def getFechaString(fecha):
        dias = {
            '01': 'Primero',
            '02': 'Dos',
            '03': 'Tres',
            '04': 'Cuatro',
            '05': 'Cinco',
            '06': 'Seis',
            '07': 'Siete',
            '08': 'Ocho',
            '09': 'Nueve',
            '10': 'Diez',
            '11': 'Once',
            '12': 'Doce',
            '13': 'Trece',
            '14': 'Catorce',
            '15': 'Quince',
            '16': 'Dieciseis',
            '17': 'Diecisiete',
            '18': 'Dieciocho', 
            '19': 'Diecinueve', 
            '20': 'Veinte',
            '21': 'Veintiuno', 
            '22': 'Veintidós', 
            '23': 'Veintitrés', 
            '24': 'Veinticuatro', 
            '25': 'Veinticinco',
            '26': 'Veintiséis',
            '27': 'Veintisiete',
            '28': 'Veintiocho',
            '29': 'Veintinueve', 
            '30': 'Treinta',
            '31': 'Treinta y uno'
        }
        meses = {
            '01': 'Enero',
            '02': 'Febrero',
            '03': 'Marzo',
            '04': 'Abril',
            '05': 'Mayo',
            '06': 'Junio',
            '07': 'Julio',
            '08': 'Agosto',
            '09': 'Septiembre',
            '10': 'Octubre',
            '11': 'Noviembre',
            '12': 'Diciembre'
        }

        unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seicientos", "setecientos", "ochocientos", "novecientos"]

        dia, mes, anio = fecha.split('/')

        anio_nro = int(anio)
        anio_letras = ""

        print(anio_nro)

        if anio_nro == 1000:
            anio_letras = "mil"
        elif anio_nro < 1000:
            c = anio_nro // 100
            d = (anio_nro % 100) // 10
            u = anio_nro % 10
            anio_letras = f"{centenas[c]} {decenas[d]} {unidades[u]}".strip()
        else:
            miles = anio_nro // 1000
            resto = anio_nro % 1000
            c = resto // 100
            d = (resto % 100) // 10
            u = resto % 10
           
            

            if miles > 1:
                anio_letras = f"{unidades[miles]} mil  {centenas[c]} {decenas[d]} {unidades[u]}".strip()
            else:
                anio_letras = f"mil {centenas[c]} {decenas[d]} {unidades[u]}".strip()

        fecha_string = f"{dias[dia]} de {meses[mes]} de {anio_letras}".capitalize()
        return fecha_string

    @staticmethod
    def getFechaDate(dia, mes, anio):
        return 
class Principal:
    def main():
        fecha = "15/10/1024"
        resultado = FuncionesPrograma.getFechaString(fecha)
        print(resultado)

Principal.main()