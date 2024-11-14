# Given an array representing the heights of towers, the task is to find, for each tower, the index of the nearest tower that is shorter than it.
# The search for a shorter tower can be performed by looking to the left and right sides of each tower.

# The following rules apply:

# If there are two or more smaller towers at the same distance from the current tower, choose the tower with the smallest height.
# If two towers have the same height, choose the one with the smaller index.

def nearest_shorter_tower(heights):
    n = len(heights)
    result = [-1] * n  # Start with -1 (means no shorter tower found)

    for i in range(n):
        left_index = -1
        right_index = -1

        # Check left side
        for j in range(i - 1, -1, -1):
            if heights[j] < heights[i]:
                left_index = j
                break

        # Check right side
        for k in range(i + 1, n):
            if heights[k] < heights[i]:
                right_index = k
                break

        # Compare distances
        if left_index == -1:
            result[i] = right_index
        elif right_index == -1:
            result[i] = left_index
        else:
            if abs(i - left_index) < abs(i - right_index):
                result[i] = left_index
            elif abs(i - left_index) > abs(i - right_index):
                result[i] = right_index
            else:  # Same distance, choose the shorter one
                if heights[left_index] <= heights[right_index]:
                    result[i] = left_index
                else:
                    result[i] = right_index

    return result

# Example usage:
heights = [7, 3, 4, 9, 2]
print(nearest_shorter_tower(heights))  # Output: [1, 4, 1, 2, -1]
