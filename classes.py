import pygame

class Brick():
    List = []

    def __init__(self, x, y, width, height):
        Brick.List.append(self)
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        
    def destroy(self):
        Brick.List.remove(self)
        del self

class Plate():

    def __init__(self, x, y, width, height):
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        self.velx = 0

    def move(self, SCREENWIDTH, SCREENHEIGHT):

        predicted_location = self.posx + self.velx

        if predicted_location + self.width > SCREENWIDTH:
            self.velx = 0
        elif predicted_location < 0:
            self.velx = 0

        self.posx += self.velx

class Ball():

    def __init__(self, x, y, radius):
        self.posx = x
        self.posy = y
        self.radius = radius
        self.launch = False
        self.velx = 0
        self.vely = 0
        self.game_over = False

    def move(self, plate, SCREENWIDTH, SCREENHEIGHT):

        if not self.launch:
            self.velx = plate.velx
            self.vely = 0

        # bouncing
            
        predicted_location_x = self.posx + self.velx
        predicted_location_y = self.posy + self.vely

        if predicted_location_x + self.radius > SCREENWIDTH \
           or predicted_location_x - self.radius < 0:
            self.velx = -self.velx

        if predicted_location_y + self.radius > SCREENHEIGHT:
            self.vely = -self.vely
            self.game_over = True
            
        if predicted_location_y - self.radius < 0:
            self.vely = -self.vely

        if predicted_location_y + self.radius > plate.posy \
           and predicted_location_y - self.radius < plate.posy:
            if predicted_location_x >= plate.posx \
              and predicted_location_x <= plate.posx + plate.width:
                self.vely = -self.vely
                

        if predicted_location_y > plate.posy \
            and predicted_location_y < plate.posy:
            if (predicted_location_x - self.radius <= plate.posx \
                and predicted_location_x + self.radius >= plate.posx) \
                or (predicted_location_x + self.radius >= plate.posx + plate.width  \
                and predicted_location_x - self.radius <= plate.posx + plate.width):
                self.vely = -self.vely
                self.velx = -self.velx

        if (predicted_location_x < plate.posx and predicted_location_y < plate.posy):
                if predicted_location_x + self.radius > plate.posx and predicted_location_y + self.radius > plate.posy:
                    temp = self.velx
                    self.velx = -self.vely
                    self.vely = -temp

        elif (predicted_location_x > plate.posx + plate.width and predicted_location_y < plate.posy):
                if predicted_location_x - self.radius < plate.posx + plate.width and predicted_location_y + self.radius > plate.posy:
                    temp = self.velx
                    self.velx = self.vely
                    self.vely = temp
        
        for brick in Brick.List:

            # bottom

            if predicted_location_y + self.radius > brick.posy \
               and predicted_location_y - self.radius < brick.posy:
                if predicted_location_x >= brick.posx \
                  and predicted_location_x <= brick.posx + brick.width:
                    self.vely = -self.vely
                    brick.destroy()
                    break

            # top

            elif predicted_location_y - self.radius < brick.posy + brick.height \
                 and predicted_location_y + self.radius > brick.posy + brick.height:
                if predicted_location_x >= brick.posx \
                  and predicted_location_x <= brick.posx + brick.width:
                    self.vely = -self.vely
                    brick.destroy()
                    break
                
            # sides
            
            elif predicted_location_y > brick.posy \
               and predicted_location_y < brick.posy + brick.height:
                if (predicted_location_x - self.radius <= brick.posx \
                  and predicted_location_x + self.radius >= brick.posx) \
                  or (predicted_location_x + self.radius >= brick.posx + brick.width  \
                  and predicted_location_x - self.radius <= brick.posx + brick.width):
                    self.velx = -self.velx
                    brick.destroy()
                    break
                
            # corners
            
            elif (predicted_location_x > brick.posx + brick.width and predicted_location_y > brick.posy + brick.height):
                if predicted_location_x - self.radius < brick.posx + brick.width and predicted_location_y - self.radius < brick.posy + brick.height:
                    temp = self.velx
                    self.velx = -self.vely
                    self.vely = -temp
                    brick.destroy()
                    break
                
            elif (predicted_location_x < brick.posx and predicted_location_y < brick.posy):
                if predicted_location_x + self.radius > brick.posx and predicted_location_y + self.radius > brick.posy:
                    temp = self.velx
                    self.velx = -self.vely
                    self.vely = -temp
                    brick.destroy()
                    break
                
            elif (predicted_location_x < brick.posx and predicted_location_y > brick.posy + brick.height):
                if predicted_location_x + self.radius < brick.posx and predicted_location_y - self.radius < brick.posy + brick.height:
                    temp = self.velx
                    self.velx = self.vely
                    self.vely = temp
                    brick.destroy()
                    break
                
            elif (predicted_location_x > brick.posx + brick.width and predicted_location_y < brick.posy):
                if predicted_location_x - self.radius < brick.posx + brick.width and predicted_location_y + self.radius > brick.posy:
                    temp = self.velx
                    self.velx = self.vely
                    self.vely = temp
                    brick.destroy()
                    break
                
        # moving
              
        self.posx += self.velx
        self.posy += self.vely
        
        
