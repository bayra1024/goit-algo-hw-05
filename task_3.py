import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def measure_time(algorithm, text, pattern):
    # Функція для вимірювання часу виконання алгоритму
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


# Зчитування текстових файлів
with open("./text_1.txt", "r", encoding="utf-8") as file:
    article1 = file.read()

with open("./text_2.txt", "r", encoding="utf-8") as file:
    article2 = file.read()

# Задання підрядків
existing_pattern = "binarySearch"
fake_pattern = "чудові рози у саду"

# Вимірювання часу для кожного алгоритму та виду підрядка
boyer_moore_existing_time = measure_time(boyer_moore_search, article1, existing_pattern)
boyer_moore_fake_time = measure_time(boyer_moore_search, article1, fake_pattern)

kmp_existing_time = measure_time(kmp_search, article1, existing_pattern)
kmp_fake_time = measure_time(kmp_search, article1, fake_pattern)

rabin_karp_existing_time = measure_time(rabin_karp_search, article1, existing_pattern)
rabin_karp_fake_time = measure_time(rabin_karp_search, article1, fake_pattern)


# Задання підрядків
existing_pattern2 = "Editors Ricci"
fake_pattern2 = "чудові рози у саду"

# Вимірювання часу для кожного алгоритму та виду підрядка
boyer_moore_existing_time2 = measure_time(
    boyer_moore_search, article2, existing_pattern2
)
boyer_moore_fake_time2 = measure_time(boyer_moore_search, article2, fake_pattern2)

kmp_existing_time2 = measure_time(kmp_search, article2, existing_pattern2)
kmp_fake_time2 = measure_time(kmp_search, article2, fake_pattern2)

rabin_karp_existing_time2 = measure_time(rabin_karp_search, article2, existing_pattern2)
rabin_karp_fake_time2 = measure_time(rabin_karp_search, article2, fake_pattern2)

# Вивід результатів для статті 1
print("Алгоритм Боєра-Мура:")
print("Час для існуючого підрядка:", boyer_moore_existing_time)
print("Час для вигаданого підрядка:", boyer_moore_fake_time)


print("Алгоритм Кнута-Морріса-Прата:")
print("Час для існуючого підрядка:", kmp_existing_time)
print("Час для вигаданого підрядка:", kmp_fake_time)


print("Алгоритм Рабіна-Карпа:")
print("Час для існуючого підрядка:", rabin_karp_existing_time)
print("Час для вигаданого підрядка:", rabin_karp_fake_time)


# Повторення того ж самого для статті 2
# Вивід результатів для статті 2
print("Алгоритм Боєра-Мура:")
print("Час для існуючого підрядка2:", boyer_moore_existing_time2)
print("Час для вигаданого підрядка2:", boyer_moore_fake_time2)


print("Алгоритм Кнута-Морріса-Прата:")
print("Час для існуючого підрядка2:", kmp_existing_time2)
print("Час для вигаданого підрядка2:", kmp_fake_time2)


print("Алгоритм Рабіна-Карпа:")
print("Час для існуючого підрядка2:", rabin_karp_existing_time2)
print("Час для вигаданого підрядка2:", rabin_karp_fake_time2)
