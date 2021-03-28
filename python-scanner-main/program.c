

float main() {
	int lower_bound = 0;
	int upper_bound = 10;
	int sum = 0;
	float average;

while (lower_bound <= upper_bound) {
	if ((lower_bound % 2) != 0) {
		sum += lower_bound;
}

lower_bound += 1;
}

average = sum / (upper_bound - lower_bound);

return average; 
}
