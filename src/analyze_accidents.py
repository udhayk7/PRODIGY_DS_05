import sys
sys.path.append('.')

import pandas as pd
import matplotlib.pyplot as plt
from src.data_utils import (
    load_and_clean_data,
    analyze_state_statistics,
    analyze_regional_patterns,
    analyze_severity_metrics
)
from src.viz_utils import (
    set_plot_style,
    plot_state_accidents,
    plot_regional_comparison,
    plot_severity_metrics,
    create_summary_statistics,
    plot_fatality_analysis,
    plot_injury_severity,
    plot_comparative_metrics
)

def main():
    print("Loading and cleaning data...")
    df = load_and_clean_data('data/india_accidents.csv')
    
    print("Analyzing state statistics...")
    stats, national_avg = analyze_state_statistics(df)
    
    print("Analyzing regional patterns...")
    regional_stats = analyze_regional_patterns(df)
    
    print("Analyzing severity metrics...")
    severity_metrics = analyze_severity_metrics(df)
    
    print("Creating visualizations...")
    set_plot_style()
    
    # Create visualizations
    plot_state_accidents(df, 'output')
    plot_regional_comparison(regional_stats, 'output')
    plot_severity_metrics(severity_metrics, 'output')
    create_summary_statistics(df, national_avg, 'output')
    
    # Additional visualizations
    plot_fatality_analysis(df, 'output')
    plot_injury_severity(df, 'output')
    plot_comparative_metrics(df, 'output')
    
    print("\nAnalysis complete! Check the 'output' directory for results.")
    print("\nKey findings:")
    print(f"- Total accidents in India (2019): {df['Total_Accidents'].sum():,}")
    print(f"- Total fatalities: {df['Total_Deaths'].sum():,}")
    print(f"- Total injuries: {df['Total_Injuries'].sum():,}")
    print(f"- National average fatality rate: {national_avg['avg_fatality_rate']:.2f}%")
    print(f"- States with highest number of accidents:")
    for _, row in stats.head(3).iterrows():
        print(f"  * {row['State/UT']}: {row['Total_Accidents']:,} accidents")
    
    # Additional insights
    print("\nAdditional insights:")
    highest_fatality = df.loc[df['Fatality_Rate'].idxmax()]
    highest_injury = df.loc[(df['Total_Injuries']/df['Total_Accidents']).idxmax()]
    print(f"- Highest fatality rate: {highest_fatality['State/UT']} ({highest_fatality['Fatality_Rate']:.1f}%)")
    print(f"- Highest injury per accident: {highest_injury['State/UT']} ({(highest_injury['Total_Injuries']/highest_injury['Total_Accidents']):.1f} injuries/accident)")

if __name__ == "__main__":
    main()
