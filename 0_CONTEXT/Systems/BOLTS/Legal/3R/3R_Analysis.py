from typing import Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd
import csv
import os
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

def ensure_output_folder_exists(folder: str) -> None:
    # Ensures that the output folder exists. If it does not, it creates it.
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

def load_3R_data_from_csv(file_path: str) -> Dict[str, Any]:
    # Loads the 3R data from a CSV file and returns a dictionary of context statistics.
    #
    # Parameters:
    # - file_path (str): The path to the CSV file.
    #
    # Returns:
    # - Dict[str, Any]: A dictionary containing the context statistics.
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        
        # Print column headers and first data row for schema confirmation
        if data:
            print("Column Headers:", reader.fieldnames)
            print("First Data Row:", data[0])
        else:
            print("The CSV file is empty.")
    
    context_stats = {
        "total_recognize_events": len(data),
        "recognize_methods": [row["Recognize"] for row in data],
        "remember_methods": [row["Remember"] for row in data],
        "respond_methods": [row["Respond"] for row in data],
        "recognize_time_distribution": [row["UTC Timestamp"] for row in data],
        "remember_time_distribution": [row["UTC Timestamp"] for row in data],
        "respond_time_distribution": [row["UTC Timestamp"] for row in data],
        "risk_scores": [int(row["Risk Score"]) for row in data],
        "settings": [row["Setting"] for row in data],
        "sub_domains": [row["Sub-domain"] for row in data]
    }
    return context_stats

def print_3R_summary(summary: Dict[str, Any]) -> None:
    # Prints a summary of the 3R context statistics.
    #
    # Parameters:
    # - summary (Dict[str, Any]): A dictionary containing the context statistics.
    print("3R Summary:")
    for key, value in summary.items():
        print(f"{key.capitalize()}:")
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"  {key}_list: {value}")

def visualize_3R_summary(summary: Dict[str, Any], output_folder: str) -> None:
    # Visualizes the 3R context statistics.
    #
    # Parameters:
    # - summary (Dict[str, Any]): A dictionary containing the context statistics.
    # - output_folder (str): The folder where the visualizations will be saved.
    
    # Word cloud for recognize methods
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["recognize_methods"]))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    wordcloud_file_path = os.path.join(output_folder, "recognize_methods_wordcloud.png")
    plt.savefig(wordcloud_file_path)
    print(f"Recognize methods word cloud saved to {wordcloud_file_path}")

    # Bar plot for recognize methods
    plt.figure(figsize=(12, 8))
    recognize_methods_series = pd.Series(summary["recognize_methods"])
    sns.countplot(y=recognize_methods_series, order=recognize_methods_series.value_counts().index)
    plt.title('Count of Recognize Methods')
    plt.xlabel('Count')
    plt.ylabel('Recognize Method')
    recognize_methods_plot_path = os.path.join(output_folder, "recognize_methods_countplot.png")
    plt.savefig(recognize_methods_plot_path)
    plt.close()
    print(f"Count plot of recognize methods saved to {recognize_methods_plot_path}")

    # Bar plot for remember methods
    plt.figure(figsize=(12, 8))
    remember_methods_series = pd.Series(summary["remember_methods"])
    sns.countplot(y=remember_methods_series, order=remember_methods_series.value_counts().index)
    plt.title('Count of Remember Methods')
    plt.xlabel('Count')
    plt.ylabel('Remember Method')
    remember_methods_plot_path = os.path.join(output_folder, "remember_methods_countplot.png")
    plt.savefig(remember_methods_plot_path)
    plt.close()
    print(f"Count plot of remember methods saved to {remember_methods_plot_path}")

    # Bar plot for respond methods
    plt.figure(figsize=(12, 8))
    respond_methods_series = pd.Series(summary["respond_methods"])
    sns.countplot(y=respond_methods_series, order=respond_methods_series.value_counts().index)
    plt.title('Count of Respond Methods')
    plt.xlabel('Count')
    plt.ylabel('Respond Method')
    respond_methods_plot_path = os.path.join(output_folder, "respond_methods_countplot.png")
    plt.savefig(respond_methods_plot_path)
    plt.close()
    print(f"Count plot of respond methods saved to {respond_methods_plot_path}")

    # Violin plot for risk scores
    plt.figure(figsize=(12, 8))
    sns.violinplot(x=summary["risk_scores"])
    plt.title('Violin Plot of Risk Scores')
    plt.xlabel('Risk Score')
    violinplot_file_path = os.path.join(output_folder, "risk_scores_violinplot.png")
    plt.savefig(violinplot_file_path)
    plt.close()
    print(f"Violin plot of risk scores saved to {violinplot_file_path}")

    # Heatmap of Recognize vs Remember methods
    plt.figure(figsize=(15, 10))
    recognize_remember_df = pd.DataFrame({'Recognize': summary["recognize_methods"], 'Remember': summary["remember_methods"]})
    heatmap_data = pd.crosstab(recognize_remember_df['Recognize'], recognize_remember_df['Remember'])
    sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu')
    plt.title('Heatmap of Recognize vs Remember Methods')
    plt.tight_layout()
    heatmap_file_path = os.path.join(output_folder, "recognize_remember_heatmap.png")
    plt.savefig(heatmap_file_path)
    plt.close()
    print(f"Heatmap of Recognize vs Remember methods saved to {heatmap_file_path}")

    # Scatter plot of Risk Scores vs Settings
    plt.figure(figsize=(15, 10))
    settings_risk_df = pd.DataFrame({'Setting': summary["settings"], 'Risk Score': summary["risk_scores"]})
    sns.scatterplot(x='Setting', y='Risk Score', data=settings_risk_df)
    plt.xticks(rotation=45, ha='right')
    plt.title('Scatter Plot of Risk Scores vs Settings')
    plt.tight_layout()
    scatter_file_path = os.path.join(output_folder, "risk_scores_settings_scatter.png")
    plt.savefig(scatter_file_path)
    plt.close()
    print(f"Scatter plot of Risk Scores vs Settings saved to {scatter_file_path}")

    # Violin plot of Risk Scores by Sub-domain
    plt.figure(figsize=(15, 10))
    subdomain_risk_df = pd.DataFrame({'Sub-domain': summary["sub_domains"], 'Risk Score': summary["risk_scores"]})
    sns.violinplot(x='Sub-domain', y='Risk Score', data=subdomain_risk_df)
    plt.title('Violin Plot of Risk Scores by Sub-domain')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    violin_subdomain_file_path = os.path.join(output_folder, "risk_scores_subdomain_violin.png")
    plt.savefig(violin_subdomain_file_path)
    plt.close()
    print(f"Violin plot of Risk Scores by Sub-domain saved to {violin_subdomain_file_path}")

    # Combination plot for the 3R's
    fig, axes = plt.subplots(3, 3, figsize=(20, 20))
    fig.suptitle('3R Combination Plot')

    # Recognize vs Recognize
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["recognize_methods"]))
    axes[0, 0].imshow(wordcloud, interpolation='bilinear')
    axes[0, 0].axis('off')
    axes[0, 0].set_title('Recognize vs Recognize')

    # Recognize vs Remember
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["remember_methods"]))
    axes[0, 1].imshow(wordcloud, interpolation='bilinear')
    axes[0, 1].axis('off')
    axes[0, 1].set_title('Recognize vs Remember')

    # Recognize vs Respond
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["respond_methods"]))
    axes[0, 2].imshow(wordcloud, interpolation='bilinear')
    axes[0, 2].axis('off')
    axes[0, 2].set_title('Recognize vs Respond')

    # Remember vs Recognize
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["recognize_methods"]))
    axes[1, 0].imshow(wordcloud, interpolation='bilinear')
    axes[1, 0].axis('off')
    axes[1, 0].set_title('Remember vs Recognize')

    # Remember vs Remember
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["remember_methods"]))
    axes[1, 1].imshow(wordcloud, interpolation='bilinear')
    axes[1, 1].axis('off')
    axes[1, 1].set_title('Remember vs Remember')

    # Remember vs Respond
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["respond_methods"]))
    axes[1, 2].imshow(wordcloud, interpolation='bilinear')
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Remember vs Respond')

    # Respond vs Recognize
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["recognize_methods"]))
    axes[2, 0].imshow(wordcloud, interpolation='bilinear')
    axes[2, 0].axis('off')
    axes[2, 0].set_title('Respond vs Recognize')

    # Respond vs Remember
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["remember_methods"]))
    axes[2, 1].imshow(wordcloud, interpolation='bilinear')
    axes[2, 1].axis('off')
    axes[2, 1].set_title('Respond vs Remember')

    # Respond vs Respond
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(summary["respond_methods"]))
    axes[2, 2].imshow(wordcloud, interpolation='bilinear')
    axes[2, 2].axis('off')
    axes[2, 2].set_title('Respond vs Respond')

    combination_plot_path = os.path.join(output_folder, "3R_combination_plot.png")
    plt.savefig(combination_plot_path)
    plt.close()
    print(f"3R combination plot saved to {combination_plot_path}")

    # Time series plot of Risk Scores
    plt.figure(figsize=(15, 10))
    time_risk_df = pd.DataFrame({
        'Timestamp': pd.to_datetime(summary["recognize_time_distribution"]),
        'Risk Score': summary["risk_scores"],
        'Sub-domain': summary["sub_domains"]
    })
    time_risk_df = time_risk_df.sort_values('Timestamp')
    
    # Add jitter to the points
    time_risk_df['Jittered_Risk'] = time_risk_df['Risk Score'] + np.random.normal(0, 0.5, len(time_risk_df))
    
    # Plot jittered points
    sns.scatterplot(x='Timestamp', y='Jittered_Risk', hue='Sub-domain', data=time_risk_df, alpha=0.6)
    
    plt.title('Risk Scores Over Time by Sub-domain')
    plt.xlabel('Time')
    plt.ylabel('Risk Score')
    plt.xticks(rotation=45)
    plt.legend(title='Sub-domain', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    timeseries_plot_path = os.path.join(output_folder, "risk_scores_timeseries.png")
    plt.savefig(timeseries_plot_path)
    plt.close()
    print(f"Time series plot of Risk Scores saved to {timeseries_plot_path}")

def save_visualizations_to_pdf(output_folder: str) -> None:
    # Saves all visualizations into a single PDF file.
    #
    # Parameters:
    # - output_folder (str): The folder where the visualizations are saved.
    pdf_path = os.path.join(output_folder, "3R_visualizations.pdf")
    with PdfPages(pdf_path) as pdf:
        for file_name in ["recognize_methods_wordcloud.png", "recognize_methods_countplot.png", "remember_methods_countplot.png", 
                          "respond_methods_countplot.png", "risk_scores_violinplot.png", "3R_combination_plot.png",
                          "recognize_remember_heatmap.png", "risk_scores_settings_scatter.png", "risk_scores_subdomain_violin.png",
                          "risk_scores_timeseries.png"]:
            file_path = os.path.join(output_folder, file_name)
            if os.path.exists(file_path):
                image = plt.imread(file_path)
                plt.figure(figsize=(12, 8))
                plt.imshow(image)
                plt.axis('off')
                pdf.savefig()
                plt.close()
    print(f"All visualizations saved to {pdf_path}")

def main():
    output_folder = "3R_Analysis"
    ensure_output_folder_exists(output_folder)

    file_path = "LegalData/synthetic_3R_data.csv"
    context_stats = load_3R_data_from_csv(file_path)

    print_3R_summary(context_stats)
    visualize_3R_summary(context_stats, output_folder)
    save_visualizations_to_pdf(output_folder)

if __name__ == "__main__":
    main()