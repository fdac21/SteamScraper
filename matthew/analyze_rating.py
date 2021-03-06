import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def read_rating():
    with open("test_rating.csv", encoding="utf-8") as dlc:
        values = []
        for line in dlc.readlines():
            values.append(line.split(','))
    return values

def output(arr, name):
    p = np.array(arr)
    average = np.average(p)
    median = np.median(p)
    mode = stats.mode(p)
    max = np.max(p)
    min = np.min(p)
    dev = np.std(p)
    print(name)
    print("     Mean: ", round(average, 2))
    print("     Median: ", round(median,2))
    print("     Mode: ", mode[0][0] , " | Count: ", mode[1][0])
    print("     Standard deviation: ", dev)
    print("     Min: ", min)
    print("     Max: ", max)
    print("     Total considered: ", len(p))
    return p

def analyze(rows, genre=''):
    ratings = []
    error_count = 0
    for row in rows:
        if len(row) != 3:
            continue

        if "review" not in row[2]:
            if row[2].strip() == "Overwhelmingly Positive":
                ratings.append(6)
            if row[2].strip() == "Very Positive":
                ratings.append(5)
            if row[2].strip() == "Positive" or row[2].strip() == "Mostly Positive":
                ratings.append(4)
            if row[2].strip() == "Mixed":
                ratings.append(3)
            if row[2].strip() == "Negative" or row[2].strip() == "Mostly Negative":
                ratings.append(2)
            if row[2].strip() == "Very Negative":
                ratings.append(1)
            if row[2].strip() == "Overwhelmingly Negative":
                ratings.append(0)
        else:
            error_count += 1
    r = output(ratings, "RATINGS")
    print("     # of entries removed: ", error_count)
    if 0 not in ratings:
        ratings.append(0)
    counts = np.unique(r, return_counts=True)

    print(counts)
    if 0 not in counts[0]:
        plt.bar(["Very\nNegative", "Negative", 
                     "Mixed", "Positive", "Very\nPositive", "Overwhelmingly\nPositive"], counts[1])
    elif 1 not in counts[0]:
        plt.bar(["Overwhelmingly\nNegative", "Negative", 
                     "Mixed", "Positive", "Very\nPositive", "Overwhelmingly\nPositive"], counts[1])
    elif 2 not in counts[0]:
        plt.bar(["Overwhelmingly\nNegative", "Very\nNegative",
                     "Mixed", "Positive", "Very\nPositive", "Overwhelmingly\nPositive"], counts[1])
    elif 3 not in counts[0]:
        plt.bar(["Overwhelmingly\nNegative", "Very\nNegative", "Negative", 
                    "Positive", "Very\nPositive", "Overwhelmingly\nPositive"], counts[1])
    elif 4 not in counts[0]:
        plt.bar(["Overwhelmingly\nNegative", "Very\nNegative", "Negative", 
                     "Mixed", "Very\nPositive", "Overwhelmingly\nPositive"], counts[1])
    elif 5 not in counts[0]:
        plt.bar(["Overwhelmingly\nNegative", "Very\nNegative", "Negative", 
                     "Mixed", "Positive", "Overwhelmingly\nPositive"], counts[1])
    elif 6 not in counts[0]:
        plt.bar(["Overwhelmingly\nNegative", "Very\nNegative", "Negative", 
                     "Mixed", "Positive", "Very\nPositive"], counts[1])
    else:
        plt.bar(["Overwhelmingly\nNegative", "Very\nNegative", "Negative", 
                     "Mixed", "Positive", "Very\nPositive", "Overwhelmingly\nPositive"], counts[1]) 
    
    #histogram = plt.hist(r, bins=6, range=[0, 6])
    if genre == '':
        plt.title("Steam App Ratings", fontsize=16)
    else:
        plt.title("Steam App Ratings: " + genre, fontsize=16)
    plt.xlabel("Rating", fontsize=14)
    plt.ylabel("Number of Games", fontsize=14)
    plt.show()

if __name__ == "__main__":
    analyze(read_rating())


"""
Overwhelmingly Positive - 6
Very Positive - 5
Positive / Mostly Positive - 4 (Difference based on # of reviews)
Mixed - 3
Negative / Mostly Negative - 2 (Same as positive)
Very Negative - 1
Overwhelmingly Negative - 0
"""