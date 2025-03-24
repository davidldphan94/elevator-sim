# elevator-sim
Bluestaq coding challenge

This code simulates an elevator using python code. The readme is written to document some notes on my work.

# Implemented Features
1. Elevator can go up and down given a method.
2. Elevator implements a pseudo-random malfunction because realistically, elevators don't always work.
3. People can go in and out of elevators whenever their floors are reached.
4. Elevator has a maximum weight and occupancy limit.
5. Elevator can go into maintenance mode given any malfunctions.

# Unimplemented Features
1. Does not implement elevator numbers under ground level (no basement functionality).
2. Elevator does not pick up people on the way.
3. Elevator does not distinguish which way it'll go to drop people off most efficiently.

### NOTES I TOOK TO BRAINSTORM ###
1. Elevators should go up and down based on how many floors there are.
2. Elevators have a maximum capacity on people and weight.
3. Elevators should have the floors capped until more floors are built. 
4. Elevators have a button on each floor in order to get it to come to a user.
5. Elevators should have an open or close button for the doors.
6. Elevators should have some sort of emergency contact in case it malfunctions.

Elevator Class:

Attributes:
- Maximum weight
- Maximum capacity on people
- Emergency contact
- Buttons for floors
- Under maintenance or not
- Current floor

Methods:
- Is the door open?
- Can you enter the elevator (i.e. weight or person limit, under maintenance, etc.)
- What floor is it on?

Thoughts:
- I originally had it so that it was single-use only.
- Should it try to accomodate for multiple users who already know where they're going?
- Implement Person, Floor classes to store more information past primitives