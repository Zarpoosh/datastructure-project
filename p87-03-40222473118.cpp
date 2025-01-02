
/*
سؤال: برنامه‌ای بنویسید که از کاربر یک ماتریس مربعی با اندازه 
𝑛
×
𝑛
n×n بگیرد و موارد زیر را محاسبه کند:

جمع اعداد قطر اصلی.
جمع اعداد قطر فرعی.
تعداد اعداد مثبت موجود در ماتریس.
*/

#include <iostream>
using namespace std;

int main() {
    double x[10][10], sumMainDiagonal = 0, sumSecondaryDiagonal = 0;
    int n, i, j, positiveCount = 0;

    cout << "Enter the size of the matrix (n): ";
    cin >> n;

    cout << "Enter the elements of the matrix:" << endl;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            cin >> x[i][j];
            if (x[i][j] > 0) {
                positiveCount++; // Count positive numbers
            }
        }
    }

    for (i = 0; i < n; i++) {
        sumMainDiagonal += x[i][i];           // Sum of the main diagonal
        sumSecondaryDiagonal += x[i][n - 1 - i]; // Sum of the secondary diagonal
    }

    cout << "Sum of the main diagonal: " << sumMainDiagonal << endl;
    cout << "Sum of the secondary diagonal: " << sumSecondaryDiagonal << endl;
    cout << "Count of positive numbers: " << positiveCount << endl;

    return 0;
}
