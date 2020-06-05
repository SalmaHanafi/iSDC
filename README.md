# iSDC
Intro to Self Driving Cars Nano Degree

Histogram filter:
In main.cpp, you'll find a vector called grid. Grid is a char vector holding the color values of a 2-dimensional square grid.

The initialize_beliefs function takes in the char grid and outputs the initial probabilities for each square on the grid.

Then the sense function takes a measurement of the current grid space's color. The measurement is used to update the probabilities of each space on the grid.

Next, the blur function passes the grid through a smoothing algorithm.

Then the probabilities are normalized with the normalize function.

Finally, the robot moves to a new space on the board, and the probabilities are updated appropriately.

Each function is run ten-thousand times. You can adjust the number of times by changing the value in the iterations variable.


daysBetweenDates:  Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
