

def show_cpu_percent(name):
    print("\n{:>45}".format("Состояние системы:"))
    print( "\nТекущая загрузка ЦП:",name, "%")

def show_mem_percent(name):
    print("\nСвободно памяти:")
    print(f"{name}""%")
        
def show_cpu_times(name):
    print("\nВремя работы ЦП:")
    for key,value in name.items():
        print(f"{key:10}:{value:0.3f}""s.")

def show_cpu_freq(name):
    print("\nЧастота работы ЦП:")
    for key,value in name.items():
        print(f"{key:10}:{value:10}", "GHz")       

def show_virtual_memory(name):
    print("\nОбщее состояние памяти:")
    for key,value in name.items():
        print(f"{key:10}:{value:10}","bytes")

