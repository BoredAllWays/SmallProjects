//Pranav Raja
#include <iostream>
#include <string>
#include <climits>
#include <cmath>
using std::cout;
using std::cin;
using std::endl;


void Kilometers()
{
    long long x;
    cout << "How many miles did you run?: \n";
    cin >> x;
    long double calculation = x * 1.60934;
    cout << "You ran " << x << " Miles " << "and " << calculation << " kilometers." << endl;
}

void bmi()
{
    double height;
    double weight;
    cout << "What is your height in inches? \n";
    cin >> height;
    double height_m = height / 39.37;
    cout << "height in meters: " << height_m << endl;
    cout << "What is your weight in pounds \n";
    cin >> weight;
    double weight_m = weight / 2.205;
    cout << "Weight in kilograms: " << weight_m << endl;
    double bmi = weight_m / (pow(height_m, 2));
    cout << "bmi: " << bmi << endl;
    if (bmi > 14.5 && bmi < 25)
    {
        cout << "You are fine, HOOOOOOOORAY" << endl;
    }
    else if (bmi < 14.5)
    {
        cout << "You are underweight, eat some burgers" << endl;
    }
    else
    {
        cout << "You are overweight, try running" << endl;
    }
}


int main()
{
    Kilometers();
    bmi();
}