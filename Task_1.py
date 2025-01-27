import heapq

def min_cable_connection_cost(cables):
 
    if not cables:
        return 0  # Якщо список порожній, витрати дорівнюють 0
    
    # Перетворюємо список довжин кабелів на купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Виймаємо два найкоротших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # З'єднуємо їх і додаємо витрати
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Тестування
cables = [4, 3, 2, 6]  # Вхідні довжини кабелів
print("Довжини кабелів:", cables)
min_cost = min_cable_connection_cost(cables)
print("Мінімальні витрати на з'єднання:", min_cost)