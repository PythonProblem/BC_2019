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

    def get_closest_resource(self,map,x,y): #Gives x,y of closest resource
        loc = [x,y]
        closest_loc = (-1, -1)
        best_dist_sq = 64 * 64 + 64 * 64 + 1
        for x in range(len(map)):
            if (x - loc[0])**2 > best_dist_sq:
                continue
            for y in range(len(map[0])):
                if (y - loc[1])**2 > best_dist_sq:
                    continue
                d = (x-loc[0]) ** 2 + (y-loc[1]) **2
                if map[y][x] and d < best_dist_sq:
                    best_dist_sq = d
                    closest_loc = (x,y)
        return closest_loc
     
    def move_to(self,x,y,passable_map,visible_map): #moves "smartly" to [x,y]. Make sure x,y is passable
        return None

    def get_path(self,x,y,passable_map): #returns path to [x,y], tile by tile
        return []

    def is_adjacent(self,r): #Returns true if 'r' object is adjacent to 'self' object
        l = [r.x-self.x,r.y-self.y]
        for i in self.surrounding_tiles:
            if(l == i):
                return True
        return False

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
                self.destination = self.get_closest_resource(karbonite_map,self.x,self.y)
            if self.destination_path == None:
                self.destination_path = self.get_path(*self.destination,passable_map)

            if self.me.karbonite == SPECS['UNITS'][SPECS["PILGRIM"]]['KARBONITE_CAPACITY']:
                for r in visible_robots:
                    if(r.team == self.me.team and r.id == SPECS['CRUSADER'] and self.is_adjacent(r)):
                        return self.give(r.x-self.x,r.y-self.y,self.me.karbonite,0)

            if(self.x == self.destination[0] and self.y == self.destination[1]):
                return self.mine()

        

robot = MyRobot()