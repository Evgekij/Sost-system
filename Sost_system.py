import psutil


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
        i = 0
        for key,value in (proc.info).items():
            if i != 2:
                print(f"{key:<5}:{value:<30}", end=" ")
            i +=1
        else:
            print(f"{key:<5}:{value:<30}")
            i = 0

def main():
    print("\n{:>45}".format("Состояние системы:"))
    show_cpu_percent(a())
    show_mem_percent()
    show_cpu_freq()
    show_cpu_times()
    show_virtual_memory()
    print("\n{:>55}".format("Список запущенных процессов:"))
    show_proc()
main()