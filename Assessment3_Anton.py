import numpy as np
import random


def hill_climbing(start, target, choice):
    """
    At first the function creates all neighbor verities. Then, valuates discrepancy of each neighbor and chooses
    the best. This repeats till discrepancy will not equal 0.
    :param start: initial image
    :param target: target image
    :param choice: YES/NO if user want to see all steps
    :return: the best variation, number of iteration
    """
    current = start
    iterations = 0
    while score(current, target) != 0:
        iterations += 1
        print('{} iteration:'.format(iterations)) if choice == 'y' else None
        best_score = score(current, target)
        neighbors = generate_neighbors(current)
        for neighbor in neighbors:
            neighbor_score = score(neighbor, target)
            if neighbor_score < best_score:
                current = neighbor
                best_score = neighbor_score
        printing(current) if choice == 'y' else None
        print('=' * 50) if choice == 'y' else None
    return np.array(current), iterations

    # while True:
    #     print(iterations)
    #     # Generate all neighboring states
    #     best_score = score(current, target)
    #     neighbors = generate_neighbors(current)
    #     # Evaluate the neighbors and select the best one
    #     best_neighbor = None
    #     for neighbor in neighbors:
    #         neighbor_score = score(neighbor, target)
    #         if neighbor_score < best_score:
    #             best_neighbor = neighbor
    #             best_score = neighbor_score
    #
    #     if not best_neighbor:
    #         return np.array(best)
    #
    #     current = best_neighbor
    #     if score(current, target) < score(best, target):
    #         best = current
    #     iterations += 1


def generate_neighbors(state):
    """Generate all neighbors"""
    neighbors = []
    # for i in range(len(state)):
    #     for j in range(len(state[0])-1):
    #         neighbor = flip_cells(state, i, j, i, j+1)
    #         neighbors.append(neighbor)
    # for i in range(len(state) - 1):
    #     for j in range(len(state[0])):
    #         neighbor = flip_cells(state, i, j, i+1, j)
    #         neighbors.append(neighbor)
    for i in range(len(state)):
        for j in range(len(state)):
            neighbor = flip_cells2(state, i, j)
            if neighbor not in neighbors:
                neighbors.append(neighbor)
    return neighbors


def flip_cells(state, i1, j1, i2, j2):
    """Flip two adjacent cells in the state by swapping cells"""
    neighbor = [row[:] for row in state]
    neighbor[i1][j1], neighbor[i2][j2] = neighbor[i2][j2], neighbor[i1][j1]
    return neighbor


def flip_cells2(state, i, j):
    """
    Changing the value of cell
    :param state: current image
    :param i: allowable maximum for row
    :param j: allowable maximum for col
    :return: neighbor
    """
    neighbor = [row[:] for row in state]
    row, col = random.randint(0, i), random.randint(0, j)
    neighbor[row][col] = 1 - neighbor[row][col]
    return neighbor


def score(state, target):
    """
    Calculate the value of discrepancy between current image and target image
    :param state: current image
    :param target: target image
    :return: value of discrepancy
    """
    score = 0
    for i in range(len(target)):
        for j in range(len(target)):
            if state[i][j] != target[i][j]:
                score += 1
    return score


def printing(image) -> None:
    """
    Function to draw 2D array image
    :param image: array
    """
    for row in image:
        for column in row:
            print(' ' if column == 0 else '1', end='')
        print()


initial_image = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                 [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

true_image = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print('At first we have the further image:')
printing(initial_image)
best_image, num_iter = hill_climbing(initial_image, true_image, input('Do you prefer to watch each iteration? (y/n): '))
printing(best_image)
print('{} iterations was conducted'.format(num_iter))

