import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(input_file, output_file, bin_width, color, file_format):
    # Read the input file into a DataFrame
    df = pd.read_csv(input_file, delimiter='\t')

    # Extract the Distance to TSS column
    distances = df['Distance to TSS']

    # Set the range for the x-axis
    min_distance = -25000
    max_distance = 25000

    # Create bins for the histogram
    bins = np.arange(min_distance, max_distance + bin_width, bin_width)

    # Plot the histogram
    plt.hist(distances, bins=bins, color=color)
    
    # Set labels and title
    plt.xlabel('Distance to TSS')
    plt.ylabel('Number of Peaks')
    plt.title('Histogram of Distance to TSS')

    # Save the plot to the specified file format
    plt.savefig(output_file, format=file_format)

    # Show the plot (optional)
    plt.show()

def main():
    # Create an ArgumentParser
    parser = argparse.ArgumentParser(description='Plot histogram based on Distance to TSS')

    # Define command line arguments
    parser.add_argument('input_file', help='Input file with chromosomal coordinates and gene names')
    parser.add_argument('output_file', help='Output file name for the histogram plot')
    parser.add_argument('--bin_width', type=int, default=500, help='Width of histogram bins (default: 500)')
    parser.add_argument('--color', default='blue', help='Color of the histogram bars (default: blue)')
    parser.add_argument('--file_format', choices=['pdf', 'png'], default='png', help='Output file format (pdf or png, default: png)')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the function to plot the histogram
    plot_histogram(args.input_file, args.output_file, args.bin_width, args.color, args.file_format)

if __name__ == "__main__":
    main()
