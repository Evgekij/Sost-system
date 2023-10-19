import data
import show

def main():
    cpu_percent = data.cpu_percent()
    show.show_cpu_percent(cpu_percent)
    percent_memory = data.percent_memory()
    show.show_mem_percent(percent_memory)
    cpu_times = data.cpu_times()
    show.show_cpu_times(cpu_times)
    cpu_freq = data.cpu_freq()
    show.show_cpu_freq(cpu_freq)
    virt_mem = data.virt_memory()
    show.show_virtual_memory(virt_mem)


main()