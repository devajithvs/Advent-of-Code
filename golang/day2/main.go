package main

import (
	"fmt"
	"path/filepath"
	"github.com/devajithvs/Advent-of-Code/golang/utils/filehandler"
	"github.com/devajithvs/Advent-of-Code/golang/utils/helperfunctions"
	"time"
	"strings"
	"strconv"
)

func main() {
	fmt.Println("Question 1")
	
	start := time.Now()
	fmt.Println(Solution1("input.txt"))
	elapsed := time.Since(start)
	fmt.Printf("Execution took %s\n", elapsed)

	fmt.Println("\nQuestion 2")
	
	start = time.Now()
	fmt.Println(Solution2("input.txt"))
	elapsed = time.Since(start)
	fmt.Printf("Execution took %s\n", elapsed)
}

func Solution1(filename string) int {
	inputPath, _ := filepath.Abs(filename)
	inputValue := filehandler.ReadLines(inputPath)

	horizontal_pos := 0
	depth := 0
	for _, line := range(inputValue) {
		value := strings.Split(line, " ")
		if value[0] == "forward" {
			horizontal_pos = horizontal_pos + commons.toInt(value[1])
		} else if value[0] == "down" {
			depth = depth + commons.toInt(value[1])
		} else if value[0] == "up" {
			depth = depth - commons.toInt(value[1])
		}
	}
		
	// fmt.Println(horizontal_pos*depth)
	return horizontal_pos*depth
}

func Solution2(filename string) int {
	inputPath, _ := filepath.Abs(filename)
	inputValue := filehandler.ReadLines(inputPath)

	aim := 0
	
	horizontal_pos := 0
	depth := 0
	for _, line := range(inputValue) {
		value := strings.Split(line, " ")
		if value[0] == "forward" {
			horizontal_pos = horizontal_pos + commons.toInt(value[1])
			depth = depth + aim * commons.toInt(value[1])
		} else if value[0] == "down" {
			aim = aim + commons.toInt(value[1])
		} else if value[0] == "up" {
			aim = aim - commons.toInt(value[1])
		}
	}
		
	// fmt.Println(horizontal_pos*depth)
	return horizontal_pos*depth
}
