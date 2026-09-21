# PLP Python Week 3 Assignment

This repository contains two small programs practicing Python loops and conditional statements.

## Files Included
* **grade_reporter.py**: Loops through student scores to output custom text grades, pass/fail counts, and class averages.
* **bug_hunt.py**: A math loop program that has been debugged to correctly add numbers 1 through 5 together.

## Bug Hunt Reflection
The hardest bug to find in Part B was the loop boundary checking condition (`count < 5`). It did not generate a computer error message to warn me, so the script ran cleanly but printed out an incorrect sum of 10. I only realized it was broken because the final math output didn't equal the expected goal of 15, forcing me to read through the loop steps line by line.
