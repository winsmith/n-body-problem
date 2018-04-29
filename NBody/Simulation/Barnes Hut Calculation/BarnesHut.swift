//
//  BarnesHut.swift
//  NBody
//
//  Created by Daniel Jilg on 25.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

class BarnesHut: SelectionAlgorithm {
    let quadrant = Quadrant(center: Position(x: 0, y: 0), diameter: 2*1e18)

    func update(bodies: [Body], elapsedTime: Double) {
        let theTree = BHTree.init(self.quadrant)

        // If the body is inside the current quadrant, add it to the tree
        for body in bodies {
            guard let planetoid = body as? Planetoid else { continue }
            if quadrant.contains(body.position) {
                theTree.insert(insertedBody: planetoid)
            }
        }

        //  Now, use our methods in BHTree to update the forces,
        // traveling recursively through the tree
        for body in bodies {
            guard let planetoid = body as? Planetoid else { continue }
            planetoid.resetForce()
            if quadrant.contains(planetoid.position) {
                theTree.updateForce(with: planetoid)
                planetoid.update(timeSteps: elapsedTime)
            }
        }
    }
}
