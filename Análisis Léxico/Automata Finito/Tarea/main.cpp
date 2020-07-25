#include <iostream>
#include "add.h"

int main()
{
    Addition add;
    std::cout << "The sum of 3 and 4 is" << add.add(3.0,4.0) << '\n';
    return 0;
}