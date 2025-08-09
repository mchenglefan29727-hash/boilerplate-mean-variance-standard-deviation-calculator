import numpy as np # type: ignore

def calculate(numbers):
    # Check length
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert to 3x3 numpy array
    arr = np.array(numbers).reshape(3, 3)

    # Helper to compute statistics and convert to Python lists
    def get_stats(func):
        return [
            func(arr, axis=0).tolist(),
            func(arr, axis=1).tolist(),
            func(arr).item() if np.isscalar(func(arr)) else func(arr).tolist()
        ]
    
    return {
        'mean': get_stats(np.mean),
        'variance': get_stats(np.var),
        'standard deviation': get_stats(np.std),
        'max': get_stats(np.max),
        'min': get_stats(np.min),
        'sum': get_stats(np.sum)
    }
