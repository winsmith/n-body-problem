//
//  SelectionAlgorithm.swift
//  NBody
//
//  Created by Daniel Jilg on 25.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

protocol SelectionAlgorithm {
    func update(bodies: [Body], elapsedTime: Double)
}
