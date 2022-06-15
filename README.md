# Mach Eight Sample Project
Una herramienta escrita para la terminal que, dada una altura en pulgadas, busca en una lista de jugadores los pares que sumen esa altura.

## Dependencias
- Python3
- python3-pip
- [poetry](https://github.com/python-poetry/poetry)

## Instalación (Probado en Mac y Linux)
Ambos comandos (para Mac, Linux y Windows) instalan una aplicación en la terminal.  Es importante que después de la instalación, para usarla se inicie una sesión nueva de la terminal.

```bash
make install
```
## Instalación en windows (se necesita ejecutar como administrador)
```
Setup.ps1
```

## Uso
La implementación usa un algoritmo con notación <b>O($n^2 \over 2$)</b>, reduciendo a la mitad la notación mínima esperada.
```bash
~ ❯ nba 139
- Brevin Knight		Nate Robinson
- Nate Robinson		Mike Wilks
```

## Ayuda
```bash
~ ❯ nba -h
usage: nba [target]

argumentos posicionales:
  target      El tamaño debe ser un número entero en pulgadas

argumentos opcionales:
  -h, --help  Mostrar este mensaje de ayuda
```