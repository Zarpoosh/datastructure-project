#include <iostream>
using namespace std;

int main() {
    double x, m = 1;
    int i;

    cout << "Enter 100 numbers to calculate their product:" << endl;
    for (i = 0; i < 100; i++) {
        cin >> x;
        m *= x;
    }

    cout << "The product of the entered numbers is: " << m << endl;

    return 0;
}






