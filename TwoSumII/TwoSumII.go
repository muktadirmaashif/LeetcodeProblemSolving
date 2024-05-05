func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	var res []int
	for i := 0; i < len(numbers); i++ {
		complement := numbers[left] + numbers[right]
		if complement > target {
			right--
		} else if complement < target {
			left++
		} else {
			res = append(res, left+1, right+1)
			return res
		}
	}
	return res
}   
