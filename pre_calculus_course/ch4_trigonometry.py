import math
import matplotlib.pyplot as plt
import numpy as np


def trig_calculator(angle_degrees):
    """Calculates sine, cosine, tangent, and cotangent for a given angle in degrees."""
    angle_radians = math.radians(angle_degrees)

    sin_val = math.sin(angle_radians)
    cos_val = math.cos(angle_radians)

    # Tangent is undefined where cos(x) = 0 (90°, 270°, etc.)
    tan_val = (
        f"{math.tan(angle_radians):.4f}"
        if abs(cos_val) > 1e-10
        else "Undefined (Asymptote)"
    )

    # Cotangent is undefined where sin(x) = 0 (0°, 180°, 360°, etc.)
    cot_val = (
        f"{1 / math.tan(angle_radians):.4f}"
        if abs(sin_val) > 1e-10
        else "Undefined (Asymptote)"
    )

    print(f"--- Trigonometric Values for {angle_degrees}° ---")
    print(f"Radians: {angle_radians:.4f} rad")
    print(f"sin({angle_degrees}°): {sin_val:.4f}")
    print(f"cos({angle_degrees}°): {cos_val:.4f}")
    print(f"tan({angle_degrees}°): {tan_val}")
    print(f"cot({angle_degrees}°): {cot_val}\n")


def plot_trig_waves():
    """Plots Sine, Cosine, Tangent, and Cotangent waves over 0 to 360 degrees."""
    x_rad = np.linspace(0, 2 * np.pi, 1000)
    x_deg = np.degrees(x_rad)

    y_sin = np.sin(x_rad)
    y_cos = np.cos(x_rad)

    # Mask undefined values to prevent vertical artifact connecting lines across asymptotes
    y_tan = np.tan(x_rad)
    y_tan[np.abs(y_tan) > 10] = np.nan  # Mask tangent asymptotes

    with np.errstate(divide="ignore", invalid="ignore"):
        y_cot = 1.0 / np.tan(x_rad)
    y_cot[np.abs(y_cot) > 10] = np.nan  # Mask cotangent asymptotes

    # Setup 1x2 subplot layout for visual clarity
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Plot 1: Sine & Cosine ---
    ax1.plot(x_deg, y_sin, label="y = sin(x)", color="blue", linewidth=2)
    ax1.plot(
        x_deg, y_cos, label="y = cos(x)", color="orange", linestyle="--"
    )
    ax1.set_title("Sine & Cosine")
    ax1.set_xlabel("Angle (Degrees)")
    ax1.set_ylabel("Value")
    ax1.set_xticks([0, 90, 180, 270, 360])
    ax1.axhline(0, color="black", linewidth=0.8, linestyle=":")
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # --- Plot 2: Tangent & Cotangent ---
    ax2.plot(x_deg, y_tan, label="y = tan(x)", color="green", linewidth=2)
    ax2.plot(
        x_deg, y_cot, label="y = cot(x)", color="purple", linestyle="--"
    )
    # Vertical asymptotes for Tan at 90° and 270°
    ax2.axvline(90, color="red", linestyle=":", alpha=0.7, label="Asymptotes")
    ax2.axvline(270, color="red", linestyle=":", alpha=0.7)

    ax2.set_title("Tangent & Cotangent")
    ax2.set_xlabel("Angle (Degrees)")
    ax2.set_ylabel("Value")
    ax2.set_ylim(-5, 5)  # Truncate vertical axis for clear view
    ax2.set_xticks([0, 90, 180, 270, 360])
    ax2.axhline(0, color="black", linewidth=0.8, linestyle=":")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 1. Run calculation tests
    trig_calculator(30)
    trig_calculator(45)
    trig_calculator(90)

    # 2. Render plots
    plot_trig_waves()