//
//  UniverseScene.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation
import SpriteKit

class UniverseScene: SKScene {
    let universe = BruteForceUniverse(numberOfBodies: 100)
    private var bodyShapes = [SKShapeNode]()
    private var lastUpdatedAt: TimeInterval?

    override func didMove(to view: SKView) {
        backgroundColor = SKColor.white

        for body in universe.bodies {
            let bodyShape = createNode(for: body)
            bodyShape.fillColor = body.color
            bodyShapes.append(bodyShape)
            addChild(bodyShape)
        }
    }

    func createNode(for body: Body) -> SKShapeNode {
        if let planetoid = body as? Planetoid {
            return SKShapeNode(circleOfRadius: CGFloat(planetoid.mass / universe.solarMass))
        } else {
            return SKShapeNode(rectOf: CGSize(width: 10, height: 10))
        }
    }

    override func update(_ currentTime: TimeInterval) {
        let minimumSideLength = min(size.width, size.height)
        let coordinateSizingParamter = Double(minimumSideLength) / universe.radius * 100

        for index in 0..<universe.bodies.count {
            let body = universe.bodies[index]
            let bodyShape = bodyShapes[index]

            bodyShape.position = CGPoint(x: body.position.x * coordinateSizingParamter + Double(size.width / 2), y: body.position.y * coordinateSizingParamter + Double(size.height / 2))
        }

        if let lastUpdatedAt = lastUpdatedAt {
            let elapsedTime = currentTime - lastUpdatedAt
            universe.update(elapsedTime: elapsedTime)
        }

        lastUpdatedAt = currentTime
    }
}
