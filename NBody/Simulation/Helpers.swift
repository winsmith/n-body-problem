//
//  Helpers.swift
//  NBody
//
//  Created by Daniel Jilg on 14.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

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
