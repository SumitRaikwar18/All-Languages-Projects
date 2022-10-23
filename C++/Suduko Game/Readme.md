Sudoku Game Made By Using C++

Program Use
Game can be started by compiling (with makefile) and running sudoku

Default action is to start interactive, 9x9 game

To fill in cell, enter the column number, row number, and value you want to enter (1 based). Separate with spaces, commas, or any other delimiter (besides an integer of course)

At any time, enter "Solve" to have the backtracer solve the game for you based on your current position.

If you've walked yoursel into an impossible configuration you will be prompted to first clear the board

Once solved, you will be asked if you want to play again

Run speed test / alternate game configurations using command flags below

Command line flags can be used to configure the game

-s --seed Set the random seed to replicate results -u --Unittest Runs unit (speed) test with both solvers. Specify number of times to run -g --gamesize Integer value to specify game size ie 9 for 9x9 game, 16 for 16x16 etc. -n --nobs Specify number of pre-filled values to include (ie. immutable Sudoku cells) -v --verbose Add flag with no argument for verbose output after every unit test. No effect if game played in interactive mode

Notes:

Puzzles are always generating using a sort of reverse backtrace (ie. filling in diagonal using random permutation, solving puzzle, and then removing cells). This means that sometimes generating the puzzle takes longer than solving it (especially for big puzzles). The unit test times only the solver function
During the class demo, in the speed test, our first puzzle took an order of magnitude longer to solve for the backtracer than the other 9 puzzles. Upon investigation, it turns out that this was likely because of the constant random seed (there is significant variability in time to solve puzzles for backtracer, the Alternating Projections approach seems to be less variable for given puzzle configuration)
Items to grade:

Game Logic/ Gameplay of the interactive game + command line tools/speed tests
Back-tracking solver (the "solve" function in solve.cpp)
Alternating projection solver (the "DR" function in altproj.cpp)
