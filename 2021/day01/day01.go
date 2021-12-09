package main

import (
	"fmt"
	"io"
	"os"
	"time"
	// "github.com/adam-lavrik/go-imath/ix"
	// "github.com/bogosj/advent-of-code"
)

func part1(in []int) {
	count := 0
	for i := 1; i < len(in); i++ {
		if in[i-1] < in[i] {
			count++
		}
	}

	fmt.Println("Part 1: ", count)
}

func part2(in []int) {
	var sum3 []int

	count := 1
	sum3 = append(sum3, 0, 0, in[0]+in[1]+in[2])
	for i := 3; i < len(in); i++ {
		sum3 = append(sum3, in[i-3]+in[i-2]+in[i-1])
		if sum3[i-1] < sum3[i] {
			count++
		}
	}

	fmt.Println("Part 1: ", count)
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

func input(fname string) []int {
	file, _ := os.Open(fname)

	var perline int
	var nums []int

	for {
		_, err := fmt.Fscanf(file, "%d\n", &perline)

		if err != nil {

			if err == io.EOF {
				break
			}
			fmt.Println(err)
			os.Exit(1)
		}

		nums = append(nums, perline)
	}

	return nums
}
