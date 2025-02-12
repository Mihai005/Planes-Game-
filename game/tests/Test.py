import unittest
from game.repository.Table import Table
from game.service.Service import Service


class Test(unittest.TestCase):
    def setUp(self):
        self.playerTable = Table()
        self.computerTable = Table()
        self.service = Service(self.playerTable, self.computerTable)

    def test_repository(self):
        self.playerTable.addPlane(('A', 3), 'N')
        assert self.playerTable.getMap[0][2] == 2
        self.playerTable.addPlane(('D', 10), 'E')
        assert self.playerTable.getMap[3][9] == 4
        for i in range(5):
            assert self.playerTable.getMap[1+i][8] == 1
        self.playerTable.addPlane(('J', 5), 'S')
        assert self.playerTable.getMap[9][4] == 3
        assert self.playerTable.getMap[7][4] == 1
        self.computerTable.addPlane(('E', 3), 'W')
        for i in range(3):
            assert self.computerTable.getMap[3+i][5] == 1
        self.playerTable.deleteDeadFromTable(0, 2)
        assert self.playerTable.getMap[0][2] == -1
        assert self.computerTable.isDone() is False
        assert self.computerTable.handleGuess(4, 2) == "Dead"
        assert self.computerTable.handleGuess(8, 2) == "Air"
        assert self.playerTable.handleGuess(2, 6) == "Hit"

    def test_service(self):
        self.service.coordinatesInputValidation('A 3')
        try:
            self.service.coordinatesInputValidation('G ')
            assert False
        except ValueError as v:
            assert v.args[0] == 'Invalid number of arguments'
        try:
            self.service.coordinatesInputValidation('Q 2')
            assert False
        except ValueError as v:
            assert v.args[0] == 'Invalid X coordinate value'
        try:
            self.service.coordinatesInputValidation('B c')
        except ValueError as v:
            assert v.args[0] == 'Invalid Y coordinate type'
        try:
            self.service.coordinatesInputValidation('C 11')
        except ValueError as v:
            assert v.args[0] == 'Invalid Y coordinate value'
        self.service.directionInputValidation('E')
        try:
            self.service.directionInputValidation('A')
        except ValueError as v:
            assert v.args[0] == 'Invalid direction'
        cockpitPosition, direction = self.service.generateAddComputer()
        x, y = cockpitPosition
        assert x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        assert 1 <= y <= 10
        assert direction in ['N', 'S', 'E', 'W']
        self.service.hitHistoryComputer.append([2, 6])
        assert self.service.getChoiceComputer() == (1, 6)
        assert self.service.targetNearbyHits() == (3, 6)
        assert self.service.getNeighbours(5, 5) == [[4, 5], [6, 5], [5, 4], [5, 6]]
        assert self.service.getNeighbours(9, 9) == [[8, 9], [9, 8]]
        assert self.service.convertCoordinates('C', '9') == (2, 8)
        assert self.service.getStarter() == 1 or self.service.getStarter() == 2
        assert self.service.getResult() == "Draw"


if __name__ == '__main__':
    unittest.main()
