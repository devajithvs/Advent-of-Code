package main

import (
	"fmt"
	"path/filepath"
	"github.com/devajithvs/Advent-of-Code/golang/utils/filehandler"
	"time"
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
	fmt.Println(inputValue)
	return ""
}

func Solution2(filename string) int {
	// inputPath, _ := filepath.Abs(filename)
	// inputValue := filehandler.ReadLines(inputPath)
	return 0
}
