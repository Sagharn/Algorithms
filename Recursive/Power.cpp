//first recursive 

#include <iostream>
using namespace std;
int power(int b, int e) {
    if (e == 0)
        return 1;
    return b * power(b, e - 1);
}

int main() {
    int b, e;
    cin >> b >> e;
    int result = power(b, e);
    cout<< result << endl;

    return 0;
}


