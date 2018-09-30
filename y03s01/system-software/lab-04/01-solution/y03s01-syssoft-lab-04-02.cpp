// y03s01-syssoft-lab-04-02.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "y03s01-syssoft-lab-04-01-mathfunslib.h"


int _tmain(int argc, _TCHAR* argv[])
{
	double a = 7.4;
	int    b = 99;
	
	std::cout << "a + b = "
		<< MathFuncs::MyMath::add(a, b) << '\n';
	std::cout << "a - b = "
		<< MathFuncs::MyMath::substract(a, b) << '\n';
	std::cout << "a * b = "
		<< MathFuncs::MyMath::multiply(a, b) << '\n';
	std::cout << "a / b = "
		<< MathFuncs::MyMath::divide(a, b) << '\n';
	std::cout << "log(a, b) = "
		<< MathFuncs::MyMath::log(a, b) << '\n';
	std::cout << "pow(a, b) = "
		<< MathFuncs::MyMath::pow(a, b) << '\n';
	std::getchar();
	return 0;
}

