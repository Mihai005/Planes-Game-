import random

from game.repository.Table import Table


class Service:
    def __init__(self, tablePlayer: Table, tableComputer: Table):
        self.tablePlayer = tablePlayer
        self.tableComputer = tableComputer
        self.choiceHistoryComputer = []
        self.hitHistoryComputer = []
        self.defaultHistoryComputer()

    def defaultHistoryComputer(self):
        """
        This function eliminates impossible cockpit coordinates from the possible guesses of the Computer
        :return: None
        """
        self.choiceHistoryComputer.append(['A', 1])
        self.choiceHistoryComputer.append(['A', 2])
        self.choiceHistoryComputer.append(['A', 9])
        self.choiceHistoryComputer.append(['A', 10])
        self.choiceHistoryComputer.append(['B', 1])
        self.choiceHistoryComputer.append(['B', 2])
        self.choiceHistoryComputer.append(['B', 9])
        self.choiceHistoryComputer.append(['B', 10])
        self.choiceHistoryComputer.append(['I', 1])
        self.choiceHistoryComputer.append(['I', 2])
        self.choiceHistoryComputer.append(['I', 9])
        self.choiceHistoryComputer.append(['I', 10])
        self.choiceHistoryComputer.append(['J', 1])
        self.choiceHistoryComputer.append(['J', 2])
        self.choiceHistoryComputer.append(['J', 9])
        self.choiceHistoryComputer.append(['J', 10])

    @staticmethod
    def coordinatesInputValidation(userInput: str):
        """
        This function validates the coordinates for adding a Plane
        :param userInput: coordinateX of cockpit, coordinateY of cockpit
        :return: None
        :raises ValueError: if invalid coordinates
        """
        if len(userInput) < 3:
            raise ValueError("Invalid number of arguments")
        coordinateX = userInput[0:1]
        coordinateY = userInput[1:]
        if coordinateX not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            raise ValueError("Invalid X coordinate value")
        try:
            int(coordinateY)
        except ValueError:
            raise ValueError("Invalid Y coordinate type")
        if not 1 <= int(coordinateY) <= 10:
            raise ValueError("Invalid Y coordinate value")
        return coordinateX, coordinateY

    @staticmethod
    def directionInputValidation(direction: str):
        """
        This function validates the direction for adding a Plane
        :param direction: user desired direction
        :return: None
        :raises ValueError: if invalid direction
        """
        if direction != 'N' and direction != 'S' and direction != 'W' and direction != 'E':
            raise ValueError("Invalid direction")
        return direction

    @staticmethod
    def addPlane(table: Table, cockpitPosition, direction):
        """
        This function adds a Plane to Player/Computer Table
        :param table: Player / Computer Table
        :param cockpitPosition: (coordinateX of cockpit, coordinateY of cockpit)
        :param direction: N/S/E/W
        :return: None
        """
        table.addPlane(cockpitPosition, direction)

    @staticmethod
    def generateAddComputer():
        """
        This function generates a possible Plane for the Computer's Table
        :return:
        """
        cockpitPositionX = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
        cockpitPositionY = random.randint(1, 10)
        cockpitPosition = (cockpitPositionX, cockpitPositionY)
        direction = random.choice(["N", "S", "W", "E"])
        return cockpitPosition, direction

    def handleGuessPlayer(self, guess: str):
        """
        This function handles the Player's guess functionality
        :param guess: coordinates of the user's guess
        :return: Air, Hit or Dead
        """
        coordinateX, coordinateY = self.getChoicePlayer(guess)
        result = self.tableComputer.handleGuess(coordinateX, coordinateY)
        match result:
            case "Air":
                return "Air"
            case "Hit":
                return "Hit"
            case "Dead":
                self.tableComputer.deleteDeadFromTable(coordinateX, coordinateY)
                return "Dead"

    def handleGuessComputer(self):
        """
        This function handles the Computer's guess functionality
        :return: Air, Hit or Dead
        """
        coordinateX, coordinateY = self.getChoiceComputer()
        result = self.tablePlayer.handleGuess(coordinateX, coordinateY)
        match result:
            case "Air":
                return "Air"
            case "Hit":
                self.hitHistoryComputer.append([coordinateX, coordinateY])
                return "Hit"
            case "Dead":
                self.tablePlayer.deleteDeadFromTable(coordinateX, coordinateY)
                return "Dead"

    def getChoicePlayer(self, guess):
        """
        This function validates the guess and converts it from String to Integers
        :param guess: user's guess
        :return: coordinateX, coordinateY as Integers
        """
        coordinateX, coordinateY = self.coordinatesInputValidation(guess)
        return self.convertCoordinates(coordinateX, coordinateY)

    def getChoiceComputer(self):
        """
        This function generates a guess by the Computer
        :return: coordinateX, coordinateY of the choice
        """
        if self.hitHistoryComputer:
            return self.targetNearbyHits()
        while True:
            coordinateX = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
            coordinateY = random.randint(1, 10)
            if not self.choiceHistoryComputer.__contains__([coordinateX, coordinateY]):
                self.choiceHistoryComputer.append([coordinateX, coordinateY])
                break
        return self.convertCoordinates(coordinateX, coordinateY)

    def targetNearbyHits(self):
        """
        This function optimizes the Computer's choice so that it searches for the cockpit near the hit targets
        :return: coordinateX, coordinateY of the guess
        """
        for hit in self.hitHistoryComputer:
            x, y = hit
            possibleTargets = self.getNeighbours(x, y)
            for target in possibleTargets:
                X, Y = target
                if not self.choiceHistoryComputer.__contains__([X, Y]):
                    self.choiceHistoryComputer.append([X, Y])
                    return X, Y
        self.hitHistoryComputer = []
        return self.getChoiceComputer()

    @staticmethod
    def getNeighbours(x, y):
        """
        This function gets the neighbours of a given (x,y) point
        :param x: coordinateX
        :param y: coordinateY
        :return: the neighbours of (x,y) that are within the Table
        """
        neighbours = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        return [[x, y] for x, y in neighbours if 0 <= x <= 9 and 0 <= y <= 9]

    @staticmethod
    def convertCoordinates(x, y):
        """
        This function converts the coordinates from Strings to Integers
        :param x: coordinateX
        :param y: coordinateY
        :return: (x,y) as a pair of Integers
        """
        return ord(x) - ord('A'), int(y) - 1

    @staticmethod
    def getStarter():
        """
        This function randomizes the starter of the game
        :return: 1 or 2, 1 - Player, 2 - Computer
        """
        return random.randint(1, 2)

    def getResult(self):
        """
        This function checks whether the game is done
        :return: the winner or draw or 0 for continuation of the game
        """
        donePlayer = self.tableComputer.isDone()
        doneComputer = self.tablePlayer.isDone()
        if donePlayer and not doneComputer:
            return "Player won"
        elif donePlayer and doneComputer:
            return "Draw"
        elif not donePlayer and doneComputer:
            return "Computer won"
        else:
            return 0

    @property
    def getTablePlayer(self):
        return self.tablePlayer

    @property
    def getTableComputer(self):
        return self.tableComputer
