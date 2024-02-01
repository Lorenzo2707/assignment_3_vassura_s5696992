
# Data Analysis and Plotting Script

This script is designed for analyzing data from CSV files, focusing on statistical analysis and visualization. It filters, cleans, and processes specified data columns, performs statistical tests, and plots the results for easy interpretation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- pandas
- matplotlib
- scipy

You can install the necessary libraries using pip:

```
pip install pandas matplotlib scipy
```

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Ensure Python and pip are installed on your system.
2. Install the required Python libraries:
    ```
    pip install pandas matplotlib scipy
    ```
3. Clone or download this script to your local machine.


## Usage

Here is how to run the script and an example of commands you might use:

```
python assignment_3_vassura_s5696992.py --csv_file_path <path_to_csv> --cleaned_file_path <path_to_cleaned_csv> --columns <column_names> --significance_level <level>
```

Replace `<path_to_csv>`, `<path_to_cleaned_csv>`, `<column_names>`, and `<level>` with your actual file paths, column names to include in the analysis, and the significance level for the statistical test, respectively.

Columns selection:
   **Col1:** sample_id
   **Col2:** treatments
   **Col3-38:** variables

## Authors

**Lorenzo Vassura** - *Initial work* - [YourGitHub](https://github.com/Lorenzo2707/assignment_3_vassura_s5696992)
