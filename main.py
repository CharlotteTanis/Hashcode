def PrepareFile(fp, shape):
    """
    Prepares the CSV file to load the Rush Hour board.
    """

    vehicles = {}
    with open(fp, "rb") as fileRushhour:
        reader_vehicles = csv.reader(fileRushhour, delimiter=',')
        # iterate over each vehicle in the CSV
        for vehicle in reader_vehicles:
            vehicles[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

    return Board(shape, shape, round((shape / 2.) - 1), vehicles)

    board = PrepareFile(fp, shape)


class Board(object):
    """
    Rush Hour board.
    """

    def __init__(self, width, height, y_exit, vehicles):
        """
        Initialize board.
        """

        self.width = width
        self.height = height
        self.y_exit = y_exit
        self.makeBoard(vehicles)

    def printBoard(self):
        """
        Print board.
        """
        # transpose board to print x and y correctly
        board = [[j[i] for j in self.board] for i in range(len(self.board[0]))]

        # print board
        for element in board:
            print " ".join(element)
        print "\n"

    def makeBoard(self, new_vehicles):
        """
        Makes the beginstate of the board.
        """
        self.vehicles = new_vehicles
        self.board = [['_'] * self.height for _ in range(self.width)]

        # iterate over each verhicle in list 'hor_auto'
        for ID, vehicle in new_vehicles.iteritems():
            if vehicle.dir == 'H':
                # set vehicle ID on each position of the vehicle
                for i in range(0, vehicle.size):
                    self.board[vehicle.x - i][vehicle.y] = ID
            if vehicle.dir == 'V':
            # set vehicle ID on each position of the vehicle
                for i in range(0, vehicle.size):
                    self.board[vehicle.x][vehicle.y - i] = ID
