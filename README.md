# Basic project on MicroPython for ESP32 board

[MicroPython](http://docs.micropython.org/en/latest/index.html)

Install
* USB driver for ESP32 board
  * [FTDI](https://www.ftdichip.com/Drivers/VCP.htm)
  * [Silicon Labs](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
* Connect the board to the computer and find its USB path
```
$ls /dev/cu*
/dev/cu.SLAB_USBtoUART

$ls /dev/ttyUSB*
/dev/ttyUSB0
```
* [rshell](https://pypi.org/project/rshell/) - Remote MicroPython shell
* IntelliJ [PyCharm](https://www.jetbrains.com/pycharm/)
* IntelliJ PyCharm plugin [MicroPython](https://github.com/vlasovskikh/intellij-micropython)
## Optionally
* Install [MicroPython](https://github.com/micropython/micropython)
* Install [upip](https://pypi.org/project/micropython-upip/) - MicropPython package manager
* Install Telnet client
* Install FarManager ([Linux, MacOS](https://github.com/elfmz/far2l), [Windows](https://www.farmanager.com/)). It has very good FTP client.

##Workflow
*In PyCharm - create a new Pure Python project
