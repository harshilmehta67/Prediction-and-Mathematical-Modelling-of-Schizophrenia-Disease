import numpy as np
import random
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function for getting probability for given values of Allene Frequency


def get_Probability_factor(input, mul):
    return input*(mul*mul + 2*mul*(1-mul))  # (1/x) * (p^2 + 2*p*q)

# Working on it .. function for splitting 2D data into 3D
# Someone Help over in this part!!


def gen_pairs_forPlot(x):
    for i in range(0, len(x)):
        temp = random.uniform(20, 160)
        New_x.append(temp)
        New_y.append(x[i] / temp)
    # print(New_x)
    # print(New_y)

# Unknown Dhap - requires major altercations


def gen_OddRatio(dhap, non_dhap):
    return (dhap / (1 - dhap)) / (non_dhap / (1 - non_dhap))

# Auxilary Function for getting 2D graph


def plot_graph(x, y):
    plt.plot(x, y, color='green', linestyle='solid')
    plt.xlabel('x - axis as N-T')
    plt.ylabel('y - axis as Probability of offspring being diseased')
    plt.figure()


def plot_graph_demo(x, y, z):
    x.sort()
    y.sort()
    z.sort()
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, color='blue', linestyle='solid')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Function for generating random test data set for generating graph


def get_data(ratio, starPoint, endPoint):
    for _ in range(1, 20):
        temp = random.uniform(starPoint, endPoint)
        threshold_freq.append(temp)
        Probabilities_ans.append(get_Probability_factor(temp, ratio))

# Function for Solving Joint Probability and Mathematical Equations with Auxilary output function


def solve_probability_case(typeA_pop, typeB_pop, total_population, Allele_A_freq, Allele_B_freq, case_study):
    chance_of_case = (typeA_pop/total_population * typeB_pop /
                      total_population)  # Joint Probability
    B_a = Allele_A_freq  # given probability of type A genes in person A
    b_a = 1 - Allele_A_freq
    B_b = Allele_B_freq  # given probability of type B genes in person B
    b_b = 1 - Allele_B_freq
    Probability_schizophrenia = chance_of_case * \
        (B_a*B_b + B_a*b_b + B_b*b_a)  # Total Probability Theorem
    print('Probability of OffSpring having Schizophrenia in Case when ' + case_study)
    # Final Probability for diseased offspring
    print(Probability_schizophrenia)
    # print(1 - Probability_schizophrenia)


if __name__ == "__main__":
    total_population = 7000000000
    patient_population = 0.01*total_population
    non_patient_population = 0.99*total_population
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
    get_data((0.01*0.01), 0.8, 0.95)
    gen_pairs_forPlot(threshold_freq)
    plot_graph_demo(New_x, New_y, Probabilities_ans)
    solve_probability_case(
        patient_population, patient_population, total_population, 0.8, 0.8, case_study)

    # Case study for #2 Case
    case_study = 'Both Parents are in Non Patient Population'
    threshold_freq.clear()
    Probabilities_ans.clear()
    get_data((0.99*0.99), 0.00001, 0.01)
    # plot_graph(threshold_freq, Probabilities_ans)
    # solve_probability_case(non_patient_population, non_patient_population,
    #                        total_population, 0.01, 0.01, case_study)

    # Case study for #3 Case*
    case_study = 'One parent is in Non patient Population and other in Patient Population'
    threshold_freq.clear()
    Probabilities_ans.clear()
    get_data((0.99*0.01), random.uniform(0.001, 0.01),
             random.uniform(0.8, 0.95))

    # AA COMENTS KADHINE CODE READY KAR


    # plot_graph(threshold_freq, Probabilities_ans)
    # solve_probability_case(non_patient_population, patient_population,
    #                        total_population, 0.01, 0.8, case_study)

    # plt.show()
