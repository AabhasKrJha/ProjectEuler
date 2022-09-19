#include <iostream>
using namespace std;

bool isTriangle(int a, int b, int c){
    if ((a + b > c) && (a +  c > b) && (b + c > a)){
        return true;
    }
    return false;
}

bool isTriplet(int a, int b, int c){
    if (a*a + b*b == c*c){
        return true;
    }
    return false;
}

int main(){

    for (int a = 1; a < 1001; a++){
        for (int b = 1; b < 1001; b++){
            for (int c = 1; c < 1001; c++){
                if (isTriangle(a, b, c) && isTriplet(a, b, c) && (a + b + c == 1000)){
                    cout << a*b*c << endl;
                }
            }
        }
    }
    return 0;
}