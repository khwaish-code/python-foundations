import statistics

data = [10, 20, 30, 40, 50, 60, 70]

print("Data:", data)

mean_value = statistics.mean(data)

median_value = statistics.median(data)

mode_value = statistics.mode(data)

variance_value = statistics.variance(data)

std_dev = statistics.stdev(data)

minimum = min(data)
maximum = max(data)

range_value = maximum - minimum

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Range:", range_value)