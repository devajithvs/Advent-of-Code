package helperfunctions

import (
	"strconv"
)

func toInt(num string) int {
	result, _ :=strconv.Atoi(num)
	return result
}