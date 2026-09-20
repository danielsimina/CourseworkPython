import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def sociological_imagination_demo():
    """Demonstrates C. Wright Mills' Sociological Imagination by framing

    personal troubles as broader public issues.
    """
    scenarios = [
        {
            "Issue": "Unemployment",
            "Personal Trouble": "An individual loses their job and struggles to pay rent.",
            "Public Issue": "A nationwide recession or industrial automation causes 10% unemployment.",
        },
        {
            "Issue": "Student Debt",
            "Personal Trouble": "A student owes $40,000 and feels overwhelmed by monthly payments.",
            "Public Issue": "Rising higher education costs and stagnant wage growth affect millions.",
        },
        {
            "Issue": "Health Care",
            "Personal Trouble": "A person cannot afford necessary prescription medication.",
            "Public Issue": "Systemic healthcare costs and insurance structure gaps impact public health.",
        },
    ]

    df_si = pd.DataFrame(scenarios)
    print("--- Chapter 1: The Sociological Imagination (C. Wright Mills) ---")
    for idx, row in df_si.iterrows():
        print(f"\n[Scenario {idx + 1}: {row['Issue']}]")
        print(f"  • Personal Trouble: {row['Personal Trouble']}")
        print(f"  • Public Issue:    {row['Public Issue']}")


def theoretical_perspectives_analysis():
    """Generates and visualizes comparative data for the 3 main sociological theories."""
    data = {
        "Theoretical Perspective": [
            "Functionalism",
            "Functionalism",
            "Conflict Theory",
            "Conflict Theory",
            "Symbolic Interactionism",
            "Symbolic Interactionism",
        ],
        "Level of Analysis": [
            "Macro-level",
            "Macro-level",
            "Macro-level",
            "Macro-level",
            "Micro-level",
            "Micro-level",
        ],
        "Focus Area": [
            "Social Stability & Order",
            "Institutional Functions",
            "Power & Inequality",
            "Resource Competition",
            "Shared Symbols & Meaning",
            "Day-to-day Interactions",
        ],
        "Explanatory Weight Score": [85, 80, 90, 88, 75, 82],
    }

    df_theory = pd.DataFrame(data)

    print("\n\n--- Three Major Sociological Perspectives ---")
    print(df_theory.to_string(index=False))

    # Plotting theoretical focus levels
    plt.figure(figsize=(10, 5))
    sns.barplot(
        data=df_theory,
        x="Theoretical Perspective",
        y="Explanatory Weight Score",
        hue="Level of Analysis",
        palette="Set1",
    )

    plt.title(
        "Sociological Analysis: Core Theoretical Perspectives (Chapter 1)",
        fontsize=14,
        pad=15,
    )
    plt.xlabel("Sociological Theory", fontsize=12)
    plt.ylabel("Conceptual Emphasis Score (0-100)", fontsize=12)
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend(title="Analysis Scale", loc="upper right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sociological_imagination_demo()
    theoretical_perspectives_analysis()