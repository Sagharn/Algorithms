// time complexity : log n
#include <iostream>
using namespace std;

double power(double x, int n) 
{
    if (n == 0)
        return 1;
    
    double half = power(x, n / 2);
    
    if (n % 2 == 0)
        return half * half;
    else
        return x * half * half;
}


int main() 
{
    double base;
    int exponent;
    
    cin >> base;
    
    cin >> exponent;
    
    double result = power(base, exponent);
    
    cout<< result << endl;
    
    return 0;
}
