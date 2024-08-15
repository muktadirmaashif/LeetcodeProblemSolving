package main

import (
	"fmt"
	// "strings"
)

// func ValidAnagram(s string, t string) bool {
// 	if len(s) != len(t) {
// 		return false
// 	}
// 	res := true
// 	for _, val := range t {
// 		countS := strings.Count(s, string(val))
// 		countT := strings.Count(t, string(val))
//
// 		if countS != countT {
// 			res = false
// 		}
// 	}
// 	if res {
// 		return res
// 	} else {
// 		return false
// 	}
// }

func ValidAnagram(s string, t string) bool {
	chars := make([]int, 26)
	for _, v := range s {
		i := int(v - 'a')
		chars[i]++
	}

	for _, v := range t {
		i := int(v - 'a')
		chars[i]--
	}
	fmt.Println(chars)
	for _, v := range chars {
		if v != 0 {
			return false
		}
	}
	return true
}

func main() {
	var s, t string
	s = "anagram"
	t = "nagaram"
	// ValidAnagram(s, t)
	fmt.Println(ValidAnagram(s, t))

	s = "rat"
	t = "art"
	fmt.Println(ValidAnagram(s, t))
	// ValidAnagram(s, t)
	//
	s = "rat"
	t = "car"
	// ValidAnagram(s, t)
	fmt.Println(ValidAnagram(s, t))
	//
	s = "aacc"
	t = "ccac"
	// ValidAnagram(s, t)
	fmt.Println(ValidAnagram(s, t))
	//
	s = "a"
	t = "ac"
	fmt.Println(ValidAnagram(s, t))
}
