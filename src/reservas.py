import csv
from typing import NamedTuple
from datetime import date, datetime

Reserva = NamedTuple("Reserva", 
                     [("nombre", str),
                      ("dni", str),
                      ("fecha_entrada", date),
                      ("fecha_salida", date),
                      ("tipo_habitacion", str),
                      ("num_personas", int),
                      ("precio_noche", float),
                      ("servicios_adicionales", list[str])
                    ])



def lee_reservas(ruta_fichero: str) -> list[Reserva]:
    res = []
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, \
        num_personas, precio_noche, servicio_adicionales in lector:
            fecha_entrada = parseo_fecha(fecha_entrada)
            fecha_salida = parseo_fecha(fecha_salida)
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            # servicio_adicionales = list(servicio_adicionales)
            res.append(Reserva(nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, \
            num_personas, precio_noche, servicio_adicionales))
    return res



def parseo_fecha(fecha):
    fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
    return fecha


#(fecha2 - fecha1).days

def total_facturado(reservas: list[Reserva], 
                    fecha_ini: date | None = None, 
                    fecha_fin: date | None = None) -> float:
    
    if fecha_ini is None:
        fecha_ini = datetime.min.date()
    if fecha_fin is None:
        fecha_fin = datetime.max.date()
    
    total = sum(a.precio_noche for a in reservas if fecha_ini <= a.fechahora.date() <= fecha_fin)
    
    return total


def reservas_mas_largas(reservas: list[Reserva], n: int = 3) -> list[tuple[str, date]]:
    res= []
    for a in reservas:
        res.append(((a.nombre,a.fecha_entrada,(a.fecha_salida - a.fecha_entrada).days)))
    res_ord = sorted(res, key = lambda r:r[2], reverse = True)
    return [(x[0],x[1]) for x in res_ord][:n]


def cliente_mayor_facturacion(reservas: list[Reserva], 
                              servicios: set[str] | None = None) -> tuple[str, float]:
    
    # res = max(((a.dni,a.precio_noche) for a in reservas if servicios == None or a.servicios_adicionales in servicios), key = lambda r:r[1])
    # return res


    d = dict()
    for a in reservas:
        dni = a.dni
        serv = a.servicios_adicionales
        if dni in d:
            
            if serv in d[dni]:
                d[dni][serv]+=a.precio_noche
            else:
                d[dni][serv]=a.precio_noche
        else:
            d[dni] = {serv:a.precio_noche}
    if servicios is None:

