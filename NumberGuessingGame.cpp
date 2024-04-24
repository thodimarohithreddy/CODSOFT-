#include <iostream>
#include <cstdlib>
#include <ctime>
#include <limits>
using namespace std;
int main() 
{
    srand(time(0));
    int secretNumber = rand() % 100 + 1;
    int guess;
    while (true) {
        cout << "Enter your guess (between 1 and 100): ";
        cin >> guess;
        if (cin.fail()) {
            cout << "Invalid input. Please enter a valid number." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }  
        if (guess > secretNumber) {
            cout << "Too high! Try again." << endl;
        } else if (guess < secretNumber) {
            cout << "Too low! Try again." << endl;
        } else {
            cout << "Congratulations! You guessed the correct number." << endl;
            break; 
        }
    }
    return 0;
}
