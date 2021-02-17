"""
symbols.py - Basic drawn symbols for player pieces. ie, O, and X.
"""
import pygame


def draw_x(surface, rect, color=(30,30,30), offset=None):
    """
    Draws an X/Cross. Does so by drawing two lines in X shape.
    1st line --> Top left, to bottom right.
    2nd line --> Top right, to bottom left.

    Params:
        surface: Pygame surface object.
        rect: Pygame rect object (X, Y, Width, Height)
        color: RGB color of lines in X/Cross (XXX,YYY,ZZZ)
        offset: value used to make it fit inside pygame rect size chosen nicely.
    """
    pygame.draw.line(surface, color,
            (rect[0] + offset,
             rect[1] + offset),
            (rect[0] + rect[2] - offset,
             rect[1] + rect[3] - offset),  5)
    pygame.draw.line(surface, color,
            (rect[0] + rect[2] - offset,
             rect[1] + offset),
            (rect[0] + offset,
             rect[1] + rect[3] - offset),5)



def draw_o(surface, rect=None, CR=None, color=(255, 51, 51), thickness=5):
    """
    Draws the O/Naught. Does so by drawing a circle using pygame draw circle
    method. Cicle can be drawn given either a pygame rect object, or a by
    given a tuple CR=((X,Y)R) given the x,y of the center, and the radius of
    said circle

    Params:
        surface: Pygame surface object.
        rect: Pygame rect object (X, Y, Width, Height) Given rect object points
        CR: A tuple of the circles center (X, Y), and radius R. --> ((X, Y), R)
        to the top left corner of circle if circle was drawn inside of a square.
        Calulates the center and radius of the circle to draw it itself.
        color: RGB color of lines in X/Cross (XXX,YYY,ZZZ)
        thickness: Thickness of the circles line
    center --> rect[0] + rect[2]/2 --> X value + half width,
               rect[1] + rect[3]/2 --> Y value + half height,
    radius --> rect[3]/3 --> Height / 3
    """
    if rect:
        pygame.draw.circle(surface, color,
            (int(rect[0] + rect[2]/2),
            int(rect[1] + rect[3]/2) ),
            int(rect[3]/3), thickness)
    elif CR:
        pygame.draw.circle(surface, color, CR[0][0], CR[0][1]. CR[1])
