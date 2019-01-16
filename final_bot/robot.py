from battlecode import BCAbstractRobot, SPECS
import battlecode as bc
import random


__pragma__('iconv')
__pragma__('tconv')
#__pragma__('opov')


# don't try to use global variables!!

class MyRobot(BCAbstractRobot):

    round = -1
    initial_pilgrims = 5
    surrounding_tiles = [
        [-1,-1], #Top-Left
        [0,-1],  #Top
        [1,-1],  #Top-Right
        [1,0],   #Right
        [1,1],   #Bottom-Right
        [0,1],   #Bottom
        [-1,1],  #Bottom-Left
        [-1,0]  #Left
    ]

    def turn(self):
        self.round += 1

        passable_map = self.get_passable_map()
        karbonite_map = self.get_karbonite_map()
        visible_map = self.get_visible_robot_map()
        fuel_map = self.get_fuel_map()
        
        if self.me['unit'] == SPECS['CASTLE']:
            if(self.initial_pilgrims>0):
                for dx,dy in self.surrounding_tiles:
                    x = self.me.x+dx
                    y = self.me.y+dy
                    if(passable_map[y][x]==True and visible_map[y][x] == 0):
                        self.log("Created pilgrim.")
                        self.initial_pilgrims -= 1
                        return self.build_unit(SPECS['PILGRIM'],dx,dy)

        if self.me['unit'] == SPECS['PILGRIM']:
            pass

robot = MyRobot()