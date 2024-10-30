test_scores = [9, 8, 4, 10, 8, 8, 2, 6, 7,8, 9, 4, 7, 5, 10, 9, 8, 8, 7, 6, 7, 5, 8]

sum = 0

for x in test_scores:
    sum += x

# print(sum)

# print(max(test_scores))

# REPLICATE MAX FUNCTION USING LOOPS

top_score = 0

for x in test_scores:
    if x > top_score:
        top_score = x
    
print(top_score)