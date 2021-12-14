package filehandler

import (
    "fmt"
    "os"
	"bufio"
    "strconv"
)

func check(e error) {
    if e != nil {
        fmt.Println()
        panic(e)
    }
}

func ReadLines(filepath string) []string {
	file, e := os.Open(filepath)
	check(e)
	defer file.Close()

	var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
	check(scanner.Err())
    return lines
}

func ReadLinesInt(filepath string) []int {
	file, e := os.Open(filepath)
	check(e)
	defer file.Close()

	var lines []int
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        value, _ := strconv.Atoi(scanner.Text())
        lines = append(lines, value)
    }
	check(scanner.Err())
    return lines
}

func ParseInts(lines []string) []int {
	result := []int{}

    for _,line := range(lines) {
        value, _ := strconv.Atoi(line)
        result = append(result, value)
    }
    return result
}
