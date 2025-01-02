#include <iostream>
using namespace std;

int main() {
    double x[10][10], a = 0, b = 1, c;
    int n, i, j, d = 0, e = 0;

    cout << "Enter the size of the matrix (n): ";
    cin >> n;

    cout << "Enter the elements of the matrix:" << endl;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            cin >> x[i][j];
            if (x[i][j] < 0) {
                e++; // Count negative numbers
            }
        }
    }

    c = x[0][0]; // Initialize max diagonal value

    for (i = 0; i < n; i++) {
        a += x[i][0];       // Sum of the first column
        b *= x[n - 1][i];   // Product of the last row
        if (x[i][i] > c) {
            c = x[i][i];    // Find the maximum value on the main diagonal
        }
        if (x[i][n - 1 - i] == 0) {
            d++;            // Count zeros on the secondary diagonal
        }
    }

    cout << "Sum of the first column: " << a << endl;
    cout << "Product of the last row: " << b << endl;
    cout << "Maximum value on the main diagonal: " << c << endl;
    cout << "Count of zeros on the secondary diagonal: " << d << endl;
    cout << "Count of negative numbers: " << e << endl;

    return 0;
}

