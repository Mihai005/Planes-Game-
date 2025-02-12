from game.service.Service import Service


class UI:
    def __init__(self, service: Service):
        self.service = service
        self.run()

    def addPlanePlayer(self):
        print("\n(CockpitX, CockpitY)")
        cockpitPosition = input("Enter coordinates: ")
        direction = input("Direction: ")
        cockpitX, cockpitY = self.service.coordinatesInputValidation(cockpitPosition)
        direction = self.service.directionInputValidation(direction)
        cockpitPos = (cockpitX, cockpitY)
        self.service.addPlane(self.service.getTablePlayer, cockpitPos, direction)

    def addPlaneComputer(self):
        cockpitPosition, direction = self.service.generateAddComputer()
        self.service.addPlane(self.service.getTableComputer, cockpitPosition, direction)

    def drawPlanesPlayerA(self):
        i = 0
        while i < 3:
            while True:
                try:
                    self.addPlanePlayer()
                    break
                except ValueError as v:
                    print(v)
            i += 1
            self.printMapOfPlanes(self.service.getTablePlayer.getMap)

    def drawPlanesPlayerB(self):
        i = 0
        while i < 3:
            while True:
                try:
                    self.addPlaneComputer()
                    break
                except ValueError:
                    pass
            i += 1

    def startGame(self):
        print("Game board for Player: ")
        self.printMapOfPlanes(self.service.getTablePlayer.getMap)
        self.drawPlanesPlayerA()
        self.drawPlanesPlayerB()
        # self.printMapOfPlanes(self.service.getTableComputer.getMap)
        self.play()

    @staticmethod
    def takeGuessPlayer():
        print("\nPlayer's turn:\npositionX positionY")
        return input("Guess: ")

    def playWithStarterPlayer(self):
        result = 0
        while result == 0:
            while True:
                try:
                    moveA = self.service.handleGuessPlayer(self.takeGuessPlayer())
                    print(f"Player move result: {moveA}")
                    break
                except ValueError as v:
                    print(v)
            moveB = self.service.handleGuessComputer()
            print(f"Computer move result: {moveB}")

            result = self.service.getResult()
            self.printMapOfPlanes(self.service.getTablePlayer.getMap)
            # self.printMapOfPlanes(self.service.getTableComputer.getMap)
        return result

    def playWithStarterComputer(self):
        result = 0
        while result == 0:
            moveB = self.service.handleGuessComputer()
            print(f"Computer move result: {moveB}")
            while True:
                try:
                    moveA = self.service.handleGuessPlayer(self.takeGuessPlayer())
                    print(f"Player move result: {moveA}")
                    break
                except ValueError as v:
                    print(v)

            result = self.service.getResult()
            self.printMapOfPlanes(self.service.getTablePlayer.getMap)
            # self.printMapOfPlanes(self.service.getTableComputer.getMap)
        return result

    def play(self):
        starter = self.service.getStarter()
        result = 0
        match starter:
            case 1:
                print("\nPlayer starts")
                result = self.playWithStarterPlayer()
            case 2:
                print("\nComputer starts")
                result = self.playWithStarterComputer()
        print(result)

    @staticmethod
    def printMapOfPlanes(planes: list):
        print("   " + " ".join([str(i) for i in range(1, 11)]))
        for i, row in enumerate(planes, start=0):
            colored_row = " ".join(
                f"\033[31m{"x"}\033[0m" if val == -1 else
                f"\033[34m{"#"}\033[0m" if val == 1 else f"\033[34m{"↑"}\033[0m" if val == 2 else f"\033[34m{"↓"}\033"
                f"[0m"f"" if val == 3 else f"\033[34m{"→"}\033[0m" if val == 4 else f"\033[34m{"←"}\033[0m" if val == 5
                else "." for val in row
            )
            print(f"{chr(ord('A') + i)}  {colored_row}")

    def run(self):
        self.startGame()
