#include "y03s01-syssoft-lab-04-01-mathfunslib.h"
#include <stdexcept>
#include <cmath> // log, exp, sqrt

namespace MathFuncs
{
	double MyMath::add(double a, double b)
	{
		return a + b;
	}

	double MyMath::substract(double a, double b)
	{
		return a - b;
	}
	
	double MyMath::multiply(double a, double b)
	{
		return a * b;
	}
	
	double MyMath::divide(double a, double b)
	{
		if (b == 0)
			throw new std::invalid_argument("b cannot be zero!");
		return a / b;
	}

	double MyMath::log(double a, double b)
	{
		// log_{a}(b) = ln(b) / ln(a)
		return std::log(b) / std::log(a);
	}

	double MyMath::pow(double a, double b)
	{
		return std::pow(a, b);
	}
}