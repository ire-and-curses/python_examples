#!/usr/bin/env python

'''
discrete_solver.py - Generalised solver for discrete problems.

Example: the 8 queens problem (see 8_queens.py).

Author: Eric Saunders
April 2011
'''


class Problem(object):

    def next(self):
        raise NotImplementedError("Provide the next thing to try here.")

    def make_move(self, move):
        raise NotImplementedError("Move the problem state to a new configuration.")

    def undo_last_move(self):
        raise NotImplementedError("Undo the last thing we did here.")

    def reset(self):
        raise NotImplementedError("Reset the state of the next() iterator")

    def is_solved(self):
        raise NotImplementedError("Implement a test for problem completion here.")



class FindValProblem(Problem):

    def __init__(self):
        self.vals        = [0,1,2,3,4,15]
        self.idx         = 0
        self.solution    = []


    def next(self):

        while True:

            # Don't provide more values if we have a full solution
            if len(self.solution) > 2:
                return False

            # If we still have values left to try...
            if self.idx < (len(self.vals) - 1):
                # Increment our pointer
                self.idx += 1

            else:
                # We've run out of values
                self.idx = len(self.vals)
                return False

            # Skip targets that are in the solution
            if not self.idx in self.solution:
                return self.idx

    def reset(self):
        self.idx = 0

    def make_move(self, move):
        self.solution.append(move)


    def undo_last_move(self):
        self.solution.pop()


    def is_solved(self):
        # We arbitrarily 'win' if our numbers sum to 9
        total = 0
        for idx in self.solution:
            total += self.vals[idx]

        if total == 9:
            return True

        return False


r_level = 0
def verbose_solve(problem):

    global r_level
    tried = []

    while True:

        print "Recursion level:", r_level
        print "Current solution state:", problem.solution
        print "Current tried list:", tried

        while True:
            next_to_try = problem.next()
            print "Next to try:", next_to_try

            if next_to_try == False: break
            if next_to_try not in tried: break

        if next_to_try is False:
            print "Ran out of things to try - backtracking..."
            problem.reset()

            return problem


        problem.make_move(next_to_try)

        # Recurse and try to solve the sub-problem
        print "    Recursing..."
        r_level += 1
        sub_problem = verbose_solve(problem)
        r_level -= 1
        print "De-recursed: current level:", r_level

        # Termination condition
        if problem.is_solved(): break

        print "Undoing last move"
        problem.undo_last_move()
        tried.append(next_to_try)
        print "So far we've tried:", tried, "\n"

    print "Solved problem with solution", problem.solution, "at recursion =",r_level

    return problem



def solve(problem):

    tried = []

    while True:

        # Find the next untried move
        while True:
            next_to_try = problem.next()

            if next_to_try == False:     break
            if next_to_try not in tried: break

        if next_to_try is False:
        #    problem.reset()
            return problem

        problem.make_move(next_to_try)

        # Recurse and try to solve the sub-problem
        sub_problem = solve(problem)

        # Termination condition
        if problem.is_solved(): break

        # This branch was unsuccessful - backtrack and record the failure
        problem.undo_last_move()
        tried.append(next_to_try)

    return problem



if __name__ == "__main__":
    problem = FindValProblem()
    problem = solve(problem)

    print "Solution =", problem.solution

