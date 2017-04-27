from matplotlib import pyplot as plt

years = [1950, 1960, 1970,1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()


movies = ["Annie Hall", "Ben-Hur", "Casablance", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.title("My Favorite Movies")
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()
