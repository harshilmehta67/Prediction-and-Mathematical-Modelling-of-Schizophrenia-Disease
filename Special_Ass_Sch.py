import numpy as np
import random
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function for getting probability for given values of Allene Frequency


def get_Probability_factor(mul, input):
    return input*(mul*mul + 2*mul*(1-mul))  # (1/x) * (p^2 + 2*p*q)

# Utility function for splitting 2D data into 3D


def gen_pairs_forPlot(x):
    for i in range(0, len(x)):
        temp = random.uniform(20, 160)
        New_x.append(temp)
        New_y.append(x[i] / temp)
    # print(New_x)
    # print(New_y)

# Unknown Work - requires major altercations
# Future Work


def gen_OddRatio(work, work_2):
    return (work / (1 - work)) / (work_2 / (1 - work_2))

# Utility Function for getting 2D graph


def plot_graph(x, y):
    plt.plot(x, y, color='green', linestyle='solid')
    plt.xlabel('x - axis as N-T')
    plt.ylabel('y - axis as Probability of offspring being diseased')
    plt.figure()

# Utility Function to clear all existing arrays


def clear_arrays(x, y, z, w):
    x.clear()
    y.clear()
    z.clear()
    w.clear()

# Final Function for plotting 3D graph


def plot_graph_3D(x, y, z):
    x.sort()
    y.sort()
    z.sort()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z, color='blue', linestyle='solid',
            label='Probability vs N & T')
    ax.legend()
    ax.set_xlabel('N')
    ax.set_ylabel('T')
    ax.set_zlabel('Probability')

# Utility Function for generating random test data set for generating graph


def get_data(ratio, starPoint, endPoint):
    for _ in range(1, 100):
        temp = random.uniform(starPoint, endPoint)
        threshold_freq.append(temp)
        Probabilities_ans.append(get_Probability_factor(temp, ratio))

# Function for Solving Joint Probability and Mathematical Equations with Auxilary output function


def solve_probability_case(Allele_A_freq, Allele_B_freq, case_study):
    # Joint Probability
    B_a = Allele_A_freq  # given probability of type A genes in person A
    b_a = 1 - Allele_A_freq
    B_b = Allele_B_freq  # given probability of type B genes in person B
    b_b = 1 - Allele_B_freq
    Probability_schizophrenia = 1 * \
        (B_a*B_b + B_a*b_b + B_b*b_a)  # Total Probability Theorem
    print('Relative Probability of OffSpring having Schizophrenia in Case when ' + case_study)
    print(Probability_schizophrenia)
    # Final Probability for diseased offspring
    return Probability_schizophrenia
    # print(1 - Probability_schizophrenia)


if __name__ == "__main__":

    total_population = 7000000000
    patient_population = 0.01*total_population
    non_patient_population = 0.99*total_population
    Sum_of_all_Prob = 0

    # 3 cases of any offspring
    # Case : 1 -> PP x PP
    # Case : 2 -> NP x NP
    # Case : 3 -> PP x NP

    # Case study for #1 Case
    case_study = 'Both Parents are in Patient Population'
    threshold_freq = []
    New_x = []
    Probabilities_ans = []
    New_y = []
    get_data((0.01*0.01), 0.8, 0.99)
    gen_pairs_forPlot(threshold_freq)
    plot_graph_3D(New_x, New_y, Probabilities_ans)
    Sum_of_all_Prob += (0.01)*(0.01)*solve_probability_case(0.8, 0.8, case_study)

    # Case study for #2 Case
    case_study = 'Both Parents are in Non Patient Population'
    clear_arrays(threshold_freq, New_x, New_y, Probabilities_ans)
    get_data((0.99*0.99), 0.00001, 0.01)
    gen_pairs_forPlot(threshold_freq)
    plot_graph_3D(New_x, New_y, Probabilities_ans)
    Sum_of_all_Prob += (0.99)*(0.99)*solve_probability_case(0.01, 0.01, case_study)

    # Case study for #3 Case
    case_study = 'One parent is in Non patient Population and other in Patient Population'
    clear_arrays(New_x, New_y, threshold_freq, Probabilities_ans)
    get_data((0.99*0.01), random.uniform(0.001, 0.01),
             random.uniform(0.8, 0.95))
    gen_pairs_forPlot(threshold_freq)
    plot_graph_3D(New_x, New_y, Probabilities_ans)
    Sum_of_all_Prob += (0.01)*(0.99)*solve_probability_case(0.01, 0.8, case_study)

    print('Final Sum of Probability over every variations = ' + str(Sum_of_all_Prob))
    plt.show()
