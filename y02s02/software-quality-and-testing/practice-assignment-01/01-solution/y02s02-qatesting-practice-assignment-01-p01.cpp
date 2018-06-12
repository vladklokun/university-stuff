#include <cstdlib>   // EXIT_FAILURE
#include <iostream>  // std::cout, std::cerr
#include <string>    // std::string, std::stod
#include <exception> // std::exception
#include <vector>    // std::vector

enum class TriType {
	INVALID     = -1,
	SCALENE     = 0,
	ISOSCELES   = 1,
	EQUILATERAL = 2,
};

TriType gettritype(const double A, const double B, const double C);
bool isvalidtriangle(const double A, const double B, const double C);

int main(int argc, char* argv[])
{
	// check if a sufficient number of arguments was passed
	if (argc != 4) {
		std::cerr << "Incorrect number of arguments!\n"
			<< "Usage: " 
			<< argv[0]
			<< " %lf %lf %lf\n";
		
		return EXIT_FAILURE;
	}

	std::vector<double> tri;

	// start at 1 since relevant arguments start at 1 in argv[]
	for (std::size_t i = 1; i < 4; i++) {
		try {
			std::string strA(argv[i]);
			tri.push_back(std::stod(strA));
		} catch (std::exception& e) {
			std::cerr << "Unable to convert to double: "
				<< '\"' << argv[i] << "\"\n";
			return EXIT_FAILURE;
		};
	}

	switch (gettritype(tri[0], tri[1], tri[2])) {
		case TriType::SCALENE:
			std::cout << "A scalene triangle.\n";
			break;
		case TriType::ISOSCELES:
			std::cout << "An isosceles triangle.\n";
			break;
		case TriType::EQUILATERAL:
			std::cout << "An equilateral triangle.\n";
			break;
		default:
			std::cout << "Not a valid triangle.\n";
			break;
	}

	return 0;
}

/*
 * Checks the type of a given triangle
 */
TriType gettritype(const double A, const double B, const double C)
{
	// assume a scalene triangle
	TriType type = TriType::SCALENE;

	if (!isvalidtriangle(A, B, C))
		return TriType::INVALID;

	// check if any TWO of the sides are equal
	if ((A == B) || (A == C) || (B == C)) {
		type = TriType::ISOSCELES;
		// check if ALL the sides are equal
		if ((A == B) && (B == C)) {
			type = TriType::EQUILATERAL;
		}
	}

	return type;
}

bool isvalidtriangle(const double A, const double B, const double C)
{
	bool isvalid = true;

	// check if all triangle sides are positive
	if (A <= 0 || B <= 0 || C <= 0)
		isvalid = false;

	// check if given sizes make a valid triangle
	if (   ((A + B) <= C)
	    || ((A + C) <= B)
	    || ((B + C) <= A) ) {
		isvalid = false;
	}

	return isvalid;
}

