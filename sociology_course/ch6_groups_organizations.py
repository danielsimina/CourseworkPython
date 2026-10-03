import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def social_groups_analysis():
    """Models Primary vs. Secondary Groups and In-Group vs. Out-Group dynamics."""
    groups_data = [
        {
            "Group Name": "Immediate Family / Close Friends",
            "Group Type": "Primary Group",
            "Relationship Style": "Personal, Long-term, Intimate",
            "Group Cohesion (1-100)": 95,
            "Size Category": "Small (2-6 members)",
        },
        {
            "Group Name": "College Seminar Class",
            "Group Type": "Secondary Group",
            "Relationship Style": "Impersonal, Task-oriented, Temporary",
            "Group Cohesion (1-100)": 60,
            "Size Category": "Medium (15-30 members)",
        },
        {
            "Group Name": "Corporate Department",
            "Group Type": "Secondary Group",
            "Relationship Style": "Goal-driven, Formal roles",
            "Group Cohesion (1-100)": 50,
            "Size Category": "Large (50+ members)",
        },
    ]

    df_groups = pd.DataFrame(groups_data)
    print("--- Chapter 6: Primary vs. Secondary Groups Analysis ---")
    print(df_groups.to_string(index=False))


def bureaucracy_efficiency_model():
    """Models Max Weber's Ideal Bureaucracy characteristics and potential dysfunctions

    (e.g., Bureaucratic Red Tape / Goal Displacement).
    """
    bureaucracy_traits = {
        "Bureaucratic Characteristic": [
            "Division of Labor",
            "Hierarchy of Authority",
            "Explicit Rules & Regulations",
            "Impersonality",
            "Qualification-Based Employment",
        ],
        "Primary Sociological Benefit": [
            "High specialization and task efficiency",
            "Clear chain of command and accountability",
            "Consistency and predictability in operations",
            "Equal treatment; reduction of personal bias",
            "Merit-based hiring and promotion",
        ],
        "Potential Dysfunction (Red Tape)": [
            "Alienation and repetitive work burnout",
            "Communication bottlenecks across levels",
            "Goal displacement (rules replace goals)",
            "Lack of empathy / rigid response to special cases",
            "Peter Principle (promoted to level of incompetence)",
        ],
        "Efficiency Rating (0-100)": [88, 75, 70, 65, 82],
    }

    df_bureaucracy = pd.DataFrame(bureaucracy_traits)
    print("\n\n--- Max Weber's Characteristics of Bureaucracies ---")
    print(df_bureaucracy.to_string(index=False))
    return df_bureaucracy


def plot_group_size_and_conformity():
    """Visualizes how group size impacts social interaction dyads/triads,

    group cohesion, and risk of conformity / Groupthink.
    """
    # Group dynamics dataset: Group size vs. Conformity Risk & Individual Accountability
    dynamics_data = {
        "Group Size (Members)": [2, 3, 5, 8, 12, 20, 35],
        "Conformity Pressure Index (0-100)": [15, 30, 65, 80, 88, 92, 95],
        "Individual Responsibility Perception (%)": [100, 85, 60, 40, 25, 15, 8],
    }

    df_dynamics = pd.DataFrame(dynamics_data)

    sns.set_theme(style="whitegrid")
    fig, ax1 = plt.subplots(figsize=(9, 5))

    # Plot Conformity Pressure (Line 1)
    color1 = "#c0392b"
    ax1.set_xlabel("Group Size (Number of Members)", fontsize=11)
    ax1.set_ylabel(
        "Conformity Pressure Index (0-100)", color=color1, fontsize=11
    )
    line1 = ax1.plot(
        df_dynamics["Group Size (Members)"],
        df_dynamics["Conformity Pressure Index (0-100)"],
        color=color1,
        marker="o",
        linewidth=2.5,
        label="Conformity Pressure / Groupthink Risk",
    )
    ax1.tick_params(axis="y", labelcolor=color1)
    ax1.set_ylim(0, 105)

    # Secondary Axis for Individual Responsibility Perception (Social Loafing effect)
    ax2 = ax1.twinx()
    color2 = "#2980b9"
    ax2.set_ylabel(
        "Perceived Individual Responsibility (%)", color=color2, fontsize=11
    )
    line2 = ax2.plot(
        df_dynamics["Group Size (Members)"],
        df_dynamics["Individual Responsibility Perception (%)"],
        color=color2,
        marker="s",
        linestyle="--",
        linewidth=2.5,
        label="Perceived Individual Accountability",
    )
    ax2.tick_params(axis="y", labelcolor=color2)
    ax2.set_ylim(0, 105)

    # Title and Annotations
    plt.title(
        "Sociological Analysis: Group Dynamics, Conformity, and Group Size (Ch. 6)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )

    # Annotate Dyad/Triad boundary
    ax1.annotate(
        "Dyads (2) & Triads (3)\nHigh intimacy & individual accountability",
        xy=(2, 15),
        xytext=(4, 10),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=5),
        fontsize=9,
        bbox=dict(
            boxstyle="round,pad=0.3", fc="#e8f8f5", ec="#1abc9c", alpha=0.9
        ),
    )

    # Annotate Asch Conformity threshold
    ax1.annotate(
        "Asch Effect Threshold\nConformity peaks around 4-5 members",
        xy=(5, 65),
        xytext=(8, 45),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=5),
        fontsize=9,
        bbox=dict(
            boxstyle="round,pad=0.3", fc="#fef9e7", ec="#f1c40f", alpha=0.9
        ),
    )

    # Merge legends from both axes
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="center right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    social_groups_analysis()
    bureaucracy_efficiency_model()
    plot_group_size_and_conformity()