---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
marp: true



---

# Criticalidad en osciladores de kuramoto

---
Modelo:
$$d\theta_i/dt = \omega_i + \sum_{i\neq j}C_{ji}(\theta_i-\theta_j)$$ 

Parámetros
```
std(omega_0) = 0.05
dt = 0.01
N = [200,300,500,800,1000,1500,2000]
G = 0-0.012    500 steps
```
---


- Conectividad de tipo lattice 1D redondo simétrico y aleatorio con igual densidad de conexiones
- Encontrar punto de inflexión de R y metaestabilidad

### Plots
- [x] Sincronia de fase v/s G (sea g el valor de conexion de los nodos)
    - Se espera una curva sigmoidal
- [x] Graficar metaestabilidad v/s g

---
**Lattice 1D CM**
![image w:350px](plots/grmeta_log_latt_8_2000.png)![w:350px](plots/grmeta_log_latt_8_300.png)![image w:350px](plots/grmeta_log_latt_8_500.png)
![image w:350px](plots/grmeta_log_latt_8_800.png)![w:350px](plots/grmeta_log_latt_8_1000.png)![image w:350px](plots/grmeta_log_latt_8_1500.png)

---
**Random CM**
![image w:350px](plots/grmeta_log_rand_8_2000.png)![w:350px](plots/grmeta_log_rand_8_300.png)![image w:350px](plots/grmeta_log_rand_8_500.png)
![image w:350px](plots/grmeta_log_rand_8_800.png)![w:350px](plots/grmeta_log_rand_8_1000.png)![image w:350px](plots/grmeta_log_rand_8_1500.png)

---

### Observaciones
* Se ven curvas sigmoidales en R pero no en meta
* Los rangos del desarrollo de curva depende de N y std
  * Se recorren N y G


---
## Extras
- [x] Perfilador -> Sacct para sobre 30 segundos
- [x] Modelo POO
    - Class Kuramoto
    - Class Simulator
---
## Siguientes
- Post esto WiCo

