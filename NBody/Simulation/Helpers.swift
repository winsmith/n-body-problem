//
//  Helpers.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import AppKit
import Foundation

// MARK: - Constants

/// Gravitational constant
let G = 6.673e-11

// MARK: - Double Extensions
extension Double {
    var squared: Double {
        return pow(self, 2)
    }
}

// MARK: - NSColor Extensions
extension NSColor {
    static func random() -> NSColor {
        let hue : CGFloat = CGFloat(arc4random() % 256) / 256 // use 256 to get full range from 0.0 to 1.0
        let saturation : CGFloat = CGFloat(arc4random() % 128) / 256 + 0.5 // from 0.5 to 1.0 to stay away from white
        let brightness : CGFloat = CGFloat(arc4random() % 128) / 256 + 0.5 // from 0.5 to 1.0 to stay away from black

        return NSColor(hue: hue, saturation: saturation, brightness: brightness, alpha: 1)
    }
}
