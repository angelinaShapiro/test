import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame_number, img, grid, N):
    """
    Обновляет состояние сетки игры "Жизнь" на один шаг.

    Args:
        frame_number: Номер текущего кадра (не используется).
        img: Объект изображения matplotlib для обновления.
        grid: Двумерный массив NumPy, представляющий сетку.
        N: Размер сетки (N x N).

    Returns:
        Список объектов matplotlib, которые нужно перерисовать.
    """

    new_grid = grid.copy()  # Создаем копию сетки для обновления

    for i in range(N):
        for j in range(N):
            # Вычисляем количество живых соседей
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                        grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                        grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                        grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]))

            # Правила игры "Жизнь"
            if grid[i, j] == 1:  # Живая клетка
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0  # Умирает от одиночества или перенаселения
            else:  # Мертвая клетка
                if total == 3:
                    new_grid[i, j] = 1  # Оживает

    img.set_data(new_grid)  # Обновляем данные изображения
    grid[:] = new_grid[:]  # Обновляем исходную сетку

    return [img]  # Возвращаем список объектов для перерисовки


def main():
    """
    Настраивает и запускает анимацию игры "Жизнь".
    """
    N = 100  # Размер сетки (N x N)

    # Создаем случайную сетку
    grid = np.random.choice([0, 1], N * N, p=[0.5, 0.5]).reshape(N, N) #Изначально 50% сетки мертво, 50% живое

    # Настраиваем matplotlib
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')  # Создаем изображение сетки
    ax.axis('off')  # Отключаем оси

    # Запускаем анимацию
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N,),
                                  interval=50, save_count=50) #Уменьшаем интервал для большей скорости

    plt.show()  # Отображаем анимацию


if __name__ == '__main__':
    main()