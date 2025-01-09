# Happiness Report Data Analysis

This repository contains an analysis of the World Happiness Report 2017 using Python. The project explores factors that contribute to global happiness and employs data science techniques such as exploratory data analysis (EDA), summary statistics, and visualization.

## Project Structure

- `happiness_2017.py`: Python script for data loading, processing, and analysis.
- `happiness_2017.csv`: Dataset from the World Happiness Report 2017.
- `2.2. Case Study 1: The Happiness Report.pdf`: Documentation detailing the case study and data analysis process.

## Dataset Description

The dataset (`happiness_2017.csv`) contains the following columns:

1. **Country**: Name of the country.
2. **Region**: Geographical region.
3. **Happiness Rank**: Rank of the country by happiness score.
4. **Happiness Score**: Average happiness score.
5. **GDP per Capita**: Economic performance.
6. **Healthy Life Expectancy**: Life expectancy adjusted for health.
7. **Social Support**: Availability of support during crises.
8. **Freedom**: Perceived freedom in life choices.
9. **Generosity**: Charitable behavior.
10. **Perceptions of Corruption**: Trust in government and business sectors.

## Objectives

1. Investigate the key factors influencing happiness.
2. Examine correlations between happiness and economic, social, and health indicators.
3. Identify patterns and anomalies in global happiness distribution.

## Requirements

- Python 3.8+
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/happiness-analysis.git
   cd happiness-analysis
   ```

2. Run the analysis script:

   ```bash
   python happiness_2017.py
   ```

3. Output includes:
   - Descriptive statistics.
   - Visualizations of happiness distributions and contributing factors.
   - Insights from correlation analysis.

## Key Findings

- Countries with higher GDP per capita and healthy life expectancy tend to score higher on happiness.
- Social support and perceived freedom also show significant positive correlations with happiness.
- Generosity and perceptions of corruption exhibit more nuanced relationships.

## Future Work

- Expand analysis to include other years of the World Happiness Report.
- Develop predictive models for happiness scores based on contributing factors.
- Create an interactive dashboard for visualizing data.

## References

- [World Happiness Report 2018](http://worldhappiness.report/ed/2018/)
- "How to Think Like a Data Scientist" - Case Study Documentation

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Contributions, suggestions, and feedback are welcome! Feel free to submit issues or pull requests.
