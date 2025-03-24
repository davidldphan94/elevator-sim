import time
import random

# Floor class
class Floor:
    num : int
    peopleAtFloor : list
    maintenanceStatus : bool
    
    """
    Constructor for the Floor class. Takes in a floor number and the people currently waiting at each floor.

    @args floorNum: the floor number
          people: the people currently waiting at the floor
    """
    def __init__(self, floorNum, people):
        self.num = floorNum
        self.peopleAtFloor = people
        self.maintenanceStatus = False

    """
    getFloorNum

    Returns the floor number

    @args None
    @return The floor number
    """
    def getFloorNum(self) -> int:
        return self.num
    
    """
    getMaintenanceStatus

    Returns the maintenance status

    @args None
    @return The maintenance status
    """
    def getMaintenanceStatus(self) -> bool:
        return self.maintenanceStatus
    
    """
    setMaintenanceStatus

    Sets the maintenance status

    @args status: a boolean that will update the maintenance status
    @return None
    """
    def setMaintenanceStatus(self, status):
        self.maintenanceStatus = status

    def __str__(self):
        return f"Floor {self.num}"
    
    def __repr__(self):
        return f"Floor {self.num}"
    
    def __eq__(self, other):
        return self.num == other.num
    
    def __lt__(self, other):
        return self.num < other.num
    
    def __gt__(self, other):
        return self.num > other.num
    
    def __hash__(self):
        return hash(self.num)

# Person
class Person:
    destination : Floor
    weight : float

    """
    Constructor for the person class. Takes in a floor destination and a weight.

    @args dest: an int that represents which floor the person wants to go to
          weight: the weight of the individual and whatever they might be carrying
    """
    def __init__(self, dest, weight):
        self.destination = dest
        self.weight = weight
    
    def __str__(self):
        return f"(Person going to {self.destination}; Total Weight: {self.weight} lbs)"
    
    def __repr__(self):
        return f"(Person going to {self.destination}; Total Weight: {self.weight} lbs)"
    
    def __eq__(self, other):
        return self.destination == other.destination
    
    def __lt__(self, other):
        return self.destination < other.destination
    
    def __gt__(self, other):
        return self.destination > other.destination
    
    def __hash__(self):
        return hash(self.destination)

# Elevator
class Elevator:
    underMaintenance : bool
    currentFloor : int
    currentOccupancy : list
    currentWeight : float
    maximumOccupancy : int
    maximumWeight : float
    numberOfFloors : int
    floors : list

    """
    Constructor for the elevator class. Takes in a number of floors, an occupancy limit, and a weight limit.

    @args floors : an integer representing how many floors this elevator can go to within this building
          occupancyLimit : an integer capping how many people can enter an elevator at a time
          weightLimit : a float capping how much weight can enter an elevator at a time
    @return None 
    """
    def __init__(self, floors, occupancyLimit = 10, weightLimit = 2000.0):
        self.numberOfFloors = floors
        self.floors = [Floor(num + 1, []) for num in range(floors)]
        self.currentFloor = self.floors[0]
        self.currentOccupancy = []
        self.currentWeight = 0.0
        self.underMaintenance = False
        self.maximumOccupancy = occupancyLimit
        self.maximumWeight = weightLimit
    
    """
    getFloors

    Returns a list of all floors provided.

    @args: None
    @return: A List of all the floors this elevator can go to.
    """
    def getFloors(self) -> list[Floor]:
        return self.floors
    
    """
    getCurrentFloor

    Gets the currentFloor that the elevator is on.

    @args: None
    @return: The floor the elevator is currently located in.
    """
    def getCurrentFloor(self) -> Floor:
        return self.currentFloor
    
    """
    setCurrentFloor

    Sets the currentFloor to the floor passed in as an argument.

    @args: floor : Floor to be set to the current floor
    @return: None
    """
    def setCurrentFloor(self, floor) -> None:
        self.currentFloor = floor
    
    """
    finishMaintenance

    Finishes maintenance on the elevator.

    @args: None
    @return: None
    """
    def finishMaintenance(self) -> None:
        print("Maintenance is finished!")
        self.underMaintenance = False

    """
    startMaintenance

    Starts maintenance on the elevator.

    @args: None
    @return: None
    """
    def startMaintenance(self) -> None:
        print("Elevator under maintenance...")
        self.underMaintenance = True

    """
    callElevator

    Calls the elevator to that floor. May or may not work if maintenance work is needed to be done on it.

    @args: floorToGo: the floor number that triggered the elevator to come to it
           people: the people wanting to board at this floor
    @return: None
    """
    def callElevator(self, floorToGo : int, people : list):
        if self.underMaintenance:
            print("Elevator currently under maintenance work, please try another elevator.")
            return
        print(f"Elevator called at Floor {floorToGo}")
        success = self.elevatorMoving(self.getCurrentFloor().getFloorNum(), floorToGo)
        if not success:
            return
        print("Entering Elevator...")
        peopleBoarding = sorted([person for person in self.boardPeople(people)], key = lambda p: self.getCurrentFloor().getFloorNum() - p.destination)
        print(f"Boarding {peopleBoarding} ; Total Weight: {self.currentWeight}")
        floorsToGo = []
        for person in peopleBoarding:
            if person.destination not in floorsToGo:
                floorsToGo.append(person.destination)
        floorsUnderMaintenance = [floor.getFloorNum() for floor in self.getFloors() if floor.getMaintenanceStatus()]
        for floor in floorsToGo:
            if floor in floorsUnderMaintenance:
                print("Floor under maintenance, please select another floor.")
                continue
            else:
                self.goToFloor(floor)

    """
    boardPeople

    Board people on the elevator. Will not be able to board everyone if occupancy or weight limits would be exceeded.

    @args: people: a list of people trying to board the elevator
    @return: None
    """
    def boardPeople(self, people : list) -> list[Person]:
        peopleToBoard = [] if len(self.currentOccupancy) + len(people) > self.maximumOccupancy or sum([p.weight for p in people]) > self.maximumWeight else people
        doneIterating = False
        while peopleToBoard == [] and not doneIterating:
            try:
                readyToBoard = False
                while not readyToBoard:
                    spaceLeft = self.maximumOccupancy - len(self.currentOccupancy)
                    weightLeft = self.maximumWeight - self.currentWeight
                    numPeopleToBoard = int(
                        input(f"Maximum occupancy is {self.maximumOccupancy} and "
                              f"maximum weight is {self.maximumWeight}, "
                              f"how many would like to come along? (Space left: {spaceLeft}; Weight left: {weightLeft}) "))
                    if numPeopleToBoard > len(people) or numPeopleToBoard < 0 or numPeopleToBoard > self.maximumOccupancy:
                        print("Invalid number, try again.")
                    else:
                        readyToBoard = True
                if numPeopleToBoard == 0:
                    print("No one is boarding.")
                    break
                totalWeight = self.currentWeight
                for i, person in enumerate(people):
                    if len(peopleToBoard) == numPeopleToBoard or totalWeight == self.maximumWeight:
                        print("Limit reached, boarding now.")
                        break
                    else:
                        personInput = None
                        while personInput != "y" and personInput != "n":
                            personInput = input(f"Person {i}, would you like to come along (y/n)? (Space left: {numPeopleToBoard - len(peopleToBoard)}) ")
                            if personInput != "y" and personInput != "n":
                                print("Please answer y or n.")
                            else:
                                if personInput == "y":
                                    if person.weight + totalWeight > self.maximumWeight:
                                        print("Weight would be at maximum limit, please wait for another elevator.")
                                    else:
                                        peopleToBoard.append(person)
                                        totalWeight += person.weight
                                break
                doneIterating = True
            except ValueError:
                print("Invalid number, try again.")
        self.currentOccupancy += peopleToBoard
        self.currentWeight += sum([p.weight for p in peopleToBoard]) 
        return peopleToBoard
    
    """
    elevatorMoving

    Moves between the floors within the list indicated by the two indices: a and b. Returns true if moving was successful and false if a problem occurred.

    @args: a : starting index
           b : ending index
    @return: bool
    """
    def elevatorMoving(self, a : int, b : int) -> bool:
        
        assert a < len(self.floors) or b > 1
        if a < b: #going up
            start, end = a - 1, b
            floorsBetween = self.getFloors()[start: end]
        else: #going down
            start, end = b - 1, a
            floorsBetween = reversed(self.getFloors()[start: end])
        for floor in floorsBetween:
            print(f"{floor}... People Boarded: {self.currentOccupancy} ; Total Weight: {self.currentWeight}")
            self.setCurrentFloor(floor)
            peopleLeaving = [person for person in self.currentOccupancy if person.destination == self.getCurrentFloor().getFloorNum()]
            if random.randint(0, 100) == 13: # life happens
                print("Elevator stopped working... call for help!")
                self.sendHelp()
                return False
            elif len(peopleLeaving) > 0:
                print(f"{peopleLeaving} now exiting at Floor {self.getCurrentFloor().getFloorNum()}...")
                self.currentOccupancy = [p for p in self.currentOccupancy if p not in peopleLeaving]
                self.currentWeight -= sum([p.weight for p in peopleLeaving])
            time.sleep(3)
        return True
  
    """
    goToFloor

    Moves the floor to to the destination

    @args: dest : the floor number to go to
    @return: None
    """
    def goToFloor(self, dest : int):
        success = self.elevatorMoving(self.getFloors().index(self.getCurrentFloor()), dest)
        if not success and self.currentOccupancy == [] and self.underMaintenance():
            return
    
    """
    sendHelp

    Calls emergency services to evacuate people currently in the elevator and then starts maintenance on it.

    @args: None
    @return: None
    """
    def sendHelp(self):
        print("Emergency services coming...")
        time.sleep(10)
        if self.currentOccupancy != []:
            print("Emergency services arrived!")
            print(f"{[person for person in self.currentOccupancy]} now exiting at Floor {self.getCurrentFloor().getFloorNum()}...")
        self.currentOccupancy = []
        self.currentWeight = 0
        self.startMaintenance()

def generateFloorClickedAndPeopleWaiting(elevator):
    floorClicked = random.randint(1, len(elevator.getFloors()))
    people = [Person(random.randint(1, len(elevator.getFloors())), 150) for _ in range(10)]
    return floorClicked, people

def main():
    e1 = Elevator(10, 20, 2000000)
    for _ in range(3):
        floorClicked, people = generateFloorClickedAndPeopleWaiting(e1)
        e1.callElevator(floorClicked, people)

if __name__ == "__main__":
    main()