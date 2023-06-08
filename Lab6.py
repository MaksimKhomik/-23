import math

# отримання даних від користувача
num_tasks = int(input("Введіть кількість завдань: "))
tasks = []
for i in range(num_tasks):
    a = float(input(f"Введіть оцінку a для завдання {i+1}: "))
    m = float(input(f"Введіть оцінку m для завдання {i+1}: "))
    b = float(input(f"Введіть оцінку b для завдання {i+1}: "))
    tasks.append((a, m, b))

# розрахунок оцінки та стандартного відхилення для кожного завдання
E_tasks = []
SD_tasks = []
for task in tasks:
    a, m, b = task
    E = (a + 4*m + b) / 6
    SD = (b - a) / 6
    E_tasks.append(E)
    SD_tasks.append(SD)

# розрахунок оцінки та стандартного відхилення для проекту
E_project = sum(E_tasks)
SD_project = math.sqrt(sum([x**2 for x in SD_tasks]))

# розрахунок довірчого інтервалу
CI_min = E_project - 2 * SD_project
CI_max = E_project + 2 * SD_project

# виведення результатів
print(f"Project's 95% confidence interval: {round(CI_min, 2)} ... {round(CI_max, 2)} points")
