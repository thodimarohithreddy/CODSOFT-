#include <iostream>
using namespace std;
int main() {
    double num1, num2, result;
    char operation;

    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    cout << "Choose operation (+, -, *, /): ";
    cin >> operation;

    result = (operation == '+') ? num1 + num2 :
             (operation == '-') ? num1 - num2 :
             (operation == '*') ? num1 * num2 :
             (operation == '/' && num2 != 0) ? num1 / num2 :
             (cout << "Error! Invalid operation or division by zero." << endl, 0);

    if (operation != '/' || num2 != 0)
        cout << "Result: " << result << endl;

    return 0;
}
