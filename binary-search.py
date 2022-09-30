list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

def binary_search(list, item):
    low = list[0]
    high = list[len(list) - 1]

    

    while low <= high:
        mid = list[int((high - low)/2)]

        if item == mid:
            return mid

        if item < mid:
            high = mid

        if item > mid:
            low = mid 
        
    return None

        
    

print(binary_search(list, 3))
# run code: python3 binary-search.py