# SmartClock
Un projecte personal que combina coneixements de diversos llenguatges i tecnologies.

## Objectius del projecte
Tindre un rellotge intel·ligent d'escriptori el qual tinga les següents funcions:
* Mostrar l'hora
* Rebre notificacions des d'un smartphone Android
* Control·lar la il·luminació d'unes peretes intel·ligents `Yeelight RGBW`
* Control·lar els paràmetres de l'aire acondicionat `Mitshubishi`

A més a més, incloure les mateixes funcions en altres interfícies, com per exemple:
* Pàgina web
* Aplicació Android
* Bot de Telegram

### Hardware
* Raspberry Pi 3
* Pantalla táctil HDMI+USB
* Arduino 
* Peretes Intel·ligents Yeelight RGBW
* Placa ESP32 
* Sensor de temperatura
* Emisor i receptor de infrarrojos

### Software
* Servidor web -> `python 3` + `bottle.py`
* Client Android -> `Java` + `Android`
* Client d'escriptori -> `python 3` + `pygobject` 
* Bot de telegram -> `python` + `python-telegram-bot`
* ESP32 -> `lua`
* Arduino firmware
