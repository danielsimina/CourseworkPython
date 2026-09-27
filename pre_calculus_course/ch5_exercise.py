import matplotlib.pyplot as plt
import numpy as np

# Define the function y = 3*sin(2x + 2pi)
def f(x):
    return 3 * np.sin(2 * x + 2 * np.pi)

# Generate x-values covering 3 full periods (from -2pi to pi)
x = np.linspace(-2 * np.pi, np.pi, 1000)
y = f(x)

# Create the figure plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r'\(y = 3\sin(2x + 2\pi)\)', color='blue', linewidth=2)

# Add reference axis lines at x=0 and y=0
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# Set labels and title
plt.title(r'Graph of \(y = 3\sin(2x + 2\pi)\)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Format x-axis ticks in steps of pi/2
tick_positions = np.arange(-2 * np.pi, np.pi + np.pi / 2, np.pi / 2)
tick_labels = [
    r'\(-2\pi\)',
    r'\(-\frac{3\pi}{2}\)',
    r'\(-\pi\)',
    r'\(-\frac{\pi}{2}\)',
    r'$0$',
    r'\(\frac{\pi}{2}\)',
    r'\(\pi\)',
]

plt.xticks(tick_positions, tick_labels, fontsize=11)
plt.ylim(-4, 4)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()