# Airport security officials have confiscated several item of the passengers at the security check 
# point. All the items have been dumped into a huge box (array). Each item possesses a certain 
# amount of risk[0,1,2]. Here, the risk severity of the items represent an array[] of N number of 
# integer values. The task here is to sort the items based on their levels of risk in the array. The risk 
# values range from 0 to 2.


# def risksorting(n):
#     n = int(input())
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     for i in sorted(arr):
#         print(i, end=" ")

# print(risksorting(arr))

# def sort_integers(numbers):
#     """Sorts a list of integers in ascending order.

#     Args:
#         numbers: A list of integers.

#     Returns:
#         A new list containing the sorted integers.
#     """

#     return sorted(numbers)

# # Get input from the user
# n = int(input())
# numbers = []
# for _ in range(n):
#     numbers.append(int(input()))

# # Sort the numbers and print the result
# sorted_numbers = sort_integers(numbers)
# print(*sorted_numbers)


def sorting(arr):
    a=[]
    for i in arr:
        a.append(i)
    a.sort()
    #return a
    return ''.join(map(str, a))
arr=[0,1,1,2,2,0]
print(sorting(arr))

