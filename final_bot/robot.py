from battlecode import BCAbstractRobot, SPECS
import battlecode as bc
import random


__pragma__('iconv')
__pragma__('tconv')
#__pragma__('opov')


# don't try to use global variables!!

class MyRobot(BCAbstractRobot):

    round = -1

    initial_pilgrims = 1
    initial_crusaders = 1
    
    surrounding_tiles = [
        [-1,-1], #Top-Left
        [0,-1],  #Top
        [1,-1],  #Top-Right
        [1,0],   #Right
        [1,1],   #Bottom-Right
        [0,1],   #Bottom
        [-1,1],  #Bottom-Left
        [-1,0]   #Left
    ]

    destination = None

    def turn(self):
        self.round += 1

        passable_map = self.get_passable_map()
        karbonite_map = self.get_karbonite_map()
        visible_map = self.get_visible_robot_map()
        fuel_map = self.get_fuel_map()
        visible_robots = self.get_visible_robots()
        
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
            if self.destination == None:
                self.destination = get_closest_resource(karbonite_map,self.x,self.y)

            if self.me.karbonite == SPECS['UNITS'][SPECS["PILGRIM"]]['KARBONITE_CAPACITY'] and :
                pass
            if(self.x == self.destination[0] and self.y == self.destination[1]):
                self.mine()

    def get_closest_resource(self,map,x,y):
        pass

    def move_to(self,x,y,passable_map,visible_map):
        pass

robot = MyRobot()