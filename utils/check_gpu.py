import torch
from pynvml import nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo, nvmlShutdown
from utils.param_enum import ModelParams

def get_model_params(model_name='llama3.1'):
    if model_name.lower() == 'llama3.1':
        return ModelParams.LLAMA_3_1_8B
    if model_name.lower() == 'llama3.1:70b':
        return ModelParams.LLAMA_3_1_70B
    if model_name.lower() == 'llama3.1:405b':
        return ModelParams.LLAMA_3_1_405B
    
def estimate_model_size(num_params, dtype=torch.float32):
    bytes_per_param = torch.finfo(dtype).bits // 8
    model_size_bytes = num_params * bytes_per_param
    model_size_gb = model_size_bytes / (1024**3)
    return model_size_gb

def get_gpu_memory():
    nvmlInit()
    gpu_memory = []
    num_gpus = nvmlDeviceGetCount()
    
    for i in range(num_gpus):
        handle = nvmlDeviceGetHandleByIndex(i)
        info = nvmlDeviceGetMemoryInfo(handle)
        gpu_memory.append({
            'total': info.total / (1024**3),
            'free': info.free / (1024**3),
            'used': info.used / (1024**3)
        })
    
    nvmlShutdown()
    return gpu_memory

def check_gpu_memory(model_params, dtype=torch.float32):
    model_size_gb = estimate_model_size(model_params, dtype)
    print(f"Estimated model size: {model_size_gb:.2f} GB")

    gpu_memory = get_gpu_memory()
    num_gpus = len(gpu_memory)
    print(f"Number of GPUs available: {num_gpus}")

    for i, mem in enumerate(gpu_memory):
        print(f"\nGPU {i}:")
        print(f"Total memory: {mem['total']:.2f} GB")
        print(f"Free memory: {mem['free']:.2f} GB")
        print(f"Used memory: {mem['used']:.2f} GB")
        
        if mem['free'] > model_size_gb:
            print(f"GPU {i} has enough memory to run the model.")
        else:
            print(f"GPU {i} does not have enough memory to run the model.")

    return gpu_memory, model_size_gb

def can_run_model(model_name, dtype=torch.uint8, multi_gpu=False):
    
    model_params = get_model_params(model_name).value

    gpu_memory, model_size_gb = check_gpu_memory(model_params, dtype)
    
    if multi_gpu:
        total_free_memory = sum(mem['free'] for mem in gpu_memory)
        if total_free_memory > model_size_gb:
            print(f"\nThe model can run using multiple GPUs (total free memory: {total_free_memory:.2f} GB)")
            return True
        else:
            print(f"\nThe model cannot run even with all GPUs combined (total free memory: {total_free_memory:.2f} GB)")
            return False
    else:
        if any(mem['free'] > model_size_gb for mem in gpu_memory):
            print("\nThe model can run on at least one GPU")
            return True
        else:
            print("\nThe model cannot run on any single GPU")
            return False

# Example usage
if __name__ == "__main__":
    model_params = 8000000000  # 1 billion parameters
    can_run = can_run_model(model_params, dtype=torch.float32, multi_gpu=True)
    print(f"Can run model: {can_run}")