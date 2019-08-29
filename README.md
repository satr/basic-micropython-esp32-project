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
* [rshell](https://pypi.org/project/rshell/) - Remote MicroPython shell ([GitHub](https://github.com/dhylands/rshell))
`pip install --user rshell`
* IntelliJ [PyCharm](https://www.jetbrains.com/pycharm/)
* IntelliJ PyCharm plugin [MicroPython](https://github.com/vlasovskikh/intellij-micropython)
## Optionally
* Install [MicroPython](https://github.com/micropython/micropython)
Get MicroPython source
```
cd ~ && mkdir dev && cd dev
git clone https://github.com/micropython/micropython.git
```
Build the cross-compiler
```
cd micropython/mpy-cross && make
```
Navigate back to the `micropython` folder
```
cd ..
```
Update submodules
```
git submodule update --init
```
Navigate to the Unix port folder and build the MicroPython
```
cd ports/unix
make
```
In case of an error _modffi.c:32:17: fatal error: ffi.h: No such file or directory_
Try the built MicroPython
```

```
* Install [upip](https://pypi.org/project/micropython-upip/) - MicropPython package manager
```
pip install micropython-upip
```
* Install Telnet client
* Install FarManager ([Linux, MacOS](https://github.com/elfmz/far2l), [Windows](https://www.farmanager.com/)). It has very good FTP client.

## Workflow
* In PyCharm - create a new Pure Python project
* Add PyCharm plugin MicroPython
![](images/pycharm-add-plugin-micropython.png)
* Set the project interpreter
![](images/pycharm-set-project-interpreter.png)
* Enable the MicroPython for the project
![](images/pycharm-enable-plugin-micropython-for-project.png)
* Add Run configurations - with Shell scripts
![](images/pycharm-add-run-configuration-run-rshell.png)
![](images/pycharm-add-configuration-upload-via-usb.png)
![](images/pycharm-add-configuartion-with-shell-script.png)
![](images/pycharm-add-configuration-run-repl.png)
* Start upload files with `rshell`
![](images/pycharm-start-upload-to-board-with-rshell.png)
