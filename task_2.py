def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] >= target:
            right = mid - 1

    if left >= len(arr):
        return (iterations, None)
    else:
        upper_bound = arr[left]
        return (iterations, upper_bound)


def main():
    sorted_array = [0.1, 0.5, 1.2, 1.8, 2.5, 3.0, 4.2, 5.1]
    target_value = 2.0

    result = binary_search(sorted_array, target_value)
    print(f"Кількість ітерацій: {result[0]}")
    print(f"Верхня межа: {result[1]}")

    if result[1]:
        print("Елемент знайдено в масиві")
    else:
        print("Елемент відсутній в масиві")


if __name__ == "__main__":
    main()
