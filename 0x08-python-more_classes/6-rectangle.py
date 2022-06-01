#!/usr/bin/python3
"""
Definning a Rectangle class.
"""


class Rectangle:
    """
    Representation of a Rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializing New Rectangle.
        Arguments:
            width:  The width of the new rectangle as an integer.
            height: The height of the new rectangle as an integer.
        Raises:
            TypeError   (Width): Must be an integer.
            ValueError  (Width): must be >= 0.
            TypeError  (Height): Must be an integer.
            ValueError (Height): Must be >= 0.
        Returns:
            Area:      Returns the area.
            Perimeter: Returns the perimeter.
            Grafical:  Returns a graphical string representation using '#'.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Setting the width of the new rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Setting the height of the new rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mst be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the perimeter of the Rectangle.
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        Returns Rectangles graphical representation as strings.
        """
        str = ""
        if self.__width == 0 or self.__height == 0:
            return (str)
        for i in range(0, self.height):
            for j in range(0, self.width):
                str = str + '#'
            str = str + '\n'
        str = str[0:-1]
        return(str)

    def __repr__(self):
        """
        Return the string representation of the Rectangle.
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """
        Prints a deleteion message.
        """
        print("Bye rectangle...")
