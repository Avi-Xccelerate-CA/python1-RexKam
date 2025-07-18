# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    if sum(needs) > 500 or any(n >= 250 for n in needs):
        return "No medicine given"

    result = []
    for value in needs:
        vitamins = (value + 9) // 10
        injections = vitamins * 10 - value
        result.append((vitamins, injections))
    return result


    #YOUR SOLUTION ENDS HERE
