# Swift in Space - The N Body Problem

> The N Body Problem is a computationally complex problem that we use to predict how planets and galaxies – and everything in between – move through space. I'll show you some interesting ways to calculate it, and we'll have a look at what to do, should you find yourself in a space ship's pilot seat.

This repository contains talk notes, example code, and general preparations for my talk about the N-Body Problem.

## A Note about Versions

This branch contains the Swift version of this talk. For an older version with example code in Python, look at the `python` branch.

## Bodies and Planetoids

The idea here is to a have two types of bodies: `Body`, and `Planetoid`, where `Body` might be something tiny and `Planetoid` is something that has considerable mass. `Planetoids` are also `Bodies`, but the inverse is not true.

Right now, `Body` instances are pretty much ignored and only `Planetoid` instances are accelereated. This should change at some point.  

## To Dos

- merge timeSteps and ticks and such
- Bodys that are not planetoids should be able to be accelerated
- explode bodies when they crash into each other 💥
- Update Readme with UniverseScene, Initializers, Calculations
