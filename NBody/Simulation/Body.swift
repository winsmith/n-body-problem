//
//  Body.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

class UniverseObject {
    var tickNumber: Int = 0
    var name: String

    init(tickNumber: Int, name: String) {
        self.tickNumber = tickNumber
        self.name = name
    }
}

class Body: UniverseObject {
    var position: Position
    var vector: Vector

    init(position: Position, vector: Vector, name: String = "Unnamed Body", tickNumber: Int = 0) {
        self.position = position
        self.vector = vector

        super.init(tickNumber: tickNumber, name: name)
    }
}

class Planetoid: Body {
    var mass: Float

    init(position: Position, vector: Vector, name: String = "Unnamed Planetoid", tickNumber: Int = 0, mass: Float = 7.34767309e22) {
        self.mass = mass

        super.init(position: position, vector: vector, name: name, tickNumber: tickNumber)
    }
}
