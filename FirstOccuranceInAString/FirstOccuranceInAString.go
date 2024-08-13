package main

import "fmt"

// // Using slicing, T.C. O(n)
// func strStr(haystack string, needle string) int {
// 	nL := len(needle)
// 	hL := len(haystack)
// 	for i := 0; i < (hL - nL + 1); i++ {
// 		sliced := haystack[i : nL+i]
// 		if sliced == needle {
// 			return i
// 		}
// 	}
// 	return -1
// }

func strStr(haystack string, needle string) int {
	var res int
	np := 0
	for hp := 0; hp < len(haystack)-len(needle)+4; hp++ {
		if np < len(needle)-1 {
			if needle[np] != haystack[hp] {
				np = 0

			} else {
				np += 1
			}
		}
	}
	return res
}

func main() {
	var n, h string

	h = "sadbutsad"
	n = "sad"
	fmt.Println(h, n, strStr(h, n))

	h = "sadbutsalt"
	n = "sad"
	fmt.Println(h, n, strStr(h, n))

	h = "butsadbut"
	n = "sad"
	fmt.Println(h, n, strStr(h, n))

	h = "nothingbuthappy"
	n = "sad"
	fmt.Println(h, n, strStr(h, n))

	h = "saltychill"
	n = "sad"
	fmt.Println(h, n, strStr(h, n))
}
