package at.htlhl

import java.nio.file.Files
import kotlin.io.path.Path
import kotlin.math.abs
import kotlin.math.cbrt
import kotlin.math.pow
import kotlin.streams.asSequence

fun main() {
    val s = Files.readAllLines(Path("input.txt"))
    val coords: MutableList<Triple<Int, Int , Int>> = mutableListOf();
    for ((i, l) in s.withIndex()) {
        val p = l.split(",")
        coords.add(Triple(p[0].toInt(), p[1].toInt(), p[2].toInt()))
    }

    val circuits: MutableList<MutableSet<Triple<Int, Int, Int>>> = mutableListOf();
    var count = 1
    val seen = mutableSetOf<Pair<Int, Int>>()
    var smallestElements: Pair<Triple<Int, Int, Int>, Triple<Int, Int, Int>>
    var smallestElementsI: Pair<Int, Int>
    do {
        var smallest = Double.POSITIVE_INFINITY
        smallestElements = Pair(Triple(0, 0, 0), Triple(0, 0, 0))
        smallestElementsI = Pair(0, 0)
        for ((i, y) in coords.withIndex()) {
            for ((j, x) in coords.stream().skip(i.toLong() + 1).asSequence().toList().withIndex()) {
                if (seen.contains(Pair(i, j)))
                    continue

                val distance = getDistance(x, y)
                if (distance < smallest) {
                    smallest = distance
                    smallestElements = Pair(x, y)
                    smallestElementsI = Pair(i, j)
                }
            }
        }
        seen.add(smallestElementsI)
        addToCircuit(circuits, smallestElements)

        count++
    } while (count < 5 || !(circuits.size == 1 && circuits.first().size == coords.size))

    println(smallestElements.first.first.toLong() * smallestElements.second.first.toLong())
}

fun addToCircuit(
    circuits: MutableList<MutableSet<Triple<Int, Int, Int>>>,
    smallestElements: Pair<Triple<Int, Int, Int>, Triple<Int, Int, Int>>
) {
    val (a, b) = smallestElements
    var circuitA: MutableSet<Triple<Int, Int, Int>>? = null
    var circuitB: MutableSet<Triple<Int, Int, Int>>? = null
    for (c in circuits) {
        if (c.contains(a))
            circuitA = c
        if (c.contains(b))
            circuitB = c
        if (c.contains(a) && c.contains(b))
            return
    }

    if (circuitA == null && circuitB == null) {
        val newCircuit: MutableSet<Triple<Int, Int, Int>> = mutableSetOf()
        newCircuit.add(a)
        newCircuit.add(b)
        circuits.add(newCircuit)
        return
    }

    if (circuitA != null && circuitB != null) {
        circuitB.addAll(circuitA)
        circuits.remove(circuitA)
    }

    circuitA?.add(b)
    circuitB?.add(a)
}

fun getDistance(x: Triple<Int, Int, Int>, y: Triple<Int, Int, Int>): Double {
    val (a, b, c) = x
    val (d, e, f) = y
    return cbrt((
            abs(d - a).toDouble().pow(2.toDouble()) +
                    abs(e - b).toDouble().pow(2.toDouble()) +
                    abs(f - c).toDouble().pow(2.toDouble())))
}
