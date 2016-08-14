import pygame

from entity import Entity
from player import Player
from energy import Energy
from action import Action
from map.tile_map import TileMap
import CONSTANTS
#from tile_map import TileMap

from input_system import InputSystem
from rendering_system import RenderingSystem

class GameLoop:
    #tile_map = TileMap()
    def __init__(self):
        pygame.display.set_mode(CONSTANTS.resolution)
        print 'init gameloop'
        self.renderer = RenderingSystem()
        self.input_system = InputSystem(self)
        self.tile_map = TileMap()

        self.current_entity_index = 0
        self.player = Player(1, 7, self)
        self.entities = []
        #self.entities.append(Entity(1,3, self))
        #self.entities.append(Entity(4,3, self))
        self.entities.append(Entity(6,3, self))
        self.entities.append(self.player)


    def start(self):
        self.update()

    def update(self):
        clock = pygame.time.Clock()
        keep_looping = True

        while keep_looping:
            #print 'extrawidth: %d, extraheight: %d' %(CONSTANTS.EXTRA_WIDTH, CONSTANTS.EXTRA_HEIGHT)
            #print 'loop: entity_index=%d energy: %d' % (self.current_entity_index, self.entities[self.current_entity_index].energy.amount)
            self.input_system.controls()
            e = self.entities[self.current_entity_index]

            if e.energy.can_take_turn or e.energy.gain():
                #print 'needs_input: %s' % ('true' if e.needs_input else 'false')
                if (e.needs_action() and e.needs_input):
                    self.input_system.wait_for_input()

                action = e.get_action()
                # check if action was successful and loop?
                if action.perform():
                    e.energy.spend_turn()
                    e.clear_action()
                    self.current_entity_index = (self.current_entity_index + 1) % len(self.entities)
                else:
                    e.clear_action()
                    pass # we can have failed actions return alternative actions to try again!

            self.renderer.render(self.entities, self.tile_map.tiles)

            pygame.display.flip()
            #clock.tick(60)



