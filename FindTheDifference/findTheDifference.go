package main

import "fmt"

func findTheDifference(s string, t string) byte {
	s_AsciSum := rune(0)
	for _, val := range s {
		s_AsciSum += val
	}
	t_AsciSum := rune(0)
	for _, val := range t {
		t_AsciSum += val
	}
	res := t_AsciSum - s_AsciSum
	return byte(res)
}

func main() {
	var s, t string

	s = "ab"
	t = "abc"
	fmt.Println(findTheDifference(s, t))

	s = "a"
	t = "aa"
	fmt.Println(findTheDifference(s, t))

	s = "ae"
	t = "aea"
	fmt.Println(findTheDifference(s, t))


}
