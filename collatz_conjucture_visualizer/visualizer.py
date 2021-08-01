from typing import List, Tuple

import pygame.display
from pygame.surface import Surface
import pygame as pg

BACKGROUND_COLOR = (210, 210, 210)  # Light gray
LINE_COLOR = (255, 51, 51)  # Red


def collatz_solution(num: int) -> List[int]:
    """
    Solves collatz conjecture for the specified number. Each term is obtained from the previous term.
    If the previous term is even, the next term is one half of the previous term. If the previous term is odd,
    the next term is 3 times the previous term plus 1.
    :param num: integer to solve using collatz
    :return: list of terms for the specified num
    """
    pass


def collatz_conjecture_solution_surface(solution_terms: List[int]) -> Surface:
    """
    Takes a list of terms representing a Collatz Conjecture solution and generates a Pygame Surface with the
    visualisation. The surface is rotated to keep the end of the solution always at the same place, allowing
    the surfaces of different solutions to be overlapped in a single visualisation later.
    :param solution_terms: list of integers with the terms of the solution of a single number.
    :return: Surface with visualization for one solution.
    """
    pass


def draw_line(where: Surface, is_even: bool, last_line_ending_pos: Tuple[int, int]) -> None:
    """
    Draw line on a surface representing one term of the visualization. Even terms are drawn with one angle,
    odd terms are drawn with another. Line starts where the last one ended.
    :param where: Surface in which to draw the line(Surface representing solution to one number).
    :param is_even: if the current term is even or odd.
    :param last_line_ending_pos: Tuple with x and y position of the last drawn line.
    :return:
    """
    pass


def overlap_solutions(solutions: List[Surface]) -> Surface:
    """
    Overlap all the generated surfaces into one, creating a tree-looking structure with all solution Surfaces.
    :param solutions: List of solutions generated for different numbers
    :return: a single Surface with all solutions overlapped
    """
    pass


def main():
    solutions = (collatz_solution(num) for num in range(2000))
    result = overlap_solutions([collatz_conjecture_solution_surface(solution) for solution in solutions])
    pg.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill(BACKGROUND_COLOR)
    screen.blit(result, (0, 0))
    pg.display.flip()


if __name__ == "__main__":
    main()

