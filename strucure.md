# Python in Space - The N-Body Problem

## The history of Celestial Mechanics
- The name celestial mechanics:
	- "Modern analytic celestial mechanics started with Isaac Newton's Principia of 1687. The name "celestial mechanics" is more recent than that. Newton wrote that the field should be called "rational mechanics." The term "dynamics" came in a little later with Gottfried Leibniz, and over a century after Newton, Pierre-Simon Laplace introduced the term "celestial mechanics." Prior to Kepler there was little connection between exact, quantitative prediction of planetary positions, using geometrical or arithmetical techniques, and contemporary discussions of the physical causes of the planets' motion."
- Important
	- Johannes Kepler
	- Isaac Newton
	- 	Joseph-Louis Lagrange
	- 	Simon Newcomb
	- 	Albert Einstein
- Antiquity
	- Aristarchus of Samos (c. 310 BC - c. 230 BC)
		- First Heliocentric model, but text has been lost
		- Explanation of missing stellar parallax
	- Claudius Ptolemaeus (c. AD 100 – c. 170)
		- Geocentric model
		- the spherical Earth lying motionless as the center
		- "fixed stars"
		- various planets revolving around the Earth.
			- The celestial realm is spherical, and moves as a sphere.
		- The Earth is a sphere.
		- The Earth is at the center of the cosmos.
		- The Earth, in relation to the distance of the fixed stars, has no appreciable size and must be treated as a mathematical point.
		- The Earth does not move.
- Middle Ages
	- Mo'ayyeduddin al-Urdi, Nasir al-Din al-Tusi, and Ibn al-Shatir
	- Nicolaus Copernicus (1473-1553) 
		- De revolutionibus orbium coelestium (1543)
		- heliocentric model
		- Sun in the middle
		- planets move in circular paths around it
		- launching point for modern astronomy
- Copernican Revolution
	- "From publication until about 1700, few astronomers were convinced by the Copernican system, though the book was relatively widely circulated (around 500 copies of the first and second editions have survived,[34] which is a large number by the scientific standards of the time)."
	- Few people at the time were ready to concede that the earth moved around the sun at the time
	- Advantages of the copernican model
		- accurately predicts the relative distances of the planets from the Sun
		- account of the cause of the seasons: that the Earth's axis is not perpendicular to the plane of its orbit
		-  explanation for the apparent retrograde motions of the planets—"namely as parallactic displacements resulting from the Earth's motion around the Sun"
	-  Disadvantages
		-  contrary to common sense 
		-  contradicts the Bible
		-  Aristotelian Physics (as opposed to Newtonian Physics) did not have an explanation of why bodies would move on their own, but postulated that heavenly bodies, being made of "aether" just have movement as a property
		-  Stars would have to be HUGE
		-  Tycho Brahe: The Copernican system "...“... expertly and completely circumvents all that is superfluous or discordant in the system of Ptolemy. On no point does it offend the principle of mathematics. Yet it ascribes to the Earth, that hulking, lazy body, unfit for motion, a motion as quick as that of the aethereal torches, and a triple motion at that.” (Owen Gingerich, The eye of heaven: Ptolemy, Copernicus, Kepler, New York: American Institute of Physics, 1993, 181, ISBN 0-88318-863-5)
- Kepler (1609)
	- used Tycho Brahe's observations of Mars' orbit
	- laws of planetary motion
	- The orbit of a planet is an ellipse with the Sun at one of the two foci.
	- A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.[1]
	- The square of the orbital period of a planet is proportional to the cube of the semi-major axis of its orbit.
- Modern Astrodynamics
- Anders Johan Lexell (1740 – 1784)
	- "The beginning of modern understanding of orbit determination is considered to be Anders Johan Lexell's work on computing the orbit of the comet discovered in 1770 that later was named Lexell's Comet,[1] in which Lexell computed the interaction of comet with Jupiter that first made the comet fly close to Earth and then would have expelled it from the Solar system.[2]"
- Johann Heinrich Lambert (1728 – 1777) 
	- https://en.wikipedia.org/wiki/Lambert%27s_problem
- Carl-Friedrich Gauss (1777–1855)
	- "Another milestone in orbit determination was Carl Friedrich Gauss' assistance in the "recovery" of the dwarf planet Ceres in 1801. Gauss' method was able to use just three observations (in the form of pairs of right ascension and declination), to find the six orbital element that completely describe an orbit. The theory of orbit determination has subsequently been developed to the point where today it is applied in GPS receivers as well as the tracking and cataloguing of newly observed minor planets."
	- https://en.wikipedia.org/wiki/Gauss%27_method

## The N-Body Problem
- what is it
	- Newton tried to use analytical geometry to predict the planets' motions from its orbital properties (position, orbital diameter, period and orbital velocity) and failed
	- realised that there is a gravitational interaction between the planets that is affecting their orbits
	- In the solar system, every planet is gravitationally affected by all the other planets to some degree. 
	- This is also true for other bodies inside and outside the solar system
	- it is easy to calculate the gravitationally interactive forces between two bodies using newtonian physics
	- as soon as there are more than two bodies involved, things get  harder to predict 
	- This technique is pretty close to reality -- the moon landings used newtonian mechanics to calculate their orbits -- but it has to be said that einstein showed that there are small micro-interactions between bodies that newtonian physics cannot predict
- why is it hard
	- This is because every body's gravity influences all the other bodies orbital parameters, which in turn influence all OTHER bodies
	- for n bodies, there are n^2 interactions to calculate
	- you have to take all bodies into account, or your result will be very imprecise 
	- You can use this to find bodies you don't know about: Plug all bodies you know about into the equations, calculate, and if the result differs from reality, Boom, you know where to look for your new dark moon
- approximation using Barnes-Hutt 
	- organise all bodies into an octo-tree (or quad-tree for 2d), ordered by their distance from each other
	- each Body is a leaf on the end of the tree, and saves its mass, plus its orbital parameters
	- save the combined mass of the attached bodies for each node
	- for far away bodies, do not calculate every body's mass and gravitational interaction individually -- instead, with increasing distance, retreat further and further up the tree and use the mass information in the upper nodes
	- it can be proven that due to the inverse square root relation of gravity to mass over distance, this only gives us very small errors as opposed to calculating every individual body
	- However, the complexity sinks from O(n^2) to O(n log n)
- Nerd Stuff
	- complexity analysis
	- tree structures
	- classes
	- algorithms
- Fun Stuff 
	- live visualisation

## Let's play with some orbits
- periapsis and apoapsis
- how to influence your orbit
- Hohmann transfer
- the oberth effect
- gravity assists
- how to land a space craft

## Sources: 

- https://en.wikipedia.org/wiki/Celestial_mechanics
- https://en.m.wikipedia.org/wiki/Caroline_Herschel
- https://en.wikipedia.org/wiki/Al-Sijzi
- https://en.wikipedia.org/wiki/Lexell%27s_Comet
- https://en.wikipedia.org/wiki/Fixed_stars
- https://en.wikipedia.org/wiki/Aristarchus_of_Samos
- https://en.wikipedia.org/wiki/Orbit_determination
- https://en.wikipedia.org/wiki/Copernican_heliocentrism
- https://en.wikipedia.org/wiki/Ptolemy
- https://en.m.wikipedia.org/wiki/Barnes–Hut_simulation
- https://en.m.wikipedia.org/wiki/N-body_simulation
- https://en.m.wikipedia.org/wiki/Octree
- https://en.m.wikipedia.org/wiki/Quadtree
- https://en.m.wikipedia.org/wiki/Discrete_element_method
- https://books.google.de/books/about/Fundamentals_of_Astrodynamics.html?id=UtJK8cetqGkC&source=kp_cover&redir_esc=y
- https://books.google.de/books/about/Spacecraft_Systems_Engineering.html?id=cCYP0rVR_IEC&source=kp_cover&redir_esc=y
- https://en.wikipedia.org/wiki/Two-line_element_set
- Owen Gingerich, The eye of heaven: Ptolemy, Copernicus, Kepler, New York: American Institute of Physics, 1993, 181, ISBN 0-88318-863-5


## Code
http://physics.princeton.edu/~fpretori/Nbody/code.htm