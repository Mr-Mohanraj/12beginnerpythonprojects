import time
import psutil


print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)


def display(cpu_usage,memory_usage, bars=50):

    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = "#" * int(cpu_percent * bars) + "$" * (bars - int(cpu_percent * bars))

    mem_percent = (memory_usage / 100.0)
    mem_bar = "#" * int(mem_percent * bars) + "$" * (bars - int(cpu_percent * bars))

    print(f"\rCPU Usage : |{cpu_bar} | {cpu_usage:.2f}% ", end="")
    print(f"\rMEMORY Usage : |{mem_bar} | {memory_usage:.2f}% ", end="")



while True:
    display(psutil.cpu_percent(),psutil.virtual_memory().percent,1)
    time.sleep(0.5)
