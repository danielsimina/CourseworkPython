import math
import matplotlib.pyplot as plt
import numpy as np


def trig_calculator(angle_degrees):
    """Calculates sine, cosine, and tangent for a given angle in degrees."""
    # Convert degrees to radians (Python's math library expects radians)
    angle_radians = math.radians(angle_degrees)

    sin_val = math.sin(angle_radians)
    cos_val = math.cos(angle_radians)

    # Tangent is undefined at 90, 270, etc.
    tan_val = (
        math.tan(angle_radians)
        if abs(cos_val) > 1e-10
        else "Undefined (Asymptote)"
    )

    print(f"--- Trigonometric Values for {angle_degrees}° ---")
    print(f"Radians: {angle_radians:.4f} rad")
    print(f"sin({angle_degrees}°): {sin_val:.4f}")
    print(f"cos({angle_degrees}°): {cos_val:.4f}")
    print(f"tan({angle_degrees}°): {tan_val}\n")


def plot_trig_waves():
    """Plots Sine and Cosine waves over one full period (0 to 360 degrees)."""
    # Generate 1000 evenly spaced points from 0 to 2*pi radians
    x_rad = np.linspace(0, 2 * np.pi, 1000)
    x_deg = np.degrees(x_rad)

    y_sin = np.sin(x_rad)
    y_cos = np.cos(x_rad)

    # Setup plot
    plt.figure(figsize=(10, 5))
    plt.plot(x_deg, y_sin, label="y = sin(x)", color="blue", linewidth=2)
    plt.plot(
        x_deg, y_cos, label="y = cos(x)", color="orange", linestyle="--"
    )

    # Styling plot
    plt.title("Trigonometric Functions (Sine & Cosine)")
    plt.xlabel("Angle (Degrees)")
    plt.ylabel("Value")
    plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
    plt.axvline(0, color="black", linewidth=0.8, linestyle=":")
    plt.xticks([0, 90, 180, 270, 360])
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Display window
    plt.show()


if __name__ == "__main__":
    # 1. Run quick calculation examples
    trig_calculator(30)
    trig_calculator(45)
    trig_calculator(90)

    # 2. Render wave visualization plot
    plot_trig_waves()