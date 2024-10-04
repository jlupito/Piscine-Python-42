from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# height = [1.71, 1.55]
# weight = [65.3, 50.4, 100.7]
# bmi = give_bmi(height, weight)

# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))

# height = [1.71, 0, 1.82]
# weight = [65.3, 50.4, 100.7]
# bmi = give_bmi(height, weight)

# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
