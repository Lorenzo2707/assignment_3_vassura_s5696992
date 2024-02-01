import argparse  # Import argparse for command-line argument parsing
import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import scipy.stats as stats  # Import scipy.stats for statistical analysis


# Define a function to process the CSV data and generate a plot
def process_and_plot_data(csv_file_path, cleaned_file_path, columns, significance_level):
    # Load the specified columns from the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path, usecols=columns)

    # Filter out rows where the first column starts with 'blank' and drop rows with any NaN values
    df = df[~df.iloc[:, 0].astype(str).str.startswith('blank')]
    df.dropna(how='any', inplace=True)

    # Define the order of treatments for plotting
    treatment_order = ['C', 'H', 'HC', 'HT', 'HC-H', 'HT-H', 'HT-HC', 'HT-HC-H']
    # Filter the DataFrame to include only specified treatments and sort them
    actual_treatments = sorted(set(df.iloc[:, 1]) & set(treatment_order), key=treatment_order.index)

    # Apply coloring and other aesthetic settings to the plot
    pastel_colors = ['#FFB6C1', '#FFD700', '#FFA07A', '#FF69B4', '#98FB98', '#DDA0DD', '#87CEEB', '#20B2AA']

    # Further processing to prepare the data for plotting
    filtered_df = df[df.iloc[:, 1].isin(actual_treatments)].copy()
    filtered_df.iloc[:, 1] = pd.Categorical(filtered_df.iloc[:, 1], categories=actual_treatments, ordered=True)

    # Group the data by treatment and prepare it for plotting
    grouped_data_ordered = filtered_df.groupby(filtered_df.columns[1], observed=True)
    data_to_plot_ordered = [group.iloc[:, -1].values for _, group in grouped_data_ordered]

    # Generate the box plot with customized aesthetics
    plt.figure(figsize=(12, 6))
    box = plt.boxplot(data_to_plot_ordered, patch_artist=True)
    for patch, color in zip(box['boxes'], pastel_colors):
        patch.set_facecolor(color)
    for element in ['whiskers', 'caps', 'medians']:
        plt.setp(box[element], color='black', linewidth=1.5)

    # Set plot labels and title
    plt.xticks(ticks=range(1, len(actual_treatments) + 1), labels=actual_treatments)
    plt.title("Effects of Treatments on Specified Measurement")
    plt.xlabel("Treatments")
    plt.ylabel("Specified Measurement")

    # Perform ANOVA to test for significant differences between groups
    f_statistic, p_value = stats.f_oneway(*data_to_plot_ordered)
    print(f"ANOVA F-statistic: {f_statistic:.4f}")
    print(f"P-value: {p_value:.4f}")
    if p_value < significance_level:
        print("There are significant differences between at least some of the treatment groups.")
    else:
        print("There are no significant differences between the treatment groups.")

    # Save the cleaned and processed data to a new file
    df.to_csv(cleaned_file_path, sep='\t', index=False, header=True)

    # Display the plot
    plt.show()


if __name__ == "__main__":
    # Parse command-line arguments for input and output file paths, columns, and significance level
    parser = argparse.ArgumentParser(description="Process and plot data from a CSV file.")
    parser.add_argument("csv_file_path", type=str, help="Path to the input CSV file.")
    parser.add_argument("cleaned_file_path", type=str, help="Path to output the cleaned data TSV file.")
    parser.add_argument("--columns", nargs='+', type=int, default=[0, 1, 34],
                        help="Columns to use from the input file.")
    parser.add_argument("--significance_level", type=float, default=0.05, help="Significance level for ANOVA test.")

    args = parser.parse_args()
    # Call the function with arguments from the command line
    process_and_plot_data(args.csv_file_path, args.cleaned_file_path, args.columns, args.significance_level)
