def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    a = []
    number = int(input("Please Enter the Total Number of Elements: "))
    for i in range(number):
        value = int(input(f"Please enter the {i} Element: "))
        a.append(value)
    print("The Sorted List in Ascending Order:", bubble_sort(a))
