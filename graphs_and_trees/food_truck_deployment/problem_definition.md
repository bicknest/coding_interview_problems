# Problem Definition
A dominant food truck company is looking to expand to a new city. The city is comprised of a grid of blocks that can either
be commercial blocks (0s) or park blocks (1s). The city will only issue one permit for a truck per park in the city.
One park is defined as a contiguous set of park blocks. Any park block that is adjacent to another park block is part of the same park.
Diagonal moves are not allowed when defining a single park.
Given a grid that represents the city (2 dimensional array/list of 1s and 0s), and the number of rows (N) and number of columns (M),
determine how many food trucks the company can deploy in this city.
