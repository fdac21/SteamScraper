import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def read_dlc():
    with open("matthew/test_dlc.csv", encoding="utf-8") as dlc:
        values = []
        for line in dlc.readlines():
            values.append(line.strip().split(','))
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
    


def analyze(values, genre = ''):
    error_count = 0
    prices = []
    percentages = []
    for row in values:
        for value in row:
            if '$' in value:
                v = value
                if '%' in value:
                    index = value.rfind('$') + 1
                    v = value[index:]
                    index2 = value.find('%')
                    percentages.append(float(value[2:index2]))
                x = v.replace('$', '')
                try:
                    price = float(x)
                except ValueError:
                    error_count += 1
                    continue
                prices.append(price)
            if "Free" in value or "free" in value:
                prices.append(0.0)

    nprice = output(prices, "PRICES")
    print("     # DLCs ignored due to bad formatting: ", error_count)
    npercent = output(percentages, "PERCENTAGE OFF")

    histogram = plt.hist(nprice, bins=10, range=[0.0, 50])
    if genre == '':
        plt.title("All Steam DLC Prices")
    else:
        plt.title("Steam DLC Prices: " + genre)
    plt.xlabel("Price of DLC in USD")
    plt.ylabel("Number of DLC")
    plt.show()
    
    histogram1 = plt.hist(npercent, bins=5, range=[0.0, 100])
    if genre == '':
        plt.title("All Steam DLC Sales")
    else:
        plt.title("Steam DLC Sales: " + genre)
    plt.xlabel("Percentage off original price")
    plt.ylabel("Number of DLC")
    plt.show()
    
if __name__ == "__main__":
    dlc = read_dlc()
    analyze(dlc)