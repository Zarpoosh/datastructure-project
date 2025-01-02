/*
برنامه‌ای بنویسید که از کاربر یک ماتریس مربعی با اندازه 
𝑛
×
𝑛
n×n بگیرد و موارد زیر را محاسبه کند:

جمع اعداد ستون آخر.
ضرب اعداد سطر اول.
کمینه مقدار موجود در قطر اصلی ماتریس.
*/


#include <iostream>
using namespace std;

int main() {
    double x[10][10], sum = 0, product = 1, minDiagonal;
    int n, i, j;

    cout << "Enter the size of the matrix (n): ";
    cin >> n;

    cout << "Enter the elements of the matrix:" << endl;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            cin >> x[i][j];
        }
    }

    minDiagonal = x[0][0]; // Initialize minimum value on the main diagonal

    for (i = 0; i < n; i++) {
        sum += x[i][n - 1]; // Sum of the last column
        product *= x[0][i]; // Product of the first row
        if (x[i][i] < minDiagonal) {
            minDiagonal = x[i][i]; // Find the minimum value on the main diagonal
        }
    }

    cout << "Sum of the last column: " << sum << endl;
    cout << "Product of the first row: " << product << endl;
    cout << "Minimum value on the main diagonal: " << minDiagonal << endl;

    return 0;
}
