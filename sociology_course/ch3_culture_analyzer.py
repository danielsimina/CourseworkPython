import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def create_cultural_text_data():
    """Generates sample corpus data representing cultural texts and value expressions."""
    data = {
        "Culture/Society": [
            "Individualist Culture",
            "Individualist Culture",
            "Individualist Culture",
            "Collectivist Culture",
            "Collectivist Culture",
            "Collectivist Culture",
        ],
        "Value Focus": [
            "Autonomy & Self-Reliance",
            "Personal Achievement",
            "Rights & Freedom",
            "Harmony & Duty",
            "Group Cohesion",
            "Family & Respect",
        ],
        "Frequency Score": [88, 92, 85, 95, 90, 94],
        "Category": [
            "Non-Material Values",
            "Non-Material Values",
            "Non-Material Values",
            "Non-Material Values",
            "Non-Material Values",
            "Non-Material Values",
        ],
    }
    return pd.DataFrame(data)


def analyze_culture_values(df):
    """Calculates core metric summaries across cultural types."""
    print("--- Chapter 3: Culture - Value Focus Analysis ---")
    print(df.to_string(index=False))

    avg_scores = df.groupby("Culture/Society")["Frequency Score"].mean()
    print("\n--- Average Focus Score by Cultural Orientation ---")
    for culture, score in avg_scores.items():
        print(f"Culture Type: {culture:<22} | Mean Focus Index: {score:.1f}")


def plot_cultural_comparison(df):
    """Plots comparative breakdown of cultural value emphasis."""
    plt.figure(figsize=(10, 5))
    sns.barplot(
        data=df,
        x="Value Focus",
        y="Frequency Score",
        hue="Culture/Society",
        palette="Set2",
    )

    plt.title(
        "Sociological Analysis: Non-Material Cultural Values Emphasis",
        fontsize=14,
        pad=15,
    )
    plt.xlabel("Core Cultural Value / Norm", fontsize=12)
    plt.ylabel("Cultural Emphasis Score (0-100)", fontsize=12)
    plt.xticks(rotation=15)
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend(title="Cultural Model", loc="upper right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df_culture = create_cultural_text_data()
    analyze_culture_values(df_culture)
    plot_cultural_comparison(df_culture)