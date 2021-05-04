#include <iostream>
#include "includes.h"
#include <time.h>
#include <string>
using namespace std;

int main() {
    cout << "Enter Error: ";
    string bruh;
    getline (cin, bruh);
    cout << "Looking for Error: " << bruh;
    Sleep(5000);
    cout << "\nCould not find Error\n";
};

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu
