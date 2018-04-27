//
//  Universe.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import AppKit
import Foundation

/// A container for simulation of orbital dynamics
class Universe {
    // MARK: Properties
    public private(set) var bodies = [Body]()
    public var selectionAlgorithm: SelectionAlgorithm?

    // MARK: - Read-Only Configuration
    public let radius = 1e12

    init(initializer: UniverseInitializer) {
        bodies = initializer.createBodies(radius: radius)
    }

    func update(elapsedTime: Double) {
        selectionAlgorithm?.update(bodies: bodies, elapsedTime: elapsedTime)
    }
}
