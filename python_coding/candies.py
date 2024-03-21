def kidswithcandies(candies, extracandies):
    max_candies = max(candies)
    result=[]
    for i in candies:
        print(i)
        if i + extracandies >= max_candies:

           result.append(True)
        else:
            result.append(False)
    return result

candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidswithcandies(candies, extraCandies))