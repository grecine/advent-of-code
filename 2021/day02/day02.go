package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"time"

	"github.com/bogosj/advent-of-code/intmath"
)

type SubVec struct {
	h, v, a int
}

func part1(in []string) {
	pos := SubVec{}

	for _, command := range in {
		com := strings.Fields(command)
		if com[0] == "forward" {
			pos.v += intmath.Atoi(com[1])
		}
		if com[0] == "down" {
			pos.h += intmath.Atoi(com[1])
		}
		if com[0] == "up" {
			pos.h -= intmath.Atoi(com[1])
		}
	}

	fmt.Println("Part 1: ", pos.h*pos.v)
}

func part2(in []string) {

	pos := SubVec{}

	for _, command := range in {
		com := strings.Fields(command)
		if com[0] == "forward" {
			pos.v += intmath.Atoi(com[1])
			pos.h += pos.a * intmath.Atoi(com[1])
		}
		if com[0] == "down" {
			pos.a += intmath.Atoi(com[1])
		}
		if com[0] == "up" {
			pos.a -= intmath.Atoi(com[1])
		}
	}

	fmt.Println("Part 2: ", pos.h*pos.v)
}

func main() {
	// in := input("test-input.csv")
	in := input("input.csv")

	t0 := time.Now()
	part1(in)
	fmt.Println("Part 1 took", time.Since(t0))

	t0 = time.Now()
	part2(in)
	fmt.Println("Part 2 took", time.Since(t0))
}

func input(fname string) []string {
	in, _ := ioutil.ReadFile(fname)
	data := strings.TrimSpace(string(in))
	return strings.Split(data, "\n")
}
