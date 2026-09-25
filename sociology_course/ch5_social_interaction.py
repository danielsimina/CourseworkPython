import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def status_and_roles_demo():
    """Demonstrates key status and role concepts:

    Ascribed vs. Achieved Status, Role Set, Role Strain, and Role Conflict.
    """
    statuses_data = [
        {
            "Status": "College Student",
            "Status Type": "Achieved",
            "Role Set Expectations": "Attend lectures, study for exams, submit assignments on time.",
            "Role Challenge": "Role Strain: Balancing multiple exams occurring on the same day.",
        },
        {
            "Status": "Employee / Worker",
            "Status Type": "Achieved",
            "Role Set Expectations": "Clock in on time, complete workplace tasks, follow company policy.",
            "Role Challenge": "Role Conflict: Work shift conflicts with attending a mandatory class.",
        },
        {
            "Status": "Family Member (Son/Daughter)",
            "Status Type": "Ascribed",
            "Role Set Expectations": "Support family members, participate in household duties.",
            "Role Challenge": "Role Strain: Fulfilling family expectations while maintaining academic goals.",
        },
    ]

    df_status = pd.DataFrame(statuses_data)
    print(
        "--- Chapter 5: Social Interaction in Everyday Life - Statuses & Roles ---"
    )
    for idx, row in df_status.iterrows():
        print(f"\n[Status {idx + 1}: {row['Status']} ({row['Status Type']})]")
        print(f"  • Role Set:   {row['Role Set Expectations']}")
        print(f"  • Challenge:  {row['Role Challenge']}")


def dramaturgical_analysis_demo():
    """Demonstrates Erving Goffman's Dramaturgical Analysis:

    Front Stage vs. Back Stage impression management behaviors.
    """
    dramaturgy_data = {
        "Social Context": [
            "Job Interview",
            "Customer Service",
            "Classroom Presentation",
            "Private Residence / Home",
        ],
        "Impression Management Stage": [
            "Front Stage",
            "Front Stage",
            "Front Stage",
            "Back Stage",
        ],
        "Observed Behavior / Script": [
            "Formal tone, professional attire, polished communication",
            "Polite demeanor, suppressed personal frustration, active listening",
            "Structured delivery, clear articulation, maintaining eye contact",
            "Casual relaxed posture, unfiltered expression, emotional decompression",
        ],
    }

    df_dramaturgy = pd.DataFrame(dramaturgy_data)
    print("\n\n--- Erving Goffman: Dramaturgical Analysis ---")
    print(df_dramaturgy.to_string(index=False))


def plot_social_interaction_types():
    """Visualizes the frequency and impact of core social interaction types

    (Exchange, Cooperation, Competition, Conflict) using Seaborn and Matplotlib.
    """
    # Synthetic data modeling interaction dimensions
    interaction_data = {
        "Interaction Type": [
            "Cooperation",
            "Exchange",
            "Competition",
            "Conflict",
            "Cooperation",
            "Exchange",
            "Competition",
            "Conflict",
        ],
        "Social Goal": [
            "Shared Group Goal",
            "Reciprocal Benefit",
            "Individual Achievement",
            "Resource Dominance",
            "Shared Group Goal",
            "Reciprocal Benefit",
            "Individual Achievement",
            "Resource Dominance",
        ],
        "Social Cohesion Index (0-100)": [90, 80, 50, 15, 85, 75, 55, 20],
        "Prevalence Frequency (%)": [35, 30, 20, 15, 38, 28, 22, 12],
    }

    df_interaction = pd.DataFrame(interaction_data)

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5))

    # Seaborn bar plot comparing Interaction Types and Social Cohesion
    sns.barplot(
        data=df_interaction,
        x="Interaction Type",
        y="Social Cohesion Index (0-100)",
        hue="Social Goal",
        palette="Blues_d",
        ax=ax,
        errorbar=None,
    )

    # Formatting and Styling
    ax.set_title(
        "Social Interaction in Everyday Life: Types & Cohesion Impact (Chapter 5)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Type of Social Interaction", fontsize=11)
    ax.set_ylabel("Average Social Cohesion Index (0-100)", fontsize=11)
    ax.set_ylim(0, 100)

    # Move legend to top right outside plot area
    ax.legend(
        title="Underlying Social Goal",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    status_and_roles_demo()
    dramaturgical_analysis_demo()
    plot_social_interaction_types()