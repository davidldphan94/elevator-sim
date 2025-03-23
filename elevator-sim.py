import time

class Floor:
    num : int
    maintenanceStatus : bool
    
    def __init__(self, floorNum):
        self.num = floorNum
        self.maintenanceStatus = False

    def getFloorNum(self):
        return self.num

    def getMaintenanceStatus(self):
        return self.maintenanceStatus
    
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

class Elevator:
    underMaintenance : bool
    numberOfFloors : int
    currentFloor : int
    floors : dict

    def __init__(self, floors):
        self.numberOfFloors = floors
        self.floors = [Floor(n + 1) for n in range(self.numberOfFloors)]
        self.underMaintenance = False
        self.currentFloor = self.floors[0]
    
    def getFloors(self):
        return self.floors
    
    def getCurrentFloor(self) -> Floor:
        return self.currentFloor
    
    def setCurrentFloor(self, floor):
        self.currentFloor = floor
    
    def finishMaintenance(self):
        print("Maintenance is finished!")
        self.underMaintenance = False

    def startMaintenance(self):
        print("Elevator under maintenance...")
        self.underMaintenance = True

    def callElevator(self, dest):
        if self.underMaintenance:
            print("Elevator currently under maintenance work, please try another elevator.")
        else:
            assert dest < len(self.floors) or dest > 1
            if dest >= self.getCurrentFloor().getFloorNum():
                self.elevatorUp(dest)
            else:
                self.elevatorDown(dest)
            print("Entering Elevator...")
            self.goToFloor()

    def elevatorUp(self, dest):
        print(f"Elevator is now on the way to Floor {dest}...")
        startIndex = self.getFloors().index(self.getCurrentFloor())
        floorsBetween = self.getFloors()[startIndex : startIndex + dest]
        for floor in floorsBetween:
            print(f"Floor {floor.num}")
            self.setCurrentFloor(floor)
            time.sleep(5)

    def elevatorDown(self, dest):
        print(f"Elevator is now on the way to Floor {dest}...")
        startIndex = self.getFloors().index(self.getCurrentFloor())
        floorsBetween = self.getFloors()[dest - 1: startIndex + 1]
        for floor in reversed(floorsBetween):
            print(f"Floor {floor.num}")
            self.setCurrentFloor(floor)
            if self.getCurrentFloor().getFloorNum() == dest:
                break
            time.sleep(5)

  
    def goToFloor(self):
        selectFloor = False
        dest = None
        while not selectFloor:
            try:
                dest = int(input(f"Which floor would you like to go to? Available floors: {[floor for floor in self.getFloors()]} "))
                if dest > len(self.floors) or dest < 1:
                    print("Invalid selection.")
                else:
                    selectFloor = True
            except ValueError:
                print("Invalid selection!")
        if dest >= self.getCurrentFloor().getFloorNum():
            self.elevatorUp(dest)
        else:
            self.elevatorDown(dest)
        print(f"Exiting Elevator at Floor {self.getCurrentFloor().getFloorNum()}...")


# For testing purposes
def main():
    e = Elevator(5)
    e.callElevator(3)
    e.callElevator(4)
    e.callElevator(1)

if __name__ == "__main__":
    main()