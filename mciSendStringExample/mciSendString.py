import ctypes
from time import sleep
def Main():
    winmm = ctypes.WinDLL("Winmm.dll")
    Kernel32 = ctypes.WinDLL("Kernel32.dll")
    winmm.mciSendStringA(bytes("play Ex.mp3 repeat", "utf-8"), 0, 0, 0)
    Kernel32.SetConsoleTitleA(bytes("mciSendString by RiritoXXL", "utf-8"))
    while True:
        sleep(3200)

if __name__ == "__main__":
    Main()