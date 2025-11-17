# Fundamentos de Programación
## Reservas de hotel

**Autor:** Fermín Cruz  
**Revisores:** Alfonso Bengoa, Mariano González, Toñi Reina  

---

### Estructura de las carpetas del proyecto

- **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.  
  - **reservas.py**: Contiene funciones para explotar los datos de reservas.  
  - **reservas_test.py**: Contiene funciones de test para probar las funciones del módulo `reservas.py`. En este módulo está el `main`.  
  - Puede añadir otros módulos para funciones auxiliares si así lo desea.

- **/data**: Contiene el dataset o datasets del proyecto.  
  - **reservas.csv**: Archivo con las reservas de un hotel.

---
### Ejercicios a realizar

Se quieren analizar los datos de las reservas de un hotel. Para ello se dispone de un archivo en formato CSV codificado en UTF-8.  
En cada línea del archivo se recoge la siguiente información: el nombre y DNI del cliente, las fechas de entrada y salida, el tipo de habitación, el número de personas, el precio por noche y los servicios adicionales contratados.

Las primeras líneas del fichero son:

```csv
nombre,dni,fecha_entrada,fecha_salida,tipo_habitacion,num_personas,precio_noche,servicios_adicionales
Ana Fernández,98762912S,2022-01-02,2022-01-06,Suite,4,202.97,"Parking,Gimnasio,Spa"
María Fernández,25061289Y,2022-01-01,2022-01-03,Familiar,4,83.77,
```

> Algunas reservas no incluyen servicios adicionales, en cuyo caso aparece una cadena vacía.  
> En otras, puede haber varios servicios separados por comas.  
> **El orden de las reservas en el CSV es arbitrario**, no necesariamente cronológico.

---

### Definición obligatoria de `NamedTuple`

```python
from typing import NamedTuple
from datetime import date

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
```

> **Nota:** Para calcular el número de días entre dos fechas `fecha1` y `fecha2`, puede usar:  
> ```python
> (fecha2 - fecha1).days
> ```

---

### Funciones a implementar

#### 1. `lee_reservas`

Recibe la ruta de un fichero CSV y devuelve una lista de tuplas `Reserva` con todos los datos.

```python
def lee_reservas(ruta_fichero: str) -> list[Reserva]:
```

**Resultado esperado:**
```
Test lee_reservas
Total reservas: 496
Las tres primeras:
    Reserva(nombre='Ana Fernández', dni='98762912S', fecha_entrada=datetime.date(2022, 1, 2), fecha_salida=datetime.date(2022, 1, 6), tipo_habitacion='Suite', num_personas=4, precio_noche=202.97, servicios_adicionales=['Parking', 'Gimnasio', 'Spa'])
    Reserva(nombre='María Fernández', dni='25061289Y', fecha_entrada=datetime.date(2022, 1, 1), fecha_salida=datetime.date(2022, 1, 3), tipo_habitacion='Familiar', num_personas=4, precio_noche=83.77, servicios_adicionales=[])
    Reserva(nombre='Laura López', dni='13728274B', fecha_entrada=datetime.date(2022, 1, 2), fecha_salida=datetime.date(2022, 1, 10), tipo_habitacion='Estandar', num_personas=1, precio_noche=87.58, servicios_adicionales=[])
```

---

#### 2. `total_facturado`

Calcula el total facturado en todas las reservas cuya fecha de entrada esté entre dos fechas dadas.

```python
def total_facturado(reservas: list[Reserva], 
                    fecha_ini: date | None = None, 
                    fecha_fin: date | None = None) -> float:
```

**Resultado esperado:**
```
Test total_facturado
En todo el periodo de datos: 244275.89000000028
Desde 1 de febrero de 2022 hasta 28 de febrero de 2022: 19098.12
Desde 1 de febrero de 2022 (fecha final None): 221532.13000000015
Hasta 28 de febrero de 2022 (fecha inicio None): 41841.88
```

---

#### 3. `reservas_mas_largas`

Devuelve las *n* tuplas `(nombre, fecha_entrada)` correspondientes a las reservas con mayor duración.

```python
def reservas_mas_largas(reservas: list[Reserva], n: int = 3) -> list[tuple[str, date]]:
```

**Resultado esperado:**
```
Test reservas_mas_largas
Con n = 3: [('Laura López', datetime.date(2022, 1, 2)), ('Sofía García', datetime.date(2022, 1, 2)), ('Miguel Sánchez', datetime.date(2022, 1, 2))]
```

---

#### 4. `cliente_mayor_facturacion`

Devuelve el cliente (DNI) con mayor facturación, considerando solo reservas con ciertos servicios adicionales.

```python
def cliente_mayor_facturacion(reservas: list[Reserva], 
                              servicios: set[str] | None = None) -> tuple[str, float]:
```

**Resultado esperado:**
```
Test cliente_mayor_facturacion
Sin filtrar por servicios: ('63550791C', 3893.2200000000003)
Con Parking: ('71828448T', 3008.17)
Con Parking o Spa: ('38747931S', 3216.0699999999997)
```

---

#### 5. `servicios_estrella_por_mes`

Indica, para cada mes, el servicio adicional más solicitado entre los tipos de habitación indicados.

```python
def servicios_estrella_por_mes(reservas: list[Reserva], 
                               tipos_habitacion: set[str] | None = None
                               ) -> dict[str, str]:
```

**Resultado esperado:**

```
Test servicios_estrella_por_mes
Todos los tipos de habitación:
    ('Enero', 'Parking')
    ('Febrero', 'Gimnasio')
    ('Marzo', 'Parking')
    ('Abril', 'Gimnasio')
    ('Mayo', 'Gimnasio')
    ('Junio', 'Parking')
    ('Julio', 'Gimnasio')
    ('Agosto', 'Gimnasio')
    ('Septiembre', 'Piscina')
    ('Octubre', 'Spa')
    ('Noviembre', 'Gimnasio')
    ('Diciembre', 'Parking')

Habitación familiar o deluxe:
    ('Enero', 'Gimnasio')
    ('Febrero', 'Gimnasio')
    ('Marzo', 'Gimnasio')
    ('Abril', 'Gimnasio')
    ('Mayo', 'Gimnasio')
    ('Junio', 'Spa')
    ('Julio', 'Gimnasio')
    ('Agosto', 'Parking')
    ('Septiembre', 'Piscina')
    ('Octubre', 'Gimnasio')
    ('Noviembre', 'Gimnasio')
    ('Diciembre', 'Gimnasio')
```

---

#### 6. `media_dias_entre_reservas`

Calcula la media de días entre cada dos reservas consecutivas en el tiempo.

```python
def media_dias_entre_reservas(reservas: list[Reserva]) -> float:
```

**Resultado esperado:**
```
Test media_dias_entre_reservas
0.7353535353535353
```

---

#### 7. `cliente_reservas_mas_seguidas`

Devuelve el DNI y la media de días entre reservas consecutivas del cliente con al menos `min_reservas` y menor media de días entre reservas.

```python
def cliente_reservas_mas_seguidas(reservas: list[Reserva], min_reservas: int) -> str:
```

**Resultado esperado:**
```
Test cliente_reservas_mas_seguidas
El DNI del cliente con al menos 5 reservas y menor media de días entre reservas consecutivas es 88681493W, con una media de días entre reservas de 9.75.
```

