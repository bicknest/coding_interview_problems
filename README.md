# coding_interview_problems

A repo to hold an assortment of problems that could come up in coding interviews

# Installation instructions

clone the repo: `git clone https://github.com/bicknest/coding_interview_problems.git`

install yarn `brew install yarn`

run `yarn` to install JavaScript dependencies

Install pipenv `brew install pipenv`

install the python dependencies with pipenv


# Using this repo for your own practice

This repo's solutions have 100% test coverage, a commit will be rejected if it is not fully covered

This allows for you to write your own solution and use these tests to check if your solution is correct.


# Contributing to this repo

If you would like to add a solution in a different programming language:
1. Make sure that there is a testing solution in place for that language, if not, add one
2. Create a new folder in the problem's folder that is the name of the language then add your solution and tests

If you would like to add a new problem:
1. Create a folder with a descriptive name of the problem
2. Write a problem defintion file and an approach file
  * The approach file should have an explanation of the implementation along with space/time complexity explanations
  * The problem defintion should include a detailed description of the input and the expected output
3. Add a folder that is named the language you are using to solve the problem
4. Write your solution and add thorough tests.
  * Make sure your tests cover base and edge cases
