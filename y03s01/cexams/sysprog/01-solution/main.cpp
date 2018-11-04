#include <random>
#include <iostream>

#define ARR_SIZE 10

int arr_rand_fill(int *a, const size_t a_size);
int arr_print(const int *a, const size_t a_size);
int count_pairs_with_opposite_signs(const int *a, const size_t a_size);

int main(void)
{
	int a[ARR_SIZE];
	size_t a_size = ARR_SIZE;

	arr_rand_fill(a, a_size);

	arr_print(a, a_size);

	std::cout << '\n' << count_pairs_with_opposite_signs(a, a_size) << '\n';

//	puts("Hello");

	return 0;
}

int arr_rand_fill(int *a, size_t a_size)
{
	size_t elcnt = 0;

	// initialize rng
	std::mt19937 rng;
	rng.seed(std::random_device()());

	// create a uniform distribution from RNG
	std::uniform_int_distribution<std::mt19937::result_type> m50to50(-50, 50);

	// fill the array
	for (size_t i = 0; i < a_size; i++) {
		a[i] = m50to50(rng);
		++elcnt;
	}

	return elcnt;
}

int arr_print(const int *a, const size_t a_size)
{
	for (size_t i = 0; i < a_size; i++)
		std::cout << a[i] << ' ';

	return 0;
}

int count_pairs_with_opposite_signs(const int *a, const size_t a_size)
{
	int pair_cnt = 0;

	for (size_t i = 0; i < a_size - 1; i++) {
		// check if two neighbouring elements have opposite signs
		if ((a[i] < 0 && a[i+1] >= 0) || (a[i] >= 0  && a[i+1] < 0)) {
			pair_cnt++;
		}
	}

	return pair_cnt;
}
