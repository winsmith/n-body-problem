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
    let universe = Universe(initializer: RandomSolarInitializer(numberOfBodies: 42))
    private var bodyShapes = [SKShapeNode]()
    private var lastUpdatedAt: TimeInterval?

    public var timeWarpFactor = 1e7
    public var drawTrails = true
    public var selectionAlgorithm: SelectionAlgorithm = BarnesHut()

    public var zoomFactor = 23e8

    override func didMove(to view: SKView) {
        backgroundColor = SKColor.white
        universe.selectionAlgorithm = selectionAlgorithm

        // Create Camera
        let cameraNode = SKCameraNode()
        addChild(cameraNode)
        cameraNode.setScale(1.2)
        camera = cameraNode

        // Create Shapes
        for body in universe.bodies {
            createNodes(for: body)
        }
    }

    private func createNodes(for body: Body) {
        var bodyShape: SKShapeNode?

        // Configure Shape
        if let planetoid = body as? Planetoid {
            let radius: CGFloat = max(CGFloat(planetoid.radius * 64 / zoomFactor), 2)
            bodyShape = SKShapeNode(circleOfRadius: radius)
        } else {
            bodyShape = SKShapeNode(rectOf: CGSize(width: 10, height: 10))
        }

        bodyShape!.fillColor = body.color
        bodyShapes.append(bodyShape!)
        addChild(bodyShape!)

        // Configure Trail
        if let emitter = SKEmitterNode(fileNamed: "TrailParticle.sks"), drawTrails {
            emitter.targetNode = self
            emitter.particleColor = body.color
            bodyShape?.addChild(emitter)
        }

        // Configure Label
        if let name = body.name {
            let bodyLabel = SKLabelNode(text: name)
            bodyLabel.fontColor = body.color
            bodyLabel.position = CGPoint(x: bodyShape!.position.x, y: bodyShape!.position.y - (30 + (bodyShape?.path?.boundingBox.height ?? 10) / 2))
            bodyShape?.addChild(bodyLabel)
        }
    }

    override func update(_ currentTime: TimeInterval) {
        updateUniverseStatus(currentTime)
        updateUniverseDisplay()

        lastUpdatedAt = currentTime
    }

    fileprivate func updateUniverseDisplay() {
        for index in 0..<universe.bodies.count {
            let body = universe.bodies[index]
            let bodyShape = bodyShapes[index]

            // Update Position
            bodyShape.position = CGPoint(
                x: body.position.x / zoomFactor,
                y: body.position.y / zoomFactor
            )
        }
    }

    fileprivate func updateUniverseStatus(_ currentTime: TimeInterval) {
        if let lastUpdatedAt = lastUpdatedAt {
            let elapsedTime = currentTime - lastUpdatedAt
            universe.update(elapsedTime: elapsedTime * timeWarpFactor)
        }
    }

    // MARK: - Keyboard Control
    override func keyDown(with theEvent: NSEvent) {
        guard let camera = camera else { return }
        let zoomStep: CGFloat = 0.2

        if theEvent.characters == "," {
            camera.setScale(max(camera.xScale - zoomStep, 0.1))
        }

        else if theEvent.characters == "." {
            camera.setScale(camera.xScale + zoomStep)
        }
    }
}
