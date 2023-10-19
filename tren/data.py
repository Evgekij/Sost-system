import psutil
from decor import caller


@caller("cpu_percent.json")
def cpu_percent():
    data = psutil.cpu_percent(interval= 1, percpu=False)
    cpu1 = str(data)
  
    return cpu1

@caller("cpu_times.json")
def cpu_times():
    data = psutil.cpu_times(percpu=False)
    cpu2 = {"user":data[0], "system":data[1], "idle":data[2], "interrupt":data[3], "dpc":data[4]}
    
    return cpu2

@caller("cpu_freq.json")
def cpu_freq():
    data = psutil.cpu_freq(percpu=False)
    cpu3 = {"current":data[0], "min":data[1], "max":data[2]}
    
    return cpu3

@caller("virtual_memory.json")
def virt_memory():
    data = psutil.virtual_memory()
    mem1 = {"total":data[0], "available":data[1], "used":data[3], "free":data[4]}

    return mem1

@caller("percent_memory.json")
def percent_memory():
    mem2 = psutil.virtual_memory()[2]
    
    return mem2

