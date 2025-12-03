from reservas import *

def test_lector(ruta):
    root = lee_reservas(ruta)
    print(root)


def test_reservas_mas_largas(reservas,n):
    m = reservas_mas_largas(reservas,n)
    print(m)

def test_cliente_mayor_facturacion(reservas,sevicios):
    c = cliente_mayor_facturacion(reservas,sevicios)
    print(c)





def main():
    test_lector("data/reservas.csv")
    ruta = lee_reservas("data/reservas.csv")
    test_reservas_mas_largas(ruta,3)
    test_cliente_mayor_facturacion(ruta,{"Parking"})

if __name__ == "__main__":
    main()