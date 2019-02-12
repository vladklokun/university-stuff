/*
 * lcg-test-builtin.cpp
 *
 * Имитационное моделирование, лаба №1.
 * Программа для моделирования линейно-конгруэнтного генератора.
 *
 * Написана на C++11, собирать так:
 * cxx -std=c++11 lcg-test-builtin.cpp
 * Где cxx — компилятор языка C++, вроде clang, gcc, cl.exe.
 */

#include <random> // std::linear_congruential_engine, std::uniform_real_distribution, std::uniform_int_distribution
#include <iostream> // std::cout
#include <vector> // std::vector
#include <numeric> // std::accumulate
#include <cmath> // std::sqrt

#define MINSTD_MODULUS 0x7FFFFFFF
#define MINSTD_MULTIPLIER 48271
#define MINSTD_INCREMENT 0

double calc_freq(const std::vector<double>& seq, const double a, const double b);

double calc_pearson_chi_sq(const std::vector<double>& seq);
std::vector<int> histogram(const std::vector<double>& seq);

double calc_mean(const std::vector<double>& seq);
double calc_variance(const std::vector<double>& seq);
double calc_stdev(const std::vector<double>& seq);

int main(void)
{
	// Задание 1: создаём модель линейного конгруэнтного генератора
	// Открываем системный генератор, чтобы получить 
	// хорошее начальное значение
	std::random_device rd;
	// Создаём наш генератор — lcg — со значениями, соответствующими
	// параметрам MINSTD (Park, Miller)
	std::linear_congruential_engine<uint_fast32_t, 
		                        MINSTD_MULTIPLIER, 
		                        MINSTD_INCREMENT, 
					MINSTD_MODULUS> lcg;

	// Считываем качественное случайное значение из системного генератора
	// и делаем его начальным значением для нашего генератора 
	lcg.seed(rd());

	// Создаём распределение от 0.0 до 1.0
	// Чтобы получить случайное число в этом интервале, нужно запустить 
	// генератор случайных чисел внутри распределения. 
	// Например, так:
	// distr_0to1(lcg)
	std::uniform_real_distribution<double> distr_0to1(0.0, 1.0);

	// Создаём вектор, который будет хранить последовательность случайных чисел. 
	std::vector<double> random_seq;
	// Записываем в вектор 1000 случайных чисел от 0.0 до 1.0
	for (size_t i = 0; i < 10000; ++i) {
		random_seq.push_back(distr_0to1(lcg));
	}

	// Выводим первые 10 значений созданной последовательности
	std::cout << "\nTask 1. Random sequence on [0.0; 1.0), first 10 values: \n(";
	for (size_t i = 0; i < 10; ++i)
		std::cout << random_seq[i] << "; ";
	std::cout << ") " << std::endl;

	// Задание 2.1: вычисляем значения критерия Пирсона
	std::cout << "\nTask 2.1. PRNG quality: Pearson's chi-squared test\n";
	double chi_sq = calc_pearson_chi_sq(random_seq);
	std::cout << "chi^2 = " << chi_sq << std::endl;

	// Задание 2.2: частотный тест
	std::cout << "\nTask 2.2. PRNG quality: Frequency test\n";
	double freq = calc_freq(random_seq, 0.2113, 0.7887);
	std::cout << "Freq = " << freq << std::endl;

	// Задание 3.1: считаем математическое ожидание
	std::cout << "\nTask 3.1. Stat parameters: mean\n";
	double mean = calc_mean(random_seq);
	std::cout << "Mean = " << mean << std::endl;

	// Задание 3.2: считаем дисперсию
	std::cout << "\nTask 3.2. Stat parameters: variance\n";
	double variance = calc_variance(random_seq);
	std::cout << "Variance = " << variance << std::endl;

	// Задание 3.1: считаем среднеквадратическое отклонение
	std::cout << "\nTask 3.3. Stat parameters: standard deviation\n";
	double stdev = calc_stdev(random_seq);
	std::cout << "Stdev = " << stdev << std::endl;

	// Задание 4: генерируем случайные числа на интервале (a, b)
	std::cout << "\nTask 4. Rand on [a, b) range\n";
	int_fast32_t a = 15, b = 623;

	// Создаём равномерное распределение на интервале [a, b)
	std::uniform_int_distribution<> dist_ab(a, b);

	// Пошагово выводим 15 случайных чисел, обработанных 
	// созданным распределением dist_ab
	std::cout << "Random sequence on [a, b): \n(";
	for (size_t i = 0; i < 15; ++i)
		std::cout << dist_ab(lcg) << "; ";
	std::cout << ") " << std::endl;

	return 0;
}

/* calc_pearson_chi_sq — высчитывает значение критерия Пирсона
 *
 * Параметры:
 * seq — последовательность
 *
 * Возвращает:
 * double — значение критерия Пирсона
 */
double calc_pearson_chi_sq(const std::vector<double>& seq)
{
	std::vector<int> freq = histogram(seq);

	// N = длина последовательности случайных чисел
	double N = static_cast<double>(seq.size());
	// m = количество подинтервалов, на которые делился общий интервал
	double m = static_cast<double>(freq.size());

	// Вычисляем сумму по формуле \sum_{i = 1}^{m} (x - N/m)^2
	double tmp_sum = 0.0;
	for (const auto& x : freq) {
		tmp_sum += pow(x - N/m, 2);
	}

	// Чтобы получить хи-квадрат, умножаем сумму на m / N
	double chi_squared = m / N * tmp_sum;

	return chi_squared;
}

/* histogram — строит гистограмму заданой последовательности
 *
 * Параметры:
 * seq — последовательность
 *
 * Возвращает:
 * std::vector<int> — вектор, каждый элемент которого — 
 * частота попадания элемента в данный интервал
 */
std::vector<int> histogram(const std::vector<double>& seq)
{

	// Границы интервала, в который попадают 
	// возможные значения последовательности. По условию [0.0; 1.0)
	double a = 0.0;
	double b = 1.0;

	size_t bins = 10; // всего 10 подинтервалов

	double z = (b - a) / static_cast<double> bins; // вычисляем размер каждого интервала

	// Создаём вектор размером в количество подинтервалов,
	// где каждый элемент будет хранить количество раз, сколько чисел 
	// из случайной последовательности, попали в интервал [a, b)
	std::vector<int> freq(bins);
	
	// Для каждого интервала с номером j
	for (size_t j = 0; j < bins; ++j) {
		// Для каждого числа x во всей последовательности seq
		for (const auto& x : seq) {
			// Проверить, вписывается ли число в текущий интервал j
			if ( (x >= (a + z * j ) ) 
			     && ( x < (a + z * (j + 1) ) ) ) {
				// увеличить счётчик чисел, попавших в интервал
				++freq[j];
			}
		}
	}

	return freq;
}

/* 
 * calc_freq — высчитывает, сколько процентов чисел последовательности 
 * попали в интервал (a, b)
 *
 * Параметры:
 * seq — последовательность
 * a, b — границы интервала
 *
 * Возвращает:
 * double — процент чисел, попавших в интервал
 */
double calc_freq(const std::vector<double>& seq, const double a, const double b)
{
	size_t cnt = 0;

	// Для каждого числа x в последовательности seq
	for (const auto& x : seq) {
		// Если a < x < b, то есть число вписывается в интервал
		if ( (x > a) && (x < b) )
			// увеличить счётчик чисел, попавших в интервал
			++cnt; 
	}

	double freq = static_cast<double>(cnt) / static_cast<double>(seq.size());

	return freq;
}

/*
 * calc_mean — вычисляет значения математического ожидания последовательности
 *
 * Параметры:
 * seq — последовательность
 *
 * Возвращает:
 * double — значение математического ожидания
 */
double calc_mean(const std::vector<double>& seq)
{
	// Суммируем все элементы seq и записываем результат в el_sum
	// 0.0 — начальное значение суммы
	double el_sum = std::accumulate(seq.begin(), seq.end(), 0.0);

	// На основе суммы считаем математическое ожидание
	double mean = el_sum / static_cast<double>(seq.size());

	return mean;
}

/*
 * calc_variance — вычисляет значения дисперсии последовательности
 *
 * Параметры:
 * seq — последовательность
 *
 * Возвращает:
 * double — значение дисперсии
 */
double calc_variance(const std::vector<double>& seq)
{
	double mean = calc_mean(seq);

	// Считаем сумму всех членов, где каждый член — (x - mean)^2
	double temp_sum = 0.0;
	for (const auto& x : seq)
		temp_sum += pow( (x - mean), 2);

	double variance = temp_sum / static_cast<double>(seq.size());

	return variance;
}

/*
 * calc_mean — вычисляет значения среднеквадратического отклонения 
 * последовательности
 *
 * Параметры:
 * seq — последовательность
 *
 * Возвращает:
 * double — значение среднеквадратического отклонения
 */
double calc_stdev(const std::vector<double>& seq)
{
	return std::sqrt(calc_variance(seq));
}

