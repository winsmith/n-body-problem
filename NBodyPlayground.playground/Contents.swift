//: Playground - noun: a place where people can play

import Cocoa
import SpriteKit
import PlaygroundSupport

//Basic dimensions that we will use more later
let frame = CGRect(x: 0, y: 0, width: 320, height: 256)
let midPoint = CGPoint(x: frame.size.width / 2.0, y: frame.size.height / 2.0)

//Create a scene, add something to it
var scene = SKScene(size: frame.size)
let nyanCat = SKSpriteNode(imageNamed: "Nyancat")
nyanCat.position = midPoint
nyanCat.setScale(8.0)
scene.addChild(nyanCat)

//Set up the view and show the scene
let view = SKView(frame: frame)
view.presentScene(scene)
PlaygroundPage.current.liveView = view
