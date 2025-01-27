# Домашнє завдання до теми “Купи, або піраміди”

Вітаємо в домашньому завданні до теми “Купи”! 🙂

Ви вже знаєте особливості купи як структури даних, як вона реалізується, які функції дозволяють працювати з нею та як виконується алгоритм пірамідального сортування.

Наразі вам потрібно реалізувати пірамідальне сортування за допомогою модуля `heapq`.

А для тих, хто хоче поглибитись у купи, запропоновано також додаткове опціональне завдання. Бажаємо успіхів! 😎

## Опис домашнього завдання

Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.

Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

### Необов'язкове завдання

Дано `k` відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. Реалізуйте функцію `merge_k_lists`, яка приймає на вхід список відсортованих списків та повертає відсортований список.

Приклад очікуваного результату:

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
```

Виведення:

```python
Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
```

## Підготовка та завантаження домашнього завдання

1. Створіть публічний репозиторій `goit-algo-hw-08`.

2. Виконайте завдання та відправте його у свій репозиторій.

3. Завантажте робочий файл на свій комп’ютер та прикріпіть його у `LMS` у форматі `zip`. Назва архіву повинна бути у форматі `ДЗ8_ПІБ`.

4. Прикріпіть посилання на репозиторій `goit-algo-hw-08` та відправте на перевірку.

> [!IMPORTANT]
>
> 💡 ВАЖЛИВО Перегляньте Інструкцію щодо завантаження робочого файлу з репозиторію на `Github`

## Формат здачі

- Прикріплений файл репозиторію у форматі `zip` з назвою `ДЗ8_ПІБ`.
- Посилання на репозиторій.

## Критерії прийняття ДЗ

- Прикріплені посилання на репозиторій `goit-algo-hw-08` та безпосередньо сам файл репозиторію у форматі `zip`.
- Код виконується і повертає мінімальну з можливих сум загальних витрат.

> [!IMPORTANT]
>
> 💡 Необов'язкове завдання: Завдання є додатковим, тому не оцінюється, проте, за бажанням, ви можете отримати конструктивний зворотній зв’язок від ментора.

## Формат оцінювання

Залік/незалік