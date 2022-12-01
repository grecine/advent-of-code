package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
	// "github.com/adam-lavrik/go-imath/ix"
	// "github.com/bogosj/advent-of-code"
)

func maxarray(x [][]int) int {
	// var max_slice [] int
	// for i := 0; i <= len(x); i++ {
	// 	max_slice[i] := ix.MaxSlice(x[i])
	// }
	// max := ix.MaxSlice(max_slice)
	fmt.Println(x[0])
	return 1
}

func main() {
	header, vents := input("./test-input.csv")
	fmt.Println(header)
	fmt.Println(vents)

	// n := maxarray(vents)
	// fmt.Println(n)
}

func sliceAtoi(sa []string) ([]int, error) {
	si := make([]int, 0, len(sa))
	for _, a := range sa {
		i, err := strconv.Atoi(a)
		if err != nil {
			return si, err
		}
		si = append(si, i)
	}
	return si, nil
}

func input(fname string) ([]string, [][]string) {
	f, err := os.Open(fname)
	if err != nil {
		log.Fatal("Unable to read input file "+fname, err)
	}
	defer f.Close()

	csvReader := csv.NewReader(f)
	header, err := csvReader.Read()
	if err != nil {
		log.Fatal("Unable to parse file as CSV fir"+fname, err)
	}

	coords, err := csvReader.ReadAll()
	if err != nil {
		log.Fatal("Unable to parse file as CSV fir"+fname, err)
	}

	// iHeader, _ := strconv.Atoi(header)
	// iCoords, _ := strconv.Atoi(coords)

	// return iHeader, iCoords
	return header, coords
}
