0x0A. Prime Game
Description
In this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.

Concepts Needed
Prime Numbers: Understanding what prime numbers are and efficient algorithms for identifying prime numbers within a range.
Sieve of Eratosthenes: An efficient algorithm for finding all prime numbers up to any given limit.
Game Theory: Basic principles of competitive games where players take turns and the concept of optimal play.
Dynamic Programming/Memoization: Using previous results to make future calculations faster.
Python Programming: Loops, conditional statements, arrays, and lists for implementing game logic and algorithms.
Resources
Prime Numbers and Sieve of Eratosthenes
Game Theory Introduction
Dynamic Programming With Python Examples
Python Lists
Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Code should use the PEP 8 style (version 1.7.x)
All files must be executable
Tasks
0. Prime Game
File: 0-prime_game.py

Description: Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

Prototype: def isWinner(x, nums)

x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4
Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5
Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1
Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins