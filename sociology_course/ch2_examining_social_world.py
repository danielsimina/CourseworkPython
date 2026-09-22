import matplotlib.pyplot as plt
import pandas as pd


def research_methods_demo():
    """Demonstrates sociological research steps by mapping hypotheses,

    independent variables (IV), dependent variables (DV), and research methods.
    """
    study_data = [
        {
            "Study Title": "Social Media & Isolation",
            "Research Method": "Survey",
            "Independent Variable (IV)": "Daily Screen Time (Hours)",
            "Dependent Variable (DV)": "Reported Loneliness Index (1-10)",
            "Sample Size (N)": 1200,
        },
        {
            "Study Title": "Income & Education Attainment",
            "Research Method": "Secondary Data Analysis",
            "Independent Variable (IV)": "Years of Higher Education",
            "Dependent Variable (DV)": "Annual Household Income ($k)",
            "Sample Size (N)": 5000,
        },
        {
            "Study Title": "Workplace Gender Bias",
            "Research Method": "Field Experiment",
            "Independent Variable (IV)": "Resume Applicant Name/Gender",
            "Dependent Variable (DV)": "Interview Callback Rate (%)",
            "Sample Size (N)": 800,
        },
    ]

    df_research = pd.DataFrame(study_data)
    print("--- Chapter 2: Examining Our Social World - Research Design ---")
    print(df_research.to_string(index=False))


def plot_correlation_vs_causation():
    """Generates a scatter plot using pure Matplotlib to visualize how sociologists

    analyze relationships between Independent (X) and Dependent (Y) variables.
    """
    # Synthetic sociological data: Education level vs. Median Annual Salary ($k)
    education_years = [12, 13, 14, 16, 16, 18, 18, 20, 21]
    annual_income = [35, 38, 42, 58, 62, 75, 80, 92, 105]

    fig, ax = plt.subplots(figsize=(9, 5))

    # Plot data points (Scatter Plot)
    ax.scatter(
        education_years,
        annual_income,
        color="#2b5c8f",
        s=70,
        edgecolor="black",
        zorder=3,
        label="Observed Sample Data",
    )

    # Plot a simple linear trendline
    ax.plot(
        [12, 21],
        [35, 105],
        color="#e74c3c",
        linestyle="--",
        linewidth=2,
        label="Positive Correlation Trend",
    )

    # Title and Labels
    ax.set_title(
        "Sociological Research: Evaluating Variable Relationships (Ch. 2)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Independent Variable (X): Years of Education", fontsize=11)
    ax.set_ylabel("Dependent Variable (Y): Income ($1,000s)", fontsize=11)

    # Axis Limits and Grid
    ax.set_xlim(11, 22)
    ax.set_ylim(20, 115)
    ax.grid(True, linestyle="--", alpha=0.5, zorder=0)

    # Annotate key research distinction
    ax.annotate(
        "Correlation ≠ Causation\n(Watch for Spurious Variables!)",
        xy=(16, 60),
        xytext=(12.5, 90),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=5),
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", fc="#fff2cc", ec="#d6b656", alpha=0.9),
    )

    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    research_methods_demo()
    plot_correlation_vs_causation()