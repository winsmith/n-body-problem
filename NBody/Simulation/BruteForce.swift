//
//  BruteForce.swift
//  NBody
//
//  Created by Daniel Jilg on 25.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

struct BruteForce: SelectionAlgorithm {
    func update(bodies: [Body], elapsedTime: Double) {
        for body in bodies where body is Planetoid {
            body.resetForce()

            // uh, oh a loop inside a loop
            // This'll get us n^2 complexity
            for otherBody in bodies where body is Planetoid {
                if otherBody !== body {
                    (body as! Planetoid).accelerate(with: (otherBody as! Planetoid))
                }
            }
        }

        for body in bodies {
            body.update(timeSteps: elapsedTime)
        }
    }
}
