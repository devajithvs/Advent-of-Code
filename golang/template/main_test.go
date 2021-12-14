package main

import (
	"testing"
)

func TestSolution1(t *testing.T) {

	t.Run("", func(t *testing.T) {
		input := "test.txt"

		want := ""
		got := Solution1(input)

		if got != want {
			t.Errorf("got %+v want %+v given, %s and", got, want, input)
		}
	})

}

func TestSolution2(t *testing.T) {

	t.Run("", func(t *testing.T) {
		input := "test.txt"

		want := ""
		got := Solution2(input)

		if got != want {
			t.Errorf("got %+v want %+v given, %s and", got, want, input)
		}
	})

}
