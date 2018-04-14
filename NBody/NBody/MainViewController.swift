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
    @IBOutlet weak var spriteKitView: SKView!

    override func viewDidLoad() {
        super.viewDidLoad()
        let scene = UniverseScene(size: view.bounds.size)
        spriteKitView.showsFPS = true
        spriteKitView.showsNodeCount = true
        spriteKitView.ignoresSiblingOrder = true
        scene.scaleMode = .resizeFill
        spriteKitView.presentScene(scene)
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}

