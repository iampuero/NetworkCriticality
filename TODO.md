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

- [?] Correlaciones entre nodos vecinos espaciotemporal en el punto critico
    - Sincronía de a pares v/s distancia?
- [x] Graficar metaestabilidad v/s g

## Extras
- [x] Tratar como interactivo y guardar resultados previos en base a nombreconvencion
- [x] Crearfuncion para carga si existe
- [x] Explorar distintos números de nodos 
- [x] Usar/Crear perfilador -- _Tiempos por mientras_
- [x] Definir modelo POO

## Siguientes
- Post esto WiCo