# Indian Road Accidents Analysis (2019)

## Project Overview
This project analyzes road accident data across different states in India for the year 2019. It provides insights into accident patterns, fatality rates, and injury statistics to help understand road safety across different regions.

## Key Features
- State-wise accident analysis
- Regional pattern identification
- Fatality and injury rate analysis
- Comprehensive data visualizations
- Statistical insights

## Dataset
The dataset contains state-wise road accident statistics for India in 2019, including:
- Total number of accidents
- Number of fatalities
- Number of injuries
- State/UT wise distribution

## Key Insights
- Total accidents in India (2019): 443,907
- Total fatalities: 146,948
- National average fatality rate: 40.50%
- States with highest accidents:
  * Tamil Nadu: 63,685 accidents
  * Madhya Pradesh: 51,641 accidents
  * Kerala: 41,111 accidents
- Highest fatality rate: Uttarakhand (73.6%)
- Highest injury per accident: Sikkim (2.2 injuries/accident)

## Project Structure
PRODIGY_DS_05/
├── data/
│   └── india_accidents.csv
├── src/
│   ├── data_utils.py
│   ├── viz_utils.py
│   └── analyze_accidents.py
├── output/
│   ├── state_accidents.png
│   ├── fatality_analysis.png
│   ├── injury_severity.png
│   ├── comparative_metrics.png
│   └── summary_statistics.txt
├── requirements.txt
└── README.md

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PRODIGY_DS_05.git
   cd PRODIGY_DS_05
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main analysis script:
```bash
python src/analyze_accidents.py
```

This will:
1. Load and process the data
2. Generate visualizations in the `output` directory
3. Print key insights and statistics

## Visualizations
The project generates several visualizations:
1. **State Accidents**: Top 10 states by number of accidents
2. **Fatality Analysis**: Relationship between accidents and fatalities
3. **Injury Severity**: Analysis of injuries per accident across states
4. **Comparative Metrics**: Multi-metric comparison for top states

## Dependencies
- Python 3.12
- pandas
- numpy
- matplotlib
- seaborn

## Future Enhancements
- Machine learning predictive modeling
- Interactive dashboard development
- Multi-year trend analysis
- More granular geographical analysis

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Your Name]

## Acknowledgments
- Data source: Government of India, Ministry of Road Transport & Highways
- PRODIGY InfoTech for the project opportunity
