import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read data from the CSV file
def read_data(file_name):
    salaries = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            salaries.append(float(row[0]))
    return salaries

# Function to calculate mean salary (W~)
def calculate_mean_salary(data):
    return np.mean(data)

# Function to calculate the fraction of the population with salaries between W~ and 1.25W~
def calculate_fraction_between(data, lower, upper):
    return np.sum((data >= lower) & (data <= upper)) / len(data)

# Main code
if __name__ == "__main__":
    # Read data from the CSV file
    file_name = 'data6.csv'
    salaries_data = read_data(file_name)

    # Calculate mean annual salary (W~)
    mean_salary = calculate_mean_salary(salaries_data)

    # Calculate the fraction of population with salaries between W~ and 1.25W~
    lower_bound = mean_salary
    upper_bound = 1.25 * mean_salary
    fraction_between = calculate_fraction_between(salaries_data, lower_bound, upper_bound)

    # Set the color for the plot and text
    plot_color = 'green'
    text_color = 'darkgreen'

    # Set the background color to black
    plt.figure(facecolor='black')

    # Plot the histogram with KDE
    sns.histplot(salaries_data, bins=30, kde=True, color=plot_color, label='Empirical Probability Density Function')

    # Plot vertical lines for mean salary and 1.25 * mean salary
    plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label=f'Mean Salary (W~): {mean_salary:.2f}')
    plt.axvline(upper_bound, color='orange', linestyle='dashed', linewidth=2, label=f'1.25 * Mean Salary: {upper_bound:.2f}')

    # Display legend, labels, and title
    plt.legend()
    plt.xlabel('Annual Salary (Euros)', color=text_color)  # Set label text color to deep green
    plt.ylabel('Probability Density', color=text_color)  # Set label text color to deep green
    plt.title('Empirical Probability Density Function of Annual Salaries', color=text_color)  # Set title text color to deep green

    # Set text color to deep green
    plt.xticks(color=text_color)
    plt.yticks(color=text_color)

    # Print the calculated values on the graph
    # plt.text(upper_bound, 0.03, f'{fraction_between:.2%}', rotation=90, color=text_color)
    # plt.text(upper_bound, 0.045, f'Value X: {fraction_between:.2%}', rotation=90, color=text_color)  # Corrected to use fraction_between

    # Show the plot
    plt.show()
