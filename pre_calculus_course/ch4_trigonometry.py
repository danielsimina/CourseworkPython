import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def verify_fundamental_trig_values():
    """Evaluates trigonometric functions across standard unit circle angles:

    Calculates sin(x), cos(x), and tan(x) for common angles in standard position.
    """
    angles_deg = [0, 30, 45, 60, 90, 120, 135, 150, 180]
    angles_rad = np.radians(angles_deg)

    results = []
    for deg, rad in zip(angles_deg, angles_rad):
        sin_val = np.sin(rad)
        cos_val = np.cos(rad)

        # Quotient calculation (handling undefined tan at 90 deg)
        tan_calc = (
            sin_val / cos_val if not np.isclose(cos_val, 0) else np.nan
        )

        results.append(
            {
                "Angle (Deg)": deg,
                "Angle (Rad)": round(rad, 4),
                "sin(x)": round(sin_val, 4),
                "cos(x)": round(cos_val, 4),
                "tan(x)": (
                    round(tan_calc, 4) if not np.isnan(tan_calc) else "Undefined"
                ),
            }
        )

    df_trig = pd.DataFrame(results)
    print("--- Chapter 4: Trigonometric Functions - Unit Circle Values ---")
    print(df_trig.to_string(index=False))


def plot_trig_waves():
    """Plots standard sine and cosine waves across [0, 2pi] with pi-formatted ticks."""
    x = np.linspace(0, 2 * np.pi, 500)
    sin_wave = np.sin(x)
    cos_wave = np.cos(x)

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        x, sin_wave, label=r"\(y = \sin(x)\)", color="#1f77b4", linewidth=2.5
    )
    ax.plot(
        x,
        cos_wave,
        label=r"\(y = \cos(x)\)",
        color="#e74c3c",
        linestyle="--",
        linewidth=2.5,
    )

    ax.set_title(
        "Trigonometric Functions: Sine and Cosine Waves (Chapter 4)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Angle x (Radians)", fontsize=11)
    ax.set_ylabel("Amplitude / Value", fontsize=11)

    ax.set_xticks(
        [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        labels=["0", r"\(\frac{\pi}{2}\)", r"\(\pi\)", r"\(\frac{3\pi}{2}\)", r"\(2\pi\)"],
    )

    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper right", fontsize=11)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    verify_fundamental_trig_values()
    plot_trig_waves()