import heapq

def merge_k_lists(sorted_lists):

    # Створимо мін-купу
    min_heap = []
    
    # Додаємо перші елементи всіх списків до купи
    for i, lst in enumerate(sorted_lists):
        if lst:  # Перевіряємо, чи список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)
    
    result = []
    
    # Поки в купі є елементи
    while min_heap:
        value, list_idx, elem_idx = heapq.heappop(min_heap)  # Вилучаємо найменший елемент
        result.append(value)  # Додаємо його до результату
        
        # Якщо у відповідному списку є ще елементи, додаємо їх до купи
        if elem_idx + 1 < len(sorted_lists[list_idx]):
            next_value = sorted_lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, elem_idx + 1))
    
    return result

# Тестування
sorted_lists = [
    [1, 5, 7],
    [2, 4, 8],
    [3, 6, 11],
    [0, 9, 10, 12, 13]
]

print("Вхідні списки:", sorted_lists)
merged_list = merge_k_lists(sorted_lists)
print("Об'єднаний відсортований список:", merged_list)