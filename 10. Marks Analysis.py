scores = [65, 78, 85, 90, 45, 85, 90, 72, 85, 90, 60, 85, 78, 90, 92, 85, 70, 64, 85, 90]


avg = sum(scores) / len(scores)
print("Average score:", round(avg, 2))


above_avg = 0
for s in scores:
    if s > avg:
        above_avg += 1
print("Students scoring above average:", above_avg)


most_common = max(scores, key=scores.count)
print("Most frequent score:", most_common)