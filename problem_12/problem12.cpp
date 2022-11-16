#include <iostream>
using namespace std;

bool HighlyDivisibleTriangularNumber(long num){
    int factor_count = 0;
    for (long divisior = 1; divisior <= num / 2; divisior++){
        if (num % divisior == 0){
            factor_count += 1;
        }
    }
    if (factor_count > 500){
        return true;
    } else {
        return false;
    }
}

int main(int argc, char const *argv[])
{
    bool found = false;
    long num = 1;
    while (!found){        
        long triangular = num * (num + 1) / 2;
        cout << "NAH " << num << " : " << triangular << endl;
        if (HighlyDivisibleTriangularNumber(triangular)){
            cout << triangular << endl;
            found = true;
        }
        num += 1;
    }
    return 0;
}
