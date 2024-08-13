from pynvml import *

# Initialize the NVIDIA Management Library
nvmlInit()

# Get the number of available NVIDIA GPUs
def get_gpu_count():
    return nvmlDeviceGetCount()

# Get a handle to a specific GPU
def get_gpu_handle(gpu_id):
    return nvmlDeviceGetHandleByIndex(gpu_id)

# Get memory information for a specific GPU
def get_gpu_memory_info(handle):
    return nvmlDeviceGetMemoryInfo(handle)

# Example usage
try:
    # Get the number of GPUs
    num_gpus = get_gpu_count()
    print(f"Number of GPUs: {num_gpus}")

    for i in range(num_gpus):
        # Get the handle for each GPU
        handle = get_gpu_handle(i)
        
        # Get memory info for the GPU
        memory_info = get_gpu_memory_info(handle)
        
        # Print memory info
        print(f"\nGPU {i}:")
        print(f"Total memory: {memory_info.total / (1024**3):.2f} GB")
        print(f"Free memory: {memory_info.free / (1024**3):.2f} GB")
        print(f"Used memory: {memory_info.used / (1024**3):.2f} GB")

finally:
    # Shut down the NVIDIA Management Library
    nvmlShutdown()