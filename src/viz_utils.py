import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def set_plot_style():
    """Set the plotting style"""
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10
    sns.set_palette('husl')

def plot_state_accidents(df, output_path):
    """Plot top 10 states by number of accidents"""
    plt.figure(figsize=(14, 7))
    top_10_states = df.nlargest(10, 'Total_Accidents')
    
    sns.barplot(data=top_10_states, x='State/UT', y='Total_Accidents')
    plt.xticks(rotation=45, ha='right')
    plt.title('Top 10 States by Number of Road Accidents (2019)')
    plt.xlabel('State/UT')
    plt.ylabel('Number of Accidents')
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/state_accidents.png')
    plt.close()

def plot_regional_comparison(regional_stats, output_path):
    """Plot regional comparison of accidents, deaths, and injuries"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: Total numbers
    regional_stats[['Total_Accidents', 'Total_Deaths', 'Total_Injuries']].plot(kind='bar', ax=axes[0])
    axes[0].set_title('Regional Comparison: Absolute Numbers')
    axes[0].set_xlabel('Region')
    axes[0].tick_params(axis='x', rotation=45)
    
    # Plot 2: Rates
    regional_stats[['Fatality_Rate', 'Injury_Rate']].plot(kind='bar', ax=axes[1])
    axes[1].set_title('Regional Comparison: Rates')
    axes[1].set_xlabel('Region')
    axes[1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/regional_comparison.png')
    plt.close()

def plot_severity_metrics(severity_metrics, output_path):
    """Plot severity metrics for top states"""
    plt.figure(figsize=(12, 6))
    
    x = range(len(severity_metrics))
    width = 0.35
    
    plt.bar(x, severity_metrics['Fatality_Rate'], width, label='Fatality Rate')
    plt.bar([i + width for i in x], severity_metrics['Injury_Rate'], width, label='Injury Rate')
    
    plt.xlabel('State/UT')
    plt.ylabel('Rate (%)')
    plt.title('Fatality and Injury Rates by State')
    plt.xticks([i + width/2 for i in x], severity_metrics['State/UT'], rotation=45, ha='right')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/severity_metrics.png')
    plt.close()

def create_summary_statistics(df, national_avg, output_path):
    """Create and save summary statistics"""
    # Create a text file with summary statistics
    with open(f'{output_path}/summary_statistics.txt', 'w') as f:
        f.write("INDIAN ROAD ACCIDENTS ANALYSIS 2019\n")
        f.write("===================================\n\n")
        
        f.write("National Statistics:\n")
        f.write(f"Total Accidents: {df['Total_Accidents'].sum():,}\n")
        f.write(f"Total Deaths: {df['Total_Deaths'].sum():,}\n")
        f.write(f"Total Injuries: {df['Total_Injuries'].sum():,}\n\n")
        
        f.write("Average Statistics per State:\n")
        f.write(f"Average Accidents: {national_avg['avg_accidents']:,.2f}\n")
        f.write(f"Average Deaths: {national_avg['avg_deaths']:,.2f}\n")
        f.write(f"Average Injuries: {national_avg['avg_injuries']:,.2f}\n")
        f.write(f"Average Fatality Rate: {national_avg['avg_fatality_rate']:.2f}%\n")
        f.write(f"Average Injury Rate: {national_avg['avg_injury_rate']:.2f}%\n")

def plot_fatality_analysis(df, output_path):
    """Create visualizations for fatality analysis"""
    plt.figure(figsize=(15, 6))
    
    # Calculate fatality rate
    df_sorted = df.sort_values('Fatality_Rate', ascending=False)
    
    # Create scatter plot
    plt.scatter(df_sorted['Total_Accidents'], df_sorted['Total_Deaths'], 
               s=100, alpha=0.6, c=df_sorted['Fatality_Rate'], cmap='YlOrRd')
    
    # Add state labels
    for i, row in df_sorted.iterrows():
        plt.annotate(row['State/UT'], 
                    (row['Total_Accidents'], row['Total_Deaths']),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8)
    
    plt.colorbar(label='Fatality Rate (%)')
    plt.xlabel('Total Accidents')
    plt.ylabel('Total Deaths')
    plt.title('Relationship between Accidents and Fatalities by State')
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/fatality_analysis.png')
    plt.close()

def plot_injury_severity(df, output_path):
    """Create visualization for injury severity analysis"""
    plt.figure(figsize=(15, 6))
    
    # Calculate injury to accident ratio
    df['Injury_to_Accident_Ratio'] = (df['Total_Injuries'] / df['Total_Accidents']).round(2)
    df_sorted = df.sort_values('Injury_to_Accident_Ratio', ascending=False)
    
    # Create bar plot
    colors = plt.cm.RdYlBu(np.linspace(0, 1, len(df_sorted)))
    bars = plt.bar(range(len(df_sorted)), df_sorted['Injury_to_Accident_Ratio'],
                  color=colors)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom')
    
    plt.xticks(range(len(df_sorted)), df_sorted['State/UT'], rotation=45, ha='right')
    plt.xlabel('State/UT')
    plt.ylabel('Injuries per Accident')
    plt.title('Injury Severity by State (Injuries per Accident)')
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/injury_severity.png')
    plt.close()

def plot_comparative_metrics(df, output_path):
    """Create a comparative visualization of key metrics"""
    plt.figure(figsize=(15, 8))
    
    # Prepare data
    metrics = ['Total_Accidents', 'Total_Deaths', 'Total_Injuries']
    top_10_states = df.nlargest(10, 'Total_Accidents')
    
    # Set up the bar positions
    x = np.arange(len(top_10_states))
    width = 0.25
    
    # Create grouped bars
    plt.bar(x - width, top_10_states['Total_Accidents'], width, label='Accidents', color='skyblue')
    plt.bar(x, top_10_states['Total_Deaths'], width, label='Deaths', color='red')
    plt.bar(x + width, top_10_states['Total_Injuries'], width, label='Injuries', color='green')
    
    plt.xlabel('State/UT')
    plt.ylabel('Count')
    plt.title('Comparison of Accidents, Deaths, and Injuries (Top 10 States)')
    plt.xticks(x, top_10_states['State/UT'], rotation=45, ha='right')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/comparative_metrics.png')
    plt.close()
