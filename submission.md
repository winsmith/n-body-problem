# Python in Space - The N Body Problem

## Abstract
The N Body Problem is a computationally complex problem that we use to predict how planets and galaxies – and everything in between – move through space. I'll show you some interesting ways to calculate it, and we'll have a look at what to do, should you find yourself in a space ship's pilot seat.

## Description
The N Body Problem is one of those famously hard to solve problems in computer science. It describes the movement and interactions of *n* bodies in space (where *n* is usually >= 3). You need a lot of computational power to passably approximate the gravitational influences a group of celestial bodies exert on each other. Can Python do that?

I'll give a super brief overview of the history of trying to predict the motion of moon, sun and the visible stars, and then we'll dive deep into the original N Body Problem, followed by creative ways to reduce the amount of calculation needed and still get a reasonable approximation. Doing this, we can see how to tackle some complex mathematic and algorithmic problems easily using Python.

If you're a Python beginner or even very early in your career as a developer, you are going to get a first impression of efficient algorithms and complex data structures, and how to measure complexity using Big O notation. If you're more advanced, you'll be treated to a hopefully interesting way of implementing the Barnes-Hutt-algorithm, and some space nerdery.

Once we have all the pieces in place, let's play with some orbits. We'll see how orbits actually behave, as opposed to what the untrained mind would expect. We can use our new algorithms to try out some manoeuvres often used by real space craft and help you be prepared for when that call from ESA or NASA finally comes, and you'll be invited to work on Python In Space!

## Reviewer Notes
In the last 12 years, I've been an app developer, a CTO, and a Python developer, mostly at the same time. I've carried through it all a desire to learn, a love for data visualisation, and a knack to pass on what I learned. Recently, my interest for anything space-related is in hyperdrive, and I want to share a slice of what makes space travel so interesting, while tying it all to concepts we as Python developers understand. 

This proposal is the second version of this talk, which started out as a short workshop on how to implement various methods of calculating orbits, and was generally well-received. I'll try to include live animations of relevant data, with fallbacks on pre rendered data.

This talk has two main aims. One is to introduce or refresh the audience's understanding of complexity analysis and good organisation of algorithmic code in Python, especially using tree structures. While I sweated the details quite a bit, audience members don't need to understand every last technicality to follow along. Instead, I hope to instill a general feeling of what is possible and what good practices are to keep complexity low and performance high in a Python program.

The other aim I have is to unabashedly share my love of space and orbital dynamics. Let's nerd out.
