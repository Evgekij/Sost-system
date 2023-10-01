import psutil
"""cput = psutil.cpu_times(percpu = False) #Время работы процессора

cpuper = psutil.cpu_percent(interval=1, percpu=True) #Загрузка процессора в процентах


stats = psutil.cpu_stats() #Статистика ЦП

cpuf = psutil.cpu_freq(percpu=False) #Частота ЦП

getl = psutil.getloadavg() #Средняя загрузка системы за последние 1, 5, 15 минут

boott = psutil.boot_time() #время загрузки системы в секундах с начала эпохи

virtm = psutil.virtual_memory() #статистика использования системной памяти

swapm = psutil.swap_memory() #статистика памяти подкачки системы

netcoun = psutil.net_io_counters(pernic=False, nowrap=True)"""

"""def cpu_percent():
    data = psutil.cpu_percent(interval= 1,percpu=False)
    cpu1 = {data}
  
    return cpu1



def cpu_times():
    data = psutil.cpu_times(percpu=False)
    cpu2 = {data[0], data[1], data[2], data[3], data[4]}
    
    return cpu2


def cpu_freq():
    data = psutil.cpu_freq(percpu=False)
    cpu3 = {"current=":data[0], "min=":data[1], "max=":data[2]}
    
    return cpu3


def virt_memory():
    data = psutil.virtual_memory()
    mem1 = {"total":data[0], "available":data[1], "percent":data[2], "used":data[3], "free":data[4]}

    return mem1
    

print(cpu_percent())"""



def cpu_percent():
    data = psutil.cpu_percent(interval= 1,percpu=False)
    cpu1 = {data}
  
    return cpu1
a= cpu_percent

def cpu_times():
    data = psutil.cpu_times(percpu=False)
    cpu2 = {"user":data[0], "system":data[1], "idle":data[2], "interrupt":data[3], "dpc":data[4]}
    
    return cpu2

def cpu_freq():
    data = psutil.cpu_freq(percpu=False)
    cpu3 = {"current":data[0], "min":data[1], "max":data[2]}
    
    return cpu3

def virt_memory():
    data = psutil.virtual_memory()
    mem1 = {"total":data[0], "available":data[1], "used":data[3], "free":data[4]}

    return mem1

def percent_memory():
    data = psutil.virtual_memory()
    mem2 = {data[2]}
    
    return mem2

def show_mem_percent():
    for el in percent_memory():
       print("\nСвободная память ПК:", el,"%") 

def show_cpu_percent(a):
    for el in a:
        print( "\nТекущая загрузка ЦП:", el, "%")

def show_cpu_times():
    print("\nВремя работы ЦП:")
    for key,value in cpu_times().items():
        print(f"{key:10}:{value:0.3f}""s.")

def show_cpu_freq():
    print("\nЧастота работы ЦП:")
    for key,value in cpu_freq().items():
        print(f"{key:10}:{value:10}", "GHz")       

def show_virtual_memory():
    print("\nОбщее состояние памяти:")
    for key,value in virt_memory().items():
        print(f"{key:10}:{value:10}","bytes")

def show_proc():
    for proc in psutil.process_iter(["pid","name","username"]):
       res=str(proc.info)
       
       
       print(f"{res:200}")

def main():
    print("\n{:>45}".format("Состояние системы:"))
    show_cpu_percent(a())
    show_mem_percent()
    show_cpu_freq()
    show_cpu_times()
    show_virtual_memory()
    print("\n{:>50}".format("Список запущенных процессов:"))
    show_proc()
main()