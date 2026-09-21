 1. This is our starting list of scores (Do not change these numbers)
scores = [72, 45, 90, 61, 38
2. We set up variables to store our counts and totals, starting at 0
pass_count = 0
fail_count = 0
total_sum = 0
3. We use a 'for' loop to look at each score in our list one by one
for score in scores:
    # Add the current score to our running total sum
    total_sum += score
 Check the conditions to assign a letter grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    # Print the individual score and its matching grade
    print("Score: " + str(score) + " -> Grade: " + grade)
    
    # Track how many students passed or failed
    if score >= 50:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

 4. Calculate the average by dividing the total sum by the amount of scores
average_score = total_sum / len(scores)

# 5. Print out the final calculated summaries
print("\n--- Summary Results ---")
print("Learners Passed: " + str(pass_count))
print("Learners Failed: " + str(fail_count))
print("Average Score: " + str(round(average_score, 1)))
