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
    let universe = BruteForceUniverse(numberOfBodies: 20)
    private var bodyShapes = [SKShapeNode]()
    private var bodyLabels = [SKLabelNode]()
    private var lastUpdatedAt: TimeInterval?

    public var timeWarpFactor = 1e7
    public var drawTrails = true

    override func didMove(to view: SKView) {
        backgroundColor = SKColor.white

        // Create Shapes
        for body in universe.bodies {
            createNodes(for: body)
        }
    }

    private func createNodes(for body: Body) {
        var bodyShape: SKShapeNode?

        if let planetoid = body as? Planetoid {
            let radius: CGFloat = min(max(CGFloat(planetoid.mass * 1e4 / universe.solarMass), 3), 200)
            bodyShape = SKShapeNode(circleOfRadius: radius)
        } else {
            bodyShape = SKShapeNode(rectOf: CGSize(width: 10, height: 10))
        }

        // Configure Trail
        if let emitter = SKEmitterNode(fileNamed: "TrailParticle.sks"), drawTrails {
            emitter.targetNode = self
            emitter.particleColor = body.color
            bodyShape?.addChild(emitter)
        }

        let bodyLabel = SKLabelNode(text: body.name)

        bodyShape!.fillColor = body.color
        bodyLabel.fontColor = body.color

        bodyShapes.append(bodyShape!)
        bodyLabels.append(bodyLabel)

        addChild(bodyShape!)
        addChild(bodyLabel)
    }

    override func update(_ currentTime: TimeInterval) {
        updateUniverseStatus(currentTime)
        updateUniverseDisplay()

        lastUpdatedAt = currentTime
    }

    fileprivate func updateUniverseDisplay() {
        let minimumSideLength = min(size.width, size.height)
        let zoomFactor = Double(minimumSideLength) / (universe.radius * 2)

        for index in 0..<universe.bodies.count {
            let body = universe.bodies[index]
            let bodyShape = bodyShapes[index]
            let bodyLabel = bodyLabels[index]

            // Update Shape
            bodyShape.position = CGPoint(
                x: body.position.x * zoomFactor + Double(size.width / 2),
                y: body.position.y * zoomFactor + Double(size.height / 2)
            )

            // Update Label
            bodyLabel.position = CGPoint(x: bodyShape.position.x, y: bodyShape.position.y - (30 + (bodyShape.path?.boundingBox.height ?? 10) / 2))
            bodyLabel.text = "\(body.name)"
            // bodyLabel.text = "\(body.direction)"
        }
    }

    fileprivate func updateUniverseStatus(_ currentTime: TimeInterval) {
        if let lastUpdatedAt = lastUpdatedAt {
            let elapsedTime = currentTime - lastUpdatedAt
            universe.update(elapsedTime: elapsedTime * timeWarpFactor)
        }
    }
}
