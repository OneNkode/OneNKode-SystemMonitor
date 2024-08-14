import psutil
import platform
import GPUtil
import time
import os

RESET = '\033[0m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
is_nvidia = None

os.system("title .:SS:. - SuperSpecs - Made by NDXCode && mode 40,32")

def get_system_info():
    global is_nvidia
    os_info = platform.system() + " " + platform.release()
    cpu_info = platform.processor()
    num_cores = psutil.cpu_count(logical=True)
    total_ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # GB
    gpus = GPUtil.getGPUs()
    gpu_info = gpus[0].name if gpus else "No GPU found"
    if "nvidia" in gpu_info.lower():
        is_nvidia = True
    else:
        is_nvidia = False
    gpu_info = gpu_info.replace("NVIDIA", f"{GREEN}NVIDIA{RESET}").replace("AMD", f"{RED}AMD{RESET}").replace("INTEL", f"{BLUE}INTEL{RESET}")
    
    return os_info, cpu_info, num_cores, total_ram, gpu_info

def get_disk_usage():
    disk_info = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append(f"{GREEN}{partition.device}{RESET} {CYAN}{usage.percent}%{RESET} used of {BLUE}{round(usage.total / (1024 ** 3), 2)} GB{RESET}")
        except Exception:
            pass
    return "\n".join(disk_info)

def get_network_io():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def display_static_info():
    os_info, cpu_info, num_cores, total_ram, gpu_info = get_system_info()
    disk_usage = get_disk_usage()

    print(f"{BLUE}========================================\n{RESET}")
    print(f"{RED}          .:SS:. - SuperSpecs           {RESET}")
    print(f"{BLUE}========================================\n{RESET}")
    print(f"{BLUE}========================================{RESET}")
    print(f"{YELLOW}Operating System:{RESET} {os_info}")
    print(f"{YELLOW}CPU:{RESET} {cpu_info}")
    print(f"{YELLOW}Number of Cores:{RESET} {num_cores}")
    print(f"{YELLOW}Total RAM:{RESET} {total_ram} GB")
    print(f"{YELLOW}GPU:{RESET} {gpu_info}")
    print(f"{BLUE}========================================\n\n{RESET}")
    print(f"{BLUE}========================================{RESET}")
    print(f"{YELLOW}Disk Usage:{RESET}")
    print(disk_usage)
    print(f"{BLUE}========================================\n{RESET}")
    if is_nvidia:
        print(f"{BLUE}========================================\n\n\n\n\n\n\n{RESET}")
    else:
        print(f"{BLUE}========================================\n\n\n\n\n{RESET}")

def display_dynamic_info(prev_sent, prev_recv):
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    #print(f"asdadsasdadsads    -- - - -      {is_nvidia}")
    if is_nvidia:
        GPUs = GPUtil.getGPUs()
        load = int(GPUs[0].load*100)
        temp = GPUs[0].temperature

    if int(cpu_usage) <= 49:
        cpu_usage = f"{GREEN}{cpu_usage}{RESET}"
    elif int(cpu_usage) > 49 and int(cpu_usage) < 75:
        cpu_usage = f"{YELLOW}{cpu_usage}{RESET}"
    elif int(cpu_usage) > 74 and int(cpu_usage) < 100:
        cpu_usage = f"{RED}{cpu_usage}{RESET}"

    if int(mem_usage) <= 49:
        mem_usage = f"{GREEN}{mem_usage}{RESET}"
    elif int(mem_usage) > 49 and int(mem_usage) < 75:
        mem_usage = f"{YELLOW}{mem_usage}{RESET}"
    elif int(mem_usage) > 74 and int(mem_usage) < 100:
        mem_usage = f"{RED}{mem_usage}{RESET}"

    if int(load) <= 49:
        load = f"{GREEN}{load}{RESET}"
    elif int(load) > 49 and int(load) < 75:
        load = f"{YELLOW}{load}{RESET}"
    elif int(load) > 74 and int(load) < 100:
        load = f"{RED}{load}{RESET}"

    if int(temp) <= 35:
        temp = f"{GREEN}{temp}{RESET}"
    elif int(temp) > 35 and int(temp) < 60:
        temp = f"{YELLOW}{temp}{RESET}"
    elif int(temp) > 60 and int(temp) < 100:
        temp = f"{RED}{temp}{RESET}"
    
    curr_sent, curr_recv = get_network_io()
    net_sent = (curr_sent - prev_sent) / (1024 ** 2)
    net_recv = (curr_recv - prev_recv) / (1024 ** 2)
    
    print(f"{CYAN}{UNDERLINE}CPU Usage:{RESET}{RESET} {cpu_usage}%      ")
    print(f"{CYAN}{UNDERLINE}Memory Usage:{RESET}{RESET} {mem_usage}%      ")
    print(f"{CYAN}{UNDERLINE}GPU Usage:{RESET}{RESET} {load}%      ")
    print(f"{CYAN}{UNDERLINE}GPU Temp:{RESET}{RESET} {temp} °C      ")
    print(f"{CYAN}{UNDERLINE}Network Sent:{RESET}{RESET} {net_sent:.2f} MB/s      ")
    print(f"{CYAN}{UNDERLINE}Network Received:{RESET}{RESET} {net_recv:.2f} MB/s      ")
    print(f"{BLUE}========================================{RESET}")
    return curr_sent, curr_recv

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    display_static_info()
    prev_sent, prev_recv = get_network_io()
    while True:
        if is_nvidia:
            print("\033[F\033[F\033[F\033[F\033[F\033[F\033[F", end="")
        else:
            print("\033[F\033[F\033[F\033[F\033[F", end="")
        prev_sent, prev_recv = display_dynamic_info(prev_sent, prev_recv)
        time.sleep(1)