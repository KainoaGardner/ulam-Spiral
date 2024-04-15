from math import sqrt

import pygame

TILEAMOUNT = 200
TILESIZE = 1000 // TILEAMOUNT
WIDTH = TILESIZE * TILEAMOUNT
HEIGHT = TILESIZE * TILEAMOUNT
WHITE = "#bdc3c7"
RED = "#e74c3c"
GREY = "#7f8c8d"
BLACK = "#121212"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()


class ulamSpiral:
    def __init__(self, size):
        self.size = size
        self.pos = [WIDTH // 2, HEIGHT // 2]
        self.fontSize = TILESIZE
        self.font = pygame.font.Font("font/LEMONMILK-Regular.otf", self.fontSize)
        self.direction = "R"
        self.numberText = None
        self.stepIncreaseCount = 0
        self.stepCount = -1
        self.stepSize = 1

    def makeSpiral(self, screen):
        for number in range(1, self.size * 2 + 1):
            if number != 1:
                match self.direction:
                    case "R":
                        self.pos[0] += TILESIZE
                    case "U":
                        self.pos[1] -= TILESIZE
                    case "L":
                        self.pos[0] -= TILESIZE
                    case "D":
                        self.pos[1] += TILESIZE

            if self.__checkPrime(number):
                self.numberText = self.font.render(f"{number}", True, BLACK)
                pygame.draw.rect(
                    screen,
                    RED,
                    (
                        self.pos[0] - TILESIZE // 2,
                        self.pos[1] - TILESIZE // 2,
                        TILESIZE,
                        TILESIZE,
                    ),
                )
            else:
                self.numberText = self.font.render(f"{number}", True, GREY)
                while self.numberText.get_width() > TILESIZE:
                    self.fontSize -= 1
                    self.font = pygame.font.Font(
                        "font/LEMONMILK-Regular.otf", self.fontSize
                    )
                    self.numberText = self.font.render(f"{number}", True, GREY)

            screen.blit(
                self.numberText,
                (
                    self.pos[0] - self.numberText.get_width() // 2,
                    self.pos[1] - self.numberText.get_height() // 2,
                ),
            )
            self.stepCount += 1
            if self.stepCount == self.stepSize:
                self.stepCount = 0
                match self.direction:
                    case "R":
                        self.direction = "U"
                    case "U":
                        self.direction = "L"
                    case "L":
                        self.direction = "D"
                    case "D":
                        self.direction = "R"

                self.stepIncreaseCount += 1

            if self.stepIncreaseCount == 2:
                self.stepIncreaseCount = 0
                self.stepSize += 1

    def __checkPrime(self, number):
        if number <= 1:
            return False

        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False

        return True


def main():
    run = True
    screen.fill(WHITE)
    spiral = ulamSpiral(TILEAMOUNT**2)
    spiral.makeSpiral(screen)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


main()
