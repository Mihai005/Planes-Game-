from game.service.Service import Service
from game.repository.Table import Table
from game.ui.UI import UI


if __name__ == '__main__':
    tableA = Table()
    tableB = Table()
    service = Service(tableA, tableB)
    ui = UI(service)
