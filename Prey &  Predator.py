__author__ = 'Barry'
"""
Predator-Prey Problem
---------------------
Simulation of natural habitat
* 2 groups of animals interact
* Prey = food source for predators
* Both populations struggle to survive
* Both groups have fixed birthrate – prey usually faster than predators
allowing for growing prey population
* Increasing prey => habitat can support a greater predator population
=> reducing prey over time
* Both populations in cycle of growth & decay
* We get to choose what is represented so simulation is much simplified.
We can adjust birth & death rates and see what happens
* Example based on wolves & moose on island in Lake Superior.
The island is isolated thus represents a fairly closed world
Rules

1. Habitat updates itself in units of time called clock ticks. During
tick each animal gets to do something
2. All animals have opportunity to move into adjacent space if
available. One move p/tick allowed.
3. Both predator & prey can reproduce. Each animal is assigned a
fixed breed time. If the animal is still alive after breed-time
clock ticks it will reproduce. It does so by finding an unoccupied
adjacent space. The offspring is created in this space. The animal's
breed-time is reset to zero. Can breed at most once p/tick.
4. Predators must eat. They have a fixed starve-time. If they cannot
find prey within starve-time clock ticks, they die.
5. Eats by moving to adjacent space containing predator.
Starve-time reset to zero. Eating counts as a move.
6. Each animal's local state updated after each tick.
Simulation using OO Programming
Identify objects and their interactions. Objects that we need:
An island
some prey (the moose)
some predators (the wolves)
methods that govern how they interact with each other and the main
program.
"""