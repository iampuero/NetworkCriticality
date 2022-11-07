# Criticalidad en osciladores de kuramoto

$$d\theta_i/dt = \omega_i +- \sum_{i\neq j}C_{ji}(\theta_i-\theta_j)$$ 

```
T = 100
dt = 0.01
omega_0 = ~10 * 2pi #explorar rango de omega0 
```


Ver el efecto de la varianza del omega0
Además de agregar ruido después

[x] Conectividad de tipo lattice 1D redondo simétrico (netwokrx cycle), o de grado 2-3 (conectadas con los vecinos, +g en subdiagonales)
[x] Fijar Seed
[x] Encontrar punto de inflexión de R y meta
[x] Probar con nodos 100,500,1000

### Observaciones
* Linear no muestra una curva facilmente
* Random genera punto de inflexión
* Rango de G depende mucho de N y std de $\omega0$
* Valores muy pequeños de G para, alto N de lattice1d y probabilidad de conexión en random



## Plot
- [x] Sincronia de fase v/s G (sea g el valor de conexion de los nodos)
    - Se espera una curva sigmoidal
- [x] Graficar metaestabilidad v/s g
- [?] Correlaciones entre nodos vecinos espaciotemporal en el punto critico
    - Sincronía de a pares v/s distancia?

## Extras
- [x] Guardar resultado en base a nombre/convencion
    - asdasd
- [x] Crearfuncion para carga si existe 
- [x] Perfilador -> Sacct para sobre 30 segundos
- [x] Modelo POO
    - Class Kuramoto
    - Class Simulator


Densidad: subir un poco la densidad?? Explorar
Definiciones de distancia entre nodos
Utilizar logspace con $G ~100 10^-1
Prune N500 para arriba

## Siguientes
- Post esto WiCo