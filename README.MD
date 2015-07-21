# GLCD SDK ![Build Travis](https://api.travis-ci.org/50thomatoes50/GLCD_SDK.py.svg "")
A Python wrapper for Logitech's LCD SDK

## Screenshot
![Screenshot1](https://raw.github.com/50thomatoes50/GLCD_SDK.py/master/Screenshot/2.png "")
![Screenshot2](https://raw.github.com/50thomatoes50/GLCD_SDK.py/master/Screenshot/1.png "")

## Requirement
- A Logitech periphral with an LCD (G19,G510,G13,G15 ...)
- Logitech Gaming Software
- LCDSDK for Logitech (Version 8.57.148 or newer)

##Instalation
Use package installer on Pypi.

## Usage
First load the LogitechLcdEnginesWrapper dll
```
GLCD_SDK.initDLL("C:\\Program Files\\Logitech Gaming Software\\LCDSDK\\LCDSDK_8.57.148\\Lib\\GameEnginesWrapper\\x86\\LogitechLcdEnginesWrapper.dll")
```

All function have the same name SDK. Except for Constants. Read LCDSDK_#.##.###\\Doc\\LogitechGamingLCDSDK.pdf
```
import GLCD_SDK, time
GLCD_SDK.initDLL("C:\\Program Files\\Logitech Gaming Software\\LCDSDK\\LCDSDK_8.57.148\\Lib\\GameEnginesWrapper\\x86\\LogitechLcdEnginesWrapper.dll")
GLCD_SDK.LogiLcdInit("Python",GLCD_SDK.TYPE_COLOR+GLCD_SDK.TYPE_MONO)
GLCD_SDK.LogiLcdColorSetText(0,"Python"+platform.python_version(),255,255,255)
GLCD_SDK.LogiLcdUpdate()
time.sleep(5)
GLCD_SDK.LogiLcdShutdown()
```
A bonus fonction to display PIL image on screen
```
GLCD_SDK.ColorBGPIL(im)
```
