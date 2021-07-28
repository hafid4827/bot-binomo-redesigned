# auto binomo

### sponsors

- VICTALEJO

## USO

- pip install selenium
- python pruebas.py

`Dentro Estaran Todos Los Ejemplos Y Metodos A Usar`

```
from binomo import apiAlfaBinomo
if __name__ == '__main__':
    aApiAlfa = apiAlfaBinomo('','', timeBotWait = 120, loginError = True) # timeBotWait 120seg (tiempo de espera hasta resolver el capcha), loginError True
    aApiAlfa.actionDV('EURUSD') # par
    aApiAlfa.buy("CALL") # compra o venta (PUT)
    aApiAlfa.mount(3000) # 3000,15000,30000,60000,150000,300000,600000,3000000 montos de compra
    aApiAlfa.timeBuy(1) # 1,2,3,4,5 minutos
    print(aApiAlfa.listOder()) # lista de activos y su profit
```
