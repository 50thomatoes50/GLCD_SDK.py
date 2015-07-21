import os, time,PIL, Image, ImageDraw, timeit, itertools, GLCD_SDK, platform

GLCD_SDK.initDLL("C:\\Program Files\\Logitech Gaming Software\\LCDSDK\\LCDSDK_8.57.148\\Lib\\GameEnginesWrapper\\x86\\LogitechLcdEnginesWrapper.dll")
GLCD_SDK.LogiLcdInit("Python",GLCD_SDK.TYPE_COLOR+GLCD_SDK.TYPE_MONO)
if GLCD_SDK.LogiLcdIsConnected(GLCD_SDK.TYPE_COLOR):
    GLCD_SDK.LogiLcdColorSetTitle(GLCD_SDK.NAME+" "+GLCD_SDK.VERSION,255,255,255)
    GLCD_SDK.LogiLcdColorSetText(0,"Python"+platform.python_version(),255,255,255)
    GLCD_SDK.LogiLcdColorSetText(1,platform.platform()+" "+platform.uname()[4],255,255,255)
    #GLCD_SDK.LogiLcdColorSetText(2,platform.uname()[0]+" "+platform.uname()[2]+" ("+platform.uname()[3]+" "+platform.uname()[4]+")",255,255,255)
    GLCD_SDK.LogiLcdColorSetText(2,platform.uname()[1],255,255,255)
    #GLCD_SDK.LogiLcdColorSetText(4,"uname"+platform.uname(),255,255,255)
    #GLCD_SDK.LogiLcdColorSetText(5,"version"+platform.version(),255,255,255)
    im = Image.new("RGBA", (320, 240), "Black")
    draw = ImageDraw.Draw(im)
    
if GLCD_SDK.LogiLcdIsConnected(GLCD_SDK.TYPE_MONO):
    GLCD_SDK.LogiLcdMonoSetText(0,GLCD_SDK.NAME+" "+GLCD_SDK.VERSION)
    GLCD_SDK.LogiLcdMonoSetText(1,"Python"+platform.python_version())
    GLCD_SDK.LogiLcdMonoSetText(2,platform.platform()+" "+platform.uname()[4])
    GLCD_SDK.LogiLcdMonoSetText(3,platform.uname()[1])
GLCD_SDK.LogiLcdUpdate()

if not(GLCD_SDK.LogiLcdIsConnected(GLCD_SDK.TYPE_COLOR)) and not(GLCD_SDK.LogiLcdIsConnected(GLCD_SDK.TYPE_MONO)):
    print "Could not connect to a logitch LCD"
    os.exit(-1)
i=0
time.sleep(20) 
if GLCD_SDK.LogiLcdIsConnected(GLCD_SDK.TYPE_COLOR):
    while i< 320:
        draw.line((i, 0, i,240), fill=(0,0,255,255))
        start_fps = timeit.default_timer()
        GLCD_SDK.ColorBGPIL(im)
        GLCD_SDK.LogiLcdColorSetText(7,"FPS:"+str(1/(timeit.default_timer()-start_fps)),255,255,255)
        GLCD_SDK.LogiLcdUpdate()
        i+=1
time.sleep(5)        
GLCD_SDK.LogiLcdShutdown()

