# Swift in Space - The N Body Problem

> The N Body Problem is a computationally complex problem that we use to predict how planets and galaxies – and everything in between – move through space. I'll show you some interesting ways to calculate it, and we'll have a look at what to do, should you find yourself in a space ship's pilot seat.

This repository contains talk notes, example code, and general preparations for my talk about the N-Body Problem.

## A Note about Versions

This branch contains the Swift version of this talk. For an older version with example code in Python, look at the `python` branch.

## To Dos

- merge timeSteps and ticks and such
- Improve `circularVelocity` helper method
- extract calculation code into its own object so the calculation can be switched between Hohmann and Brute Force at run time
- Bodys that are not planetoids should be able to be accelerated
- Add a trailing path to nodes
- explode bodies when they crash into each other
