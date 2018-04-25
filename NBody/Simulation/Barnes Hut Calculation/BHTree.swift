//
//  BHTree.swift
//  NBody
//
//  Created by Daniel Jilg on 25.04.18.
//  Copyright © 2018 breakthesystem. All rights reserved.
//

import Foundation

class BHTree {
    let quadrant: Quadrant
    var body: Planetoid?

    var northWest: BHTree?
    var northEast: BHTree?
    var southWest: BHTree?
    var southEast: BHTree?

    /// If all nodes of the BHTree are null, then the quadrant represents a single body and it is "external" or a leaf of the tree
    var isLeaf: Bool {
        return (
            northWest == nil &&
            northEast == nil &&
            southWest == nil &&
            southEast == nil
        )
    }

    init(_ quadrant: Quadrant) {
        self.quadrant = quadrant
    }

    /// We have to populate the tree with bodies. We start at the current tree and recursively travel through the branches
    func insert(insertedBody: Planetoid) {
        // If there's not a b there already, put the b there.
        if body == nil {
            body = insertedBody
        }

        // If there's already a body there, but it's not an external node combine the two bodies and figure out which quadrant of the tree it should be located in. Then recursively update the nodes below
        else if !isLeaf {
            // In this case, this means "add the acting forces together
            insertedBody.accelerate(with: body!)

            let nw = quadrant.subquadrantNorthWest()
            if nw.contains(insertedBody.position) {
                northWest = northWest ?? BHTree(nw)
                northWest!.insert(insertedBody: insertedBody)
                return
            }

            let ne = quadrant.subquadrantNorthEast()
            if ne.contains(insertedBody.position) {
                northEast = northEast ?? BHTree(ne)
                northEast!.insert(insertedBody: insertedBody)
                return
            }

            let sw = quadrant.subquadrantSouthWest()
            if sw.contains(insertedBody.position) {
                southWest = southWest ?? BHTree(sw)
                southWest!.insert(insertedBody: insertedBody)
                return
            }

            let se = quadrant.subquadrantSouthEast()
            if se.contains(insertedBody.position) {
                southEast = southEast ?? BHTree(se)
                southEast!.insert(insertedBody: insertedBody)
                return
            }
        }

        // # If the node is a leaf and contains another body, create sub-BHTrees, inserting the new body
        else {
            // TODO: This method works with self.body -- shouldnt it rather work with insertedBody?

            let nw = quadrant.subquadrantNorthWest()
            if nw.contains(body!.position) {
                northWest = northWest ?? BHTree(nw)
                insert(insertedBody: body!)
                return
            }

            let ne = quadrant.subquadrantNorthEast()
            if ne.contains(body!.position) {
                northEast = northEast ?? BHTree(ne)
                insert(insertedBody: body!)
                return
            }

            let sw = quadrant.subquadrantSouthWest()
            if sw.contains(body!.position) {
                southWest = southWest ?? BHTree(sw)
                insert(insertedBody: body!)
                return
            }

            let se = quadrant.subquadrantSouthEast()
            if se.contains(body!.position) {
                southEast = southEast ?? BHTree(se)
                insert(insertedBody: body!)
                return
            }
        }
    }

    /// Start at the main node of the tree. Then, recursively go each branch Until either we reach an leaf node or we reach a node that is sufficiently far away that the external nodes would not matter much.
    func updateForce(with otherBody: Planetoid) {
        if isLeaf {
            otherBody.accelerate(with: body!)
        }

        else if body! !== otherBody && quadrant.diameter / body!.position.distance(to: otherBody.position) < 2 {
            otherBody.accelerate(with: body!)
        }

        else {
            for quadrant in [northWest, northEast, southWest, southEast] {
                quadrant?.updateForce(with: otherBody)
            }
        }
    }
}
