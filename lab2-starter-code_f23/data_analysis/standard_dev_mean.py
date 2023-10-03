#!/usr/bin/env python3

import csv
import statistics

def calculate_mean_US(file):
    "Calculate mean from US data"
    sum  = 0
    i = 0
    with open(file,'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            sum += float(line[0])
            i += 1 
    return sum/i 

def calculate_std_dev_US(file):
    "Calculate standard deviation for US data"
    std_dev = []
    with open(file,'r') as f:
       csv_reader = csv.reader(f)
       for line in csv_reader:
           std_dev.append(float(line[0]))
    return statistics.pstdev(std_dev)

def calculate_std_dev_CS(file):
    "Calculate std_dev for CS data"
    colour = {"Red": [] ,"Green": [], "Blue": []}
    with open(file,'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            colour["Red"].append(float(line[0].replace('[','')))
            colour["Green"].append(float(line[1]))
            colour["Blue"].append(float(line[2].replace(']','')))
    print(f'Standard deviation in the measurements of Red is {statistics.pstdev(colour["Red"])}')
    print(f'Standard deviation in the measurements of Green is {statistics.pstdev(colour["Green"])}')
    print(f'Standard deviation in the measurements of Blue is {statistics.pstdev(colour["Blue"])}')
    
def calculate_mean_CS(file):
    "Calculate mean for CS data"
    colour = {"Red": [] ,"Green": [], "Blue": []}
    with open(file,'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            colour["Red"].append(float(line[0].replace('[','')))
            colour["Green"].append(float(line[1]))
            colour["Blue"].append(float(line[2].replace(']','')))
    print(f'Mean in the measurements of Red is {statistics.mean(colour["Red"])}')
    print(f'Mean in the measurements of Green is {statistics.mean(colour["Green"])}')
    print(f'Mean in the measurements of Blue is {statistics.mean(colour["Blue"])}')

if __name__ == "__main__":
    # mean     = calculate_mean_US("/Users/isbatos/Desktop/us_sensor tests/us_sensor_10cm.csv")
    # stddev   = calculate_std_dev_US("/Users/isbatos/Desktop/us_sensor tests/us_sensor_10cm.csv")
    # print(f"The mean of measurement is {round(mean,4)}")
    # print(f"Standard deviation of measurement is {round(stddev,2)}")
    # calculate_std_dev_CS(r"C:\Users\Laurent\Desktop\211\color_sensor_green.csv")
    # calculate_mean_CS(r"C:\Users\Laurent\Desktop\211\color_sensor_green.csv")