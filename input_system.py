import pygame
from pygame.locals import *
import GAME_GLOBALS

from action import WalkAction
from direction import Direction

class InputSystem:
    def __init__(self, game):
        print 'a'
        self.game = game

    def controls(self):
        event = pygame.event.poll()
        if event.type == pygame.NOEVENT:
            return
        elif event.type == KEYDOWN:
            if event.key == pygame.K_w:
                self.walk(Direction.UP)
            if event.key == pygame.K_s:
                self.walk(Direction.DOWN)
            if event.key == pygame.K_a:
                self.walk(Direction.LEFT)
            if event.key == pygame.K_d:
                self.walk(Direction.RIGHT)


    def wait_for_input(self):
        pygame.event.clear()
        no_event = True

        while no_event:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:

                if event.key == pygame.K_w:
                    self.walk(Direction.UP)
                    no_event = False
                if event.key == pygame.K_s:
                    self.walk(Direction.DOWN)
                    no_event = False
                if event.key == pygame.K_a:
                     self.walk(Direction.LEFT)
                     no_event = False
                if event.key == pygame.K_d:
                     self.walk(Direction.RIGHT)
                     no_event = False

                # UTIL CONTROLS
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    def walk(self, direction):
        self.game.player.set_next_action(WalkAction(self.game.player, direction))