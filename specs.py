import platform
import GPUtil
import os
import psutil  # Added for CPU and memory usage
from datetime import datetime
import time

# Color codes for terminal
RESET = '\033[0m'
COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bold': '\033[1m',
    'underline': '\033[4m',
}

def color_text(text, color):
    return f"{COLORS[color]}{text}{RESET}"

def init_screen():
    os.system("title .:SS:. - SuperSpecs - Made by OneNKode" if os.name == 'nt' else "echo -e '\033]0;.:SS:. - SuperSpecs - Made by OneNKode\a'")
    os.system('cls' if os.name == 'nt' else 'clear')

def get_cpu_info():
    cpu_info = platform.processor()
    num_cores = os.cpu_count()
    return cpu_info, num_cores

def get_ram_info():
    total_ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    return round(total_ram, 2)

def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total = usage.total / (1024 ** 3)  # GB
            usage_percent = usage.percent
            disk_info.append(f"{color_text(partition.device, 'green')} {color_text(usage_percent, 'cyan')}% used of {color_text(round(total, 2), 'blue')} GB")
        except PermissionError:
            continue
    return "\n".join(disk_info)

def get_network_io():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    return bytes_sent, bytes_recv

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        gpu_info = gpu.name.replace("NVIDIA", color_text("NVIDIA", 'green'))\
                           .replace("AMD", color_text("AMD", 'red'))\
                           .replace("INTEL", color_text("INTEL", 'blue'))
        return gpu_info, True
    else:
        return "No GPU Found", False

def display_static_info():
    os_info = f"{platform.system()} {platform.release()}"
    cpu_info, num_cores = get_cpu_info()
    total_ram = get_ram_info()
    disk_usage = get_disk_usage()
    gpu_info, is_nvidia = get_gpu_info()

    header = f"{color_text('.:SS:. - SuperSpecs - by OneNKode', 'red')}"
    separator = color_text("=" * 50, 'blue')

    static_info = (
        f"{separator}\n{header}\n{separator}\n\n"
        f"{color_text('Operating System:', 'yellow')} {os_info}\n"
        f"{color_text('CPU:', 'yellow')} {cpu_info} ({num_cores} cores)\n"
        f"{color_text('Total RAM:', 'yellow')} {total_ram} GB\n"
        f"{color_text('GPU:', 'yellow')} {gpu_info}\n\n"
        f"{separator}\n{color_text('Disk Usage:', 'yellow')}\n{disk_usage}\n{separator}"
    )
    print(static_info)
    return is_nvidia

def display_dynamic_info(is_nvidia, prev_sent, prev_recv):
    # Dynamic CPU usage and RAM usage
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    if is_nvidia:
        gpu = GPUtil.getGPUs()[0]
        gpu_load = int(gpu.load * 100)
        gpu_temp = gpu.temperature
        gpu_mem_used = gpu.memoryUsed
        gpu_mem_total = gpu.memoryTotal
    else:
        gpu_load, gpu_temp, gpu_mem_used, gpu_mem_total = "N/A", "N/A", "N/A", "N/A"

    # Get current network I/O
    curr_sent, curr_recv = get_network_io()
    net_sent = (curr_sent - prev_sent) / (1024 ** 2)  # Convert to MB
    net_recv = (curr_recv - prev_recv) / (1024 ** 2)

    # Print dynamic info and move the cursor back up to overwrite on the next loop
    print(
        f"{color_text('CPU Usage:', 'cyan')} {cpu_usage}%     \n"
        f"{color_text('RAM Usage:', 'cyan')} {ram_usage}%     \n"
        f"{color_text('GPU Usage:', 'cyan')} {gpu_load}%      \n"
        f"{color_text('GPU Temp:', 'cyan')} {gpu_temp} °C     \n"
        f"{color_text('GPU Memory:', 'cyan')} {gpu_mem_used}/{gpu_mem_total} MB     \n"
        f"{color_text('Network Sent:', 'cyan')} {net_sent:.2f} MB                   \n"
        f"{color_text('Network Received:', 'cyan')} {net_recv:.2f} MB               \n"
        f"{color_text('=' * 50, 'blue')}"
    )
    print(f"\033[F" * 8, end="")  # Move cursor up 7 lines to overwrite 

    return curr_sent, curr_recv

if __name__ == "__main__":
    init_screen()
    is_nvidia = display_static_info()
    prev_sent, prev_recv = get_network_io()
    
    while True:
        time.sleep(1)  # Sleep before updating
        prev_sent, prev_recv = display_dynamic_info(is_nvidia, prev_sent, prev_recv)
