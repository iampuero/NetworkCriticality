# Criticalidad en osciladores de kuramoto

$$d\theta_i/dt = \omega_i +- \sum_{i\neq j}C_{ji}(\theta_i-\theta_j)$$ 

```
T = 100
dt = 0.01
omega_0 = ~10 * 2pi #explorar rango de omega0 
```

Ver el efecto de la varianza del omega0
Además de agregar ruido después

[ ] Conectividad de tipo lattice 1D redondo simétrico (netwokrx cycle), o de grado 2-3 (conectadas con los vecinos, +g en subdiagonales)



## Plot
[ ] Sincronia de fase v/s G (sea g el valor de conexion de los nodos)
- Se espera una curva sigmoidal

[x] realizar wrapping de fase

[ ] Correlaciones entre nodos vecinos espaciotemporal en el punto critico
- Sincronía de a pares v/s distancia?
-
[ ] Graficar metaestaibilidad v/s g

## Extras
[ ] Tratar como interactivo y guardar resultados previos en base a nombreconvencion
[ ] Crearfuncion para carga si existe
[ ] Explorar distintos números de nodos
[ ] Usar/Crear perfilador
[ ] Definir modelo POO

## Siguientes
- Post esto WiCo