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
* [**Raspberry Pi 3 Model B**](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/): ARM 4-Core CPU, 1 GB RAM, WiFi+BLE, 2xUSB, 40xGPIO
* **Pantalla táctil 5" HDMI+USB**
* **Arduino [Mini](https://store.arduino.cc/arduino-mini-05) o [Nano](https://store.arduino.cc/arduino-nano)**
* Peretes Intel·ligents [**Yeelight RGBW**](http://www.yeelight.com/en_US/product/wifi-led-c)
* [**WeMos LOLIN32**](https://wiki.wemos.cc/products:lolin32:lolin32): Placa ESP32 WiFi + BLE 
* [**WeMos D1 Mini**](https://wiki.wemos.cc/products:d1:d1_mini): Placa base ESP8266EX WiFi
* Sensor de temperatura
* Emisor i receptor de infrarrojos

### Software
* Servidor web -> `python 3` + `bottle.py`
* Client Android -> `Java` + `Android`
* Client d'escriptori -> `python 3` + `pygobject` 
* Bot de telegram -> `python` + `python-telegram-bot`
* ESP32 -> `lua`
* Arduino firmware
