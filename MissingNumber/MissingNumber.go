func missingNumber(nums []int) int {
	sort.Ints(nums)
	// taking care of 0. if 0 missing, return 0
	if nums[0] != 0 {
		return 0
	}
	// once 0 got taken care of, start with 1.
	// iterate over the legth, if current element is not equal to the
	// previous element, it's missing. as the length = the last index + 1
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1]+1 {
			return nums[i-1] + 1
		}
	}
	// in case of [0,1] where no item is missing, means next to the largest number(which is 1)
	// will be returned. which will be 2
	return nums[len(nums)-1] + 1
}

