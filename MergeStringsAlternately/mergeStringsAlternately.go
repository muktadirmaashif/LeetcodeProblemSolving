func mergeAlternately(w1 string, w2 string) string {
	res := ""
	max_len := max(len(w1), len(w2))
	w1_arr := strings.Split(w1, "")
	w2_arr := strings.Split(w2, "")

	for i := 0; i < max_len; i++ {
		if i < len(w1) {
			res += w1_arr[i]
		}
		if i < len(w2) {
			res += w2_arr[i]
		}
	}
	return res
}
