//
//  SystemRenderer.swift
//  NBody
//
//  Created by Daniel Jilg on 06.05.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation
import SceneKit
import SpriteKit
import MetalKit // 🤟

/// Helper Class to render offline versions of scenes for the talk
class SystemRenderer {
    var device: MTLDevice! = nil
    var renderer: SKRenderer! = nil
    var skSccene: SKScene! = nil
    var commandQueue: MTLCommandQueue! = nil

    init(scene: SKScene) {
        skSccene = scene
        device = MTLCreateSystemDefaultDevice()
        commandQueue = device.makeCommandQueue()
        renderer = SKRenderer(device: device)
        renderer.scene = skSccene
    }

    func render() {
        let viewport = CGRect(x: 0, y: 0, width: 640, height: 480)
        // renderer.render(withViewport: viewport, commandBuffer: commandQueue, renderPassDescriptor: <#T##MTLRenderPassDescriptor#>)
    }
}

