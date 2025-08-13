# Optimizing Email Campaign Click-Through Rates via A/B Testing of Subject Line Personalization

## Overview

This project analyzes the results of an A/B test conducted to determine the optimal level of personalization in email subject lines to maximize click-through rates (CTR).  The analysis leverages A/B testing data to identify which subject line variations (ranging from no personalization to highly personalized) performed best and to provide actionable insights for future email marketing campaigns.  The analysis includes statistical comparisons to ensure the observed differences are significant.

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* Seaborn
* SciPy (for statistical analysis)


## How to Run

1. **Install Dependencies:**  Ensure you have Python 3 installed. Then, install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Analysis:** Execute the main script:

   ```bash
   python main.py
   ```

## Example Output

The script will print a summary of the A/B test results to the console, including key statistics such as click-through rates for each variation, statistical significance testing results (p-values), and a recommendation for the optimal level of personalization.  Additionally, the script will generate the following plot files in the same directory:

* **ctr_comparison.png:** A bar chart comparing the click-through rates of different subject line personalization levels.
* **statistical_significance.png:**  A visualization of the statistical significance test results.


The specific content of the console output and plots will depend on the data provided.  Refer to the analysis section within the `main.py` script for detailed explanations of the results.