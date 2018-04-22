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
    let universe = BruteForceUniverse(numberOfBodies: 10)
    private var bodyShapes = [SKShapeNode]()
    private var bodyLabels = [SKLabelNode]()
    private var radii = [CGFloat]()
    private var lastUpdatedAt: TimeInterval?

    public var timeWarpFactor = 6e9

    override func didMove(to view: SKView) {
        backgroundColor = SKColor.white

        // Create Shapes
        for body in universe.bodies {
            let bodyShape = createNode(for: body)
            bodyShape.fillColor = body.color
            bodyShapes.append(bodyShape)
            addChild(bodyShape)
        }

        // Create Labels
        for body in universe.bodies {
            let bodyLabel = SKLabelNode(text: body.name)
            bodyLabel.fontColor = body.color
            bodyLabels.append(bodyLabel)
            addChild(bodyLabel)
        }
    }

    private func createNode(for body: Body) -> SKShapeNode {
        if let planetoid = body as? Planetoid {
            let radius: CGFloat = min(max(CGFloat(planetoid.mass * 1e4 / universe.solarMass), 3), 200)
            let shapenode = SKShapeNode(circleOfRadius: radius)
            return shapenode
        } else {
            return SKShapeNode(rectOf: CGSize(width: 10, height: 10))
        }
    }

    override func update(_ currentTime: TimeInterval) {
        let minimumSideLength = min(size.width, size.height)
        let coordinateSizingParameter = Double(minimumSideLength) / universe.radius

        for index in 0..<universe.bodies.count {
            let body = universe.bodies[index]
            let bodyShape = bodyShapes[index]
            let bodyLabel = bodyLabels[index]

            bodyShape.position = CGPoint(
                x: body.position.x * coordinateSizingParameter + Double(size.width / 2),
                y: body.position.y * coordinateSizingParameter + Double(size.height / 2)
            )
            bodyLabel.position = CGPoint(x: bodyShape.position.x, y: bodyShape.position.y - (30 + (bodyShape.path?.boundingBox.height ?? 10) / 2))

            bodyLabel.text = "\(body.name)" //" \(bodyShape.position.y)"
        }

        if let lastUpdatedAt = lastUpdatedAt {
            let elapsedTime = currentTime - lastUpdatedAt
            universe.update(elapsedTime: elapsedTime * timeWarpFactor)
        }

        lastUpdatedAt = currentTime
    }
}
