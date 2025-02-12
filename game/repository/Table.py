class Table:
    def __init__(self):
        self.map = [[0 for _ in range(10)] for _ in range(10)]

    def addPlane(self, cockpitPosition: tuple, direction: str):
        """
        This functions adds a Plane on the Table
        :param cockpitPosition: (coordinateX of cockpit, coordinateY of cockpit)
        :param direction: N/S/E/W
        :return: None
        """
        cockpitCoordinateX, cockpitCoordinateY = cockpitPosition
        cockpitCoordinateX = ord(cockpitCoordinateX) - ord('A')
        cockpitCoordinateY = int(cockpitCoordinateY) - 1
        match direction:
            case 'N':
                self.addPlaneFacingNorth(cockpitCoordinateX, cockpitCoordinateY)
            case 'S':
                self.addPlaneFacingSouth(cockpitCoordinateX, cockpitCoordinateY)
            case 'E':
                self.addPlaneFacingEast(cockpitCoordinateX, cockpitCoordinateY)
            case 'W':
                self.addPlaneFacingWest(cockpitCoordinateX, cockpitCoordinateY)

    def addPlaneFacingNorth(self, cockpitCoordinateX, cockpitCoordinateY):
        """
        This plane adds a Plane facing North
        :param cockpitCoordinateX: coordinateX of cockpit
        :param cockpitCoordinateY: coordinateY of cockpit
        :return: None
        :raises ValueError: if the resulting plane does not fit within the Table
        """
        frontWingsCoordinateX = cockpitCoordinateX + 1
        frontLeftWingY = cockpitCoordinateY - 2
        frontRightWingY = cockpitCoordinateY + 2
        bodyCoordinateX = cockpitCoordinateX + 2
        bodyCoordinateY = cockpitCoordinateY
        rearWingsCoordinateX = cockpitCoordinateX + 3
        rearLeftWingY = cockpitCoordinateY - 1
        rearRightWingY = cockpitCoordinateY + 1

        if frontLeftWingY < 0 or frontRightWingY > 9 or rearWingsCoordinateX > 9:
            raise ValueError("Invalid position")

        self.drawPlaneOnMap('NS', cockpitCoordinateX, cockpitCoordinateY, 2, frontLeftWingY, frontRightWingY,
                            frontWingsCoordinateX, bodyCoordinateX, bodyCoordinateY, rearLeftWingY, rearRightWingY,
                            rearWingsCoordinateX)

    def addPlaneFacingSouth(self, cockpitCoordinateX, cockpitCoordinateY):
        """
        This plane adds a Plane facing South
        :param cockpitCoordinateX: coordinateX of cockpit
        :param cockpitCoordinateY: coordinateY of cockpit
        :return: None
        :raises ValueError: if the resulting plane does not fit within the Table
        """
        frontWingsCoordinateX = cockpitCoordinateX - 1
        frontLeftWingY = cockpitCoordinateY + 2
        frontRightWingY = cockpitCoordinateY - 2
        bodyCoordinateX = cockpitCoordinateX - 2
        bodyCoordinateY = cockpitCoordinateY
        rearWingsCoordinateX = cockpitCoordinateX - 3
        rearLeftWingY = cockpitCoordinateY + 1
        rearRightWingY = cockpitCoordinateY - 1

        if frontLeftWingY > 9 or frontRightWingY < 0 or rearWingsCoordinateX < 0:
            raise ValueError("Invalid position")

        self.drawPlaneOnMap('NS', cockpitCoordinateX, cockpitCoordinateY, 3, frontRightWingY, frontLeftWingY,
                            frontWingsCoordinateX, bodyCoordinateX, bodyCoordinateY, rearRightWingY, rearLeftWingY,
                            rearWingsCoordinateX)

    def addPlaneFacingEast(self, cockpitCoordinateX, cockpitCoordinateY):
        """
        This plane adds a Plane facing East
        :param cockpitCoordinateX: coordinateX of cockpit
        :param cockpitCoordinateY: coordinateY of cockpit
        :return: None
        :raises ValueError: if the resulting plane does not fit within the Table
        """
        frontWingsCoordinateY = cockpitCoordinateY - 1
        frontLeftWingX = cockpitCoordinateX - 2
        frontRightWingX = cockpitCoordinateX + 2
        bodyCoordinateX = cockpitCoordinateX
        bodyCoordinateY = cockpitCoordinateY - 2
        rearWingsCoordinateY = cockpitCoordinateY - 3
        rearLeftWingX = cockpitCoordinateX - 1
        rearRightWingX = cockpitCoordinateX + 1

        if frontLeftWingX < 0 or frontRightWingX > 9 or rearWingsCoordinateY < 0:
            raise ValueError("Invalid position")

        self.drawPlaneOnMap('EW', cockpitCoordinateX, cockpitCoordinateY, 4, frontLeftWingX, frontRightWingX,
                            frontWingsCoordinateY, bodyCoordinateX, bodyCoordinateY, rearLeftWingX, rearRightWingX,
                            rearWingsCoordinateY)

    def addPlaneFacingWest(self, cockpitCoordinateX, cockpitCoordinateY):
        """
        This plane adds a Plane facing West
        :param cockpitCoordinateX: coordinateX of cockpit
        :param cockpitCoordinateY: coordinateY of cockpit
        :return: None
        :raises ValueError: if the resulting plane does not fit within the Table
        """
        frontWingsCoordinateY = cockpitCoordinateY + 1
        frontLeftWingX = cockpitCoordinateX + 2
        frontRightWingX = cockpitCoordinateX - 2
        bodyCoordinateX = cockpitCoordinateX
        bodyCoordinateY = cockpitCoordinateY + 2
        rearWingsCoordinateY = cockpitCoordinateY + 3
        rearLeftWingX = cockpitCoordinateX + 1
        rearRightWingX = cockpitCoordinateX - 1

        if frontRightWingX < 0 or frontLeftWingX > 9 or rearWingsCoordinateY > 9:
            raise ValueError("Invalid position")

        self.drawPlaneOnMap('EW', cockpitCoordinateX, cockpitCoordinateY, 5, frontRightWingX, frontLeftWingX,
                            frontWingsCoordinateY, bodyCoordinateX, bodyCoordinateY, rearRightWingX, rearLeftWingX,
                            rearWingsCoordinateY)

    def drawPlaneOnMap(self, mode, cockpitA, cockpitB, valueCockpit, frontA, frontB, frontC, bodyA, bodyB, rearA, rearB,
                       rearC):
        """
        This plane draws a Plane on the Table
        :param mode: NS / EW (to check whether we draw horizontally or vertically)
        :param cockpitA: coordinateX of cockpit
        :param cockpitB: coordinateY of cockpit
        :param valueCockpit: this parameter sets the orientation of the plane (N/S/W/E)
        :param frontA: minimal range bound for front wings
        :param frontB: the row/column of the front wings (the coordinate that doesn't change)
        :param frontC: maximal range bound for front wings
        :param bodyA: coordinateX of body
        :param bodyB: coordinateY of body
        :param rearA: minimal range bound for rear wings
        :param rearB: the row/column of the rear wings (the coordinate that doesn't change)
        :param rearC: maximal range bound for rear wings
        :return: None
        :raises ValueError: if it overlaps with another already existing Plane
        """
        if self.map[cockpitA][cockpitB] != 0:
            raise ValueError("Already existing plane overlaps with cockpit of the new plane")
        for i in range(frontA, frontB + 1):
            if mode == 'NS':
                if self.map[frontC][i] != 0:
                    raise ValueError("Already existing plane overlaps with front wings of the new plane")
            else:
                if self.map[i][frontC] != 0:
                    raise ValueError("Already existing plane overlaps with front wings of the new plane")
        if self.map[bodyA][bodyB] != 0:
            raise ValueError("Already existing plane overlaps with body of the new plane")
        for i in range(rearA, rearB + 1):
            if mode == 'NS':
                if self.map[rearC][i] != 0:
                    raise ValueError("Already existing plane overlaps with rear wings of the new plane")
            else:
                if self.map[i][rearC] != 0:
                    raise ValueError("Already existing plane overlaps with rear wings of the new plane")

        self.map[cockpitA][cockpitB] = valueCockpit
        for i in range(frontA, frontB + 1):
            if mode == 'NS':
                self.map[frontC][i] = 1
            else:
                self.map[i][frontC] = 1
        self.map[bodyA][bodyB] = 1
        for i in range(rearA, rearB + 1):
            if mode == 'NS':
                self.map[rearC][i] = 1
            else:
                self.map[i][rearC] = 1

    def deleteDeadFromTable(self, x, y):
        """
        This function removes the Dead Plane from the Table
        :param x: coordinate X
        :param y: coordinate Y
        :return: None
        """
        cockpit = self.map[x][y]
        match cockpit:
            case 2:
                self.map[x][y] = -1
                for i in range(5):
                    self.map[x+1][y-2+i] = -1
                self.map[x+2][y] = -1
                for i in range(3):
                    self.map[x+3][y-1+i] = -1
            case 3:
                self.map[x][y] = -1
                for i in range(5):
                    self.map[x-1][y-2+i] = -1
                self.map[x-2][y] = -1
                for i in range(3):
                    self.map[x-3][y-1+i] = -1
            case 4:
                self.map[x][y] = -1
                for i in range(5):
                    self.map[x-2+i][y-1] = -1
                self.map[x][y-2] = -1
                for i in range(3):
                    self.map[x-i+1][y-3] = -1
            case 5:
                self.map[x][y] = -1
                for i in range(5):
                    self.map[x-2+i][y+1] = -1
                self.map[x][y+2] = -1
                for i in range(3):
                    self.map[x-i+1][y+3] = -1

    def handleGuess(self, x, y):
        """
        This function checks the guess of the Player/Computer
        :param x: coordinate X
        :param y: coordinate Y
        :return: Hit, Dead or Air
        """
        if self.map[x][y] == 1:
            return "Hit"
        elif self.map[x][y] > 1:
            return "Dead"
        else:
            return "Air"

    def isDone(self):
        """
        This function checks whether all the Planes on the Table are Dead
        :return: True or False
        """
        return not any(any(value > 0 for value in row) for row in self.map)

    @property
    def getMap(self):
        return self.map
