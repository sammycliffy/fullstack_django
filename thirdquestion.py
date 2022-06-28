def max_wealth(houses):
    n = len(houses)
    if n == 0:
        return 0
    value1 = houses[0]
    if n == 1:
        return value1
    value2 = max(houses[0], houses[1])
    if n == 2:
        return value2
    maximum_value = None
    for i in range(2, n):
        maximum_value = max(houses[i]+value1, value2)
        value1 = value2
        value2 = maximum_value
    return maximum_value
 
def main():
    houses = [2, 10, 14, 8, 1] 
   
    print("Outpout : {}".format(max_wealth(houses)))
 
if __name__ == '__main__':
    main()