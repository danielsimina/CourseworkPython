import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def create_socialization_data():
    """Generates synthetic survey data representing the influence of socialization agents

    on scale of 1-10 across different life stages.
    """
    data = {
        "Life Stage": [
            "Childhood",
            "Childhood",
            "Childhood",
            "Childhood",
            "Adolescence",
            "Adolescence",
            "Adolescence",
            "Adolescence",
            "Adulthood",
            "Adulthood",
            "Adulthood",
            "Adulthood",
        ],
        "Agent": [
            "Family",
            "Peers",
            "School",
            "Mass Media",
            "Family",
            "Peers",
            "School",
            "Mass Media",
            "Family",
            "Peers",
            "School",
            "Mass Media",
        ],
        # Influence Score on a scale of 1 to 10
        "Influence Score": [9.2, 3.1, 5.5, 4.0, 5.8, 9.1, 7.0, 8.2, 6.0, 7.5, 4.2, 8.8],
    }
    return pd.DataFrame(data)


def analyze_agents(df):
    """Calculates summary stats for agents of socialization."""
    print("--- Chapter 4: Agents of Socialization Analysis ---")
    print(df.to_string(index=False))

    # Identify dominant agent per life stage
    dominant = df.loc[df.groupby("Life Stage")["Influence Score"].idxmax()]
    print("\n--- Primary Agent of Influence by Life Stage ---")
    for _, row in dominant.iterrows():
        print(
            f"Stage: {row['Life Stage']:<12} | Top Agent: {row['Agent']:<10} | Score: {row['Influence Score']}/10"
        )


def plot_socialization_trends(df):
    """Generates a grouped bar chart visualizing the influence shift."""
    plt.figure(figsize=(10, 6))

    # Create Seaborn grouped barplot
    ax = sns.barplot(
        data=df,
        x="Life Stage",
        y="Influence Score",
        hue="Agent",
        palette="Blues_d",
    )

    # Styling plot
    plt.title(
        "Sociological Analysis: Shift in Agents of Socialization Over Time",
        fontsize=14,
        pad=15,
    )
    plt.xlabel("Developmental Life Stage", fontsize=12)
    plt.ylabel("Influence Index (1 - 10)", fontsize=12)
    plt.ylim(0, 10)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Annotate specific sociological shift (Primary to Secondary Socialization)
    plt.annotate(
        "Primary Socialization\n(Family Dominance)",
        xy=(0, 9.2),
        xytext=(-0.35, 7.5),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=6),
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3),
    )

    plt.annotate(
        "Peer & Media Shift\n(Secondary Agents)",
        xy=(1, 9.1),
        xytext=(0.65, 5.5),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=6),
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3),
    )

    plt.legend(title="Agent of Socialization", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Ensure required packages are installed
    try:
        df_social = create_socialization_data()
        analyze_agents(df_social)
        plot_socialization_trends(df_social)
    except ModuleNotFoundError as e:
        print(f"Missing dependency: {e}. Please run 'pip install pandas matplotlib seaborn'")