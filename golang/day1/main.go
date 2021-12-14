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
	inputValue := filehandler.ReadLinesInt(inputPath)

	
	counter := 0
	for index:=0; index<len(inputValue)-1; index++ {
		if inputValue[index] < inputValue[index+1] {
			counter++
		}
	}
	return counter
}

func Solution2(filename string) int {
	inputPath, _ := filepath.Abs(filename)
	inputValue := filehandler.ReadLinesInt(inputPath)

	inputValue = threeSum(inputValue)
	
	counter := 0
	for index:=0; index<len(inputValue)-1; index++ {
		if inputValue[index] < inputValue[index+1] {
			counter++
		}
	}
	return counter

}

func threeSum(inputValue []int) []int {
	threeSum := []int{}
	for index:=0; index<len(inputValue)-2; index++ {
		threeSum = append(threeSum, inputValue[index]+inputValue[index+1]+inputValue[index+2])
	}
	return threeSum
}