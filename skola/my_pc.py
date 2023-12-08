import platform
import psutil
import os

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    
my_system = platform.uname()
print(style.RED + "========================================================================" + style.END)
print(style.BLUE + "                               ZAŘÍZENÍ")
print(style.RED + "========================================================================" + style.END)
print(f"název zařízení: {my_system.node}")
print(f"typ zařízení: {my_system.machine}")
print(f"typ Procesoru: {my_system.processor}")
print(style.RED + "========================================================================" + style.END)
print(style.BLUE + "                           OPERAČNÍ SYSTÉM")
print(style.RED + "========================================================================" + style.END)
print(f"operační systém: {my_system.system}")
print(f"druh operačního systému: {my_system.release}")
print(f"konkrétní druh operačního systému: {my_system.version}")
print(style.RED + "========================================================================" + style.END)
print(style.BLUE + "                                JÁDRA")
print(style.RED + "========================================================================" + style.END)
print(f"počet fyzických jader: {psutil.cpu_count(logical=False)}")
print(f"počet logických jader: {psutil.cpu_count(logical=True)}")
print(style.RED + "========================================================================" + style.END)
print(style.BLUE + "                                 CPU")
print(style.RED + "========================================================================" + style.END)
print(f"stálá CPU frekvence: {psutil.cpu_freq().current}")
print(f"Minimální CPU frekvence: {psutil.cpu_freq().min}")
print(f"Maximální CPU frekvence: {psutil.cpu_freq().max}")
print(style.RED + "========================================================================" + style.END)
print(style.BLUE + "                                 RAM")
print(style.RED + "========================================================================" + style.END)
print(f"celá pamět RAM: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
print(f"Dostupná RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
print(f"použitá RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
print(f"Využití RAM: {psutil.virtual_memory().percent}%")
print(style.RED + "========================================================================" + style.END)