//
//  ViewController.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Cocoa
import SpriteKit

class MainViewController: NSViewController {
    // MARK: Properties

    // MARK: View Life Cycle

    override func viewDidLoad() {
        super.viewDidLoad()

        let skView = view as! SKView
        let scene = SystemScene(size: view.bounds.size)
        skView.showsFPS = false
        skView.showsNodeCount = false
        skView.ignoresSiblingOrder = true
        scene.scaleMode = .resizeFill
        skView.presentScene(scene)
    }
}

