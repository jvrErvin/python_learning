import timeit
import matplotlib.pyplot as plt
from tqdm import tqdm

# Define the sizes to test
sizes = [10, 100, 1000, 10000, 100000, 1000000]

# Define the number of iterations for timeit
iterations = 100

# Initialize dictionaries to store the timing results
results = {
    'list_zeros': [],
    'numpy_zeros': [],
    'list_addition': [],
    'numpy_addition': [],
    'list_multiplication': [],
    'numpy_multiplication': [],
    'list_power': [],
    'numpy_power': [],
    'list_dot_product': [],
    'numpy_dot_product': [],
    'list_sum': [],
    'numpy_sum': [],
    'list_sqrt': [],
    'numpy_sqrt': [],
    'list_mean': [],
    'numpy_mean': [],
    'list_std': [],
    'numpy_std': [],
}

# Measure the time for initialization with zeros
print('Working on initialization with zeros...')
for size in tqdm(sizes):
    list_zeros_time = timeit.timeit(f'[0] * {size}', number=iterations)
    numpy_zeros_time = timeit.timeit(f'np.zeros({size})', setup='import numpy as np', number=iterations)
    results['list_zeros'].append(list_zeros_time)
    results['numpy_zeros'].append(numpy_zeros_time)

# Measure the time for addition
print('Working on addition...')
for size in tqdm(sizes):
    list_setup = f'l1 = [1] * {size}; l2 = [2] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size}); n2 = np.ones({size}) * 2'
    
    list_addition_time = timeit.timeit('l3 = [x + y for x, y in zip(l1, l2)]', setup=list_setup, number=iterations)
    numpy_addition_time = timeit.timeit('n3 = n1 + n2', setup=numpy_setup, number=iterations)
    
    results['list_addition'].append(list_addition_time)
    results['numpy_addition'].append(numpy_addition_time)

# Measure the time for multiplication
print('Working on multiplication...')
for size in tqdm(sizes):
    list_setup = f'l1 = [1] * {size}; l2 = [2] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size}); n2 = np.ones({size}) * 2'
    
    list_multiplication_time = timeit.timeit('l3 = [x * y for x, y in zip(l1, l2)]', setup=list_setup, number=iterations)
    numpy_multiplication_time = timeit.timeit('n3 = n1 * n2', setup=numpy_setup, number=iterations)
    
    results['list_multiplication'].append(list_multiplication_time)
    results['numpy_multiplication'].append(numpy_multiplication_time)
    
# Measure the time for power
print('Working on power...')
for size in tqdm(sizes):
    list_setup = f'l1 = [2] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size}) * 2'
    
    list_power_time = timeit.timeit('l3 = [x ** 2 for x in l1]', setup=list_setup, number=iterations)
    numpy_power_time = timeit.timeit('n3 = np.power(n1, 2)', setup=numpy_setup, number=iterations)
    
    results['list_power'].append(list_power_time)
    results['numpy_power'].append(numpy_power_time)
    
# Measure the time for dot product
print('Working on dot product...')
for size in tqdm(sizes):
    list_setup = f'l1 = [1] * {size}; l2 = [2] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size}); n2 = np.ones({size}) * 2'

    list_dot_product_time = timeit.timeit('sum(x * y for x, y in zip(l1, l2))', setup=list_setup, number=iterations)
    numpy_dot_product_time = timeit.timeit('np.dot(n1, n2)', setup=numpy_setup, number=iterations)
    
    results['list_dot_product'].append(list_dot_product_time)
    results['numpy_dot_product'].append(numpy_dot_product_time)

# Measure the time for sum
print('Working on sum...')
for size in tqdm(sizes):
    list_setup = f'l1 = [1] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size})'

    list_sum_time = timeit.timeit('sum(l1)', setup=list_setup, number=iterations)
    numpy_sum_time = timeit.timeit('np.sum(n1)', setup=numpy_setup, number=iterations)
    
    results['list_sum'].append(list_sum_time)
    results['numpy_sum'].append(numpy_sum_time)

# Measure the time for square root
print('Working on square root...')
for size in tqdm(sizes):
    list_setup = f'l1 = [4] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size}) * 4'

    list_sqrt_time = timeit.timeit('[math.sqrt(x) for x in l1]', setup='import math; ' + list_setup, number=iterations)
    numpy_sqrt_time = timeit.timeit('np.sqrt(n1)', setup=numpy_setup, number=iterations)
    
    results['list_sqrt'].append(list_sqrt_time)
    results['numpy_sqrt'].append(numpy_sqrt_time)

# Measure the time for mean calculation
print('Working on mean...')
for size in tqdm(sizes):
    list_setup = f'l1 = [1] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size})'

    list_mean_time = timeit.timeit('sum(l1) / len(l1)', setup=list_setup, number=iterations)
    numpy_mean_time = timeit.timeit('np.mean(n1)', setup=numpy_setup, number=iterations)
    
    results['list_mean'].append(list_mean_time)
    results['numpy_mean'].append(numpy_mean_time)

# Measure the time for standard deviation calculation
print('Working on standard deviation...')
for size in tqdm(sizes):
    list_setup = f'l1 = [1] * {size}'
    numpy_setup = f'import numpy as np; n1 = np.ones({size})'
    mean_setup = 'mean = sum(l1) / len(l1)'
    list_std_time = timeit.timeit('math.sqrt(sum((x - mean) ** 2 for x in l1) / len(l1))',
                                  setup='import math; ' + list_setup + '; ' + mean_setup,
                                  number=iterations
    )
    numpy_std_time = timeit.timeit('np.std(n1)', setup=numpy_setup, number=iterations)
    
    results['list_std'].append(list_std_time)
    results['numpy_std'].append(numpy_std_time)


# Plotting the results
fig, axes = plt.subplots(9, 1, figsize=(14, 48))

log_scale = True

# Plot for Initialization with Zeros
axes[0].plot(sizes, results['list_zeros'], label='List Zeros', marker='o')
axes[0].plot(sizes, results['numpy_zeros'], label='NumPy Zeros', marker='o')
if log_scale:
    axes[0].set_xscale('log')
    axes[0].set_yscale('log')
axes[0].set_xlabel('Size')
axes[0].set_ylabel('Time (s)')
axes[0].set_title('Initialization with Zeros')
axes[0].legend()
axes[0].grid(True, which="both", ls="--")

# Plot for Addition
axes[1].plot(sizes, results['list_addition'], label='List Addition', marker='o')
axes[1].plot(sizes, results['numpy_addition'], label='NumPy Addition', marker='o')
if log_scale:
    axes[1].set_xscale('log')
    axes[1].set_yscale('log')
axes[1].set_xlabel('Size')
axes[1].set_ylabel('Time (s)')
axes[1].set_title('Addition')
axes[1].legend()
axes[1].grid(True, which="both", ls="--")

# Plot for Multiplication
axes[2].plot(sizes, results['list_multiplication'], label='List Multiplication', marker='o')
axes[2].plot(sizes, results['numpy_multiplication'], label='NumPy Multiplication', marker='o')
if log_scale:
    axes[2].set_xscale('log')
    axes[2].set_yscale('log')
axes[2].set_xlabel('Size')
axes[2].set_ylabel('Time (s)')
axes[2].set_title('Multiplication')
axes[2].legend()
axes[2].grid(True, which="both", ls="--")

# Plot for Power
axes[3].plot(sizes, results['list_power'], label='List Power', marker='o')
axes[3].plot(sizes, results['numpy_power'], label='NumPy Power', marker='o')
if log_scale:
    axes[3].set_xscale('log')
    axes[3].set_yscale('log')
axes[3].set_xlabel('Size')
axes[3].set_ylabel('Time (s)')
axes[3].set_title('Power')
axes[3].legend()
axes[3].grid(True, which="both", ls="--")

# Plot for Dot Product
axes[4].plot(sizes, results['list_dot_product'], label='List Dot Product', marker='o')
axes[4].plot(sizes, results['numpy_dot_product'], label='NumPy Dot Product', marker='o')
if log_scale:
    axes[4].set_xscale('log')
    axes[4].set_yscale('log')
axes[4].set_xlabel('Size')
axes[4].set_ylabel('Time (s)')
axes[4].set_title('Dot Product')
axes[4].legend()
axes[4].grid(True, which="both", ls="--")

# Plot for Sum
axes[5].plot(sizes, results['list_sum'], label='List Sum', marker='o')
axes[5].plot(sizes, results['numpy_sum'], label='NumPy Sum', marker='o')
if log_scale:
    axes[5].set_xscale('log')
    axes[5].set_yscale('log')
axes[5].set_xlabel('Size')
axes[5].set_ylabel('Time (s)')
axes[5].set_title('Sum')
axes[5].legend()
axes[5].grid(True, which="both", ls="--")

# Plot for Square Root
axes[6].plot(sizes, results['list_sqrt'], label='List Square Root', marker='o')
axes[6].plot(sizes, results['numpy_sqrt'], label='NumPy Square Root', marker='o')
if log_scale:
    axes[6].set_xscale('log')
    axes[6].set_yscale('log')
axes[6].set_xlabel('Size')
axes[6].set_ylabel('Time (s)')
axes[6].set_title('Square Root')
axes[6].legend()
axes[6].grid(True, which="both", ls="--")

# Plot for Mean
axes[7].plot(sizes, results['list_mean'], label='List Mean', marker='o')
axes[7].plot(sizes, results['numpy_mean'], label='NumPy Mean', marker='o')
if log_scale:
    axes[7].set_xscale('log')
    axes[7].set_yscale('log')
axes[7].set_xlabel('Size')
axes[7].set_ylabel('Time (s)')
axes[7].set_title('Mean')
axes[7].legend()
axes[7].grid(True, which="both", ls="--")

# Plot for Standard Deviation
axes[8].plot(sizes, results['list_std'], label='List Standard Deviation', marker='o')
axes[8].plot(sizes, results['numpy_std'], label='NumPy Standard Deviation', marker='o')
if log_scale:
    axes[8].set_xscale('log')
    axes[8].set_yscale('log')
axes[8].set_xlabel('Size')
axes[8].set_ylabel('Time (s)')
axes[8].set_title('Standard Deviation')
axes[8].legend()
axes[8].grid(True, which="both", ls="--")

# Save the plot to a file
fig.tight_layout()
fig_name = f'11_timeit/comparison_plots_with_logscales.png' if log_scale else f'11_timeit/comparison_plots_without_logscales.png'
fig.savefig(fig_name)
