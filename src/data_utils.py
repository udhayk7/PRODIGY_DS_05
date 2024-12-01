import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    """Load and clean the Indian road accidents dataset"""
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Calculate additional metrics
    df['Fatality_Rate'] = (df['Total_Deaths'] / df['Total_Accidents'] * 100).round(2)
    df['Injury_Rate'] = (df['Total_Injuries'] / df['Total_Accidents'] * 100).round(2)
    
    return df

def analyze_state_statistics(df):
    """Analyze state-wise accident statistics"""
    # Sort states by total accidents
    stats = df.sort_values('Total_Accidents', ascending=False)
    
    # Calculate national averages
    national_avg = {
        'avg_accidents': df['Total_Accidents'].mean(),
        'avg_deaths': df['Total_Deaths'].mean(),
        'avg_injuries': df['Total_Injuries'].mean(),
        'avg_fatality_rate': df['Fatality_Rate'].mean(),
        'avg_injury_rate': df['Injury_Rate'].mean()
    }
    
    return stats, national_avg

def analyze_regional_patterns(df):
    """Analyze regional patterns in accident data"""
    # Define regions
    north = ['Delhi', 'Haryana', 'Punjab', 'Himachal Pradesh', 'Jammu & Kashmir', 'Uttarakhand']
    south = ['Tamil Nadu', 'Karnataka', 'Kerala', 'Andhra Pradesh', 'Telangana']
    east = ['West Bengal', 'Bihar', 'Odisha', 'Jharkhand']
    west = ['Maharashtra', 'Gujarat', 'Goa', 'Rajasthan']
    central = ['Madhya Pradesh', 'Chhattisgarh', 'Uttar Pradesh']
    northeast = ['Assam', 'Tripura', 'Manipur', 'Meghalaya', 'Nagaland', 'Arunachal Pradesh', 'Mizoram', 'Sikkim']
    
    # Create region mapping
    region_map = {}
    for state in north: region_map[state] = 'North'
    for state in south: region_map[state] = 'South'
    for state in east: region_map[state] = 'East'
    for state in west: region_map[state] = 'West'
    for state in central: region_map[state] = 'Central'
    for state in northeast: region_map[state] = 'Northeast'
    
    # Add region column
    df['Region'] = df['State/UT'].map(region_map)
    
    # Calculate regional statistics
    regional_stats = df.groupby('Region').agg({
        'Total_Accidents': 'sum',
        'Total_Deaths': 'sum',
        'Total_Injuries': 'sum'
    }).round(2)
    
    regional_stats['Fatality_Rate'] = (regional_stats['Total_Deaths'] / regional_stats['Total_Accidents'] * 100).round(2)
    regional_stats['Injury_Rate'] = (regional_stats['Total_Injuries'] / regional_stats['Total_Accidents'] * 100).round(2)
    
    return regional_stats

def analyze_severity_metrics(df):
    """Analyze severity metrics across states"""
    severity_metrics = df.nlargest(10, 'Fatality_Rate')[['State/UT', 'Fatality_Rate', 'Injury_Rate']]
    return severity_metrics
