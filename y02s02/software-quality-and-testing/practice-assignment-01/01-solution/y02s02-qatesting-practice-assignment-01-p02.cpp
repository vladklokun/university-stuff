#include <cstdlib>   // EXIT_FAILURE
#include <iostream>  // std::cout, std::cerr
#include <exception> // std::exception
#include <string>    // std::stoi, std::to_string

int main(int argc, char* argv[])
{
	int num = 0;

	// check if a correct number of arguments was passed
	if (argc != 2) {
		std::cerr << "Incorrect number of parameters!\n"
			<< "Usage: "
			<< argv[0]
			<< " %d\n";
		return EXIT_FAILURE;
	}

	std::string strnum(argv[1]); // get string from 1st parameter

	// check if given string is a valid int
	try {
		num = std::stoi(strnum);
	} catch (std::exception& e) {
		std::cerr << "Unable to convert to int.\n";
		return EXIT_FAILURE;
	}

	// print given number (from string) digit by digit
	for (auto c : std::to_string(num))
		std::cout << c << '\n';

	return 0;
}

