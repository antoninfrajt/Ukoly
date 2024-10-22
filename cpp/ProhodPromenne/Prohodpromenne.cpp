<<<<<<< HEAD
#include <iostream>
using namespace std;

void Prohod(int* a, int* b){
    *a += *b;
    *b = *a-*b;
    *a -= *b;
}

int main(){
    int a = 10;
    int b = 20;
    cout<<a<<" a "<<b<<endl;
    Prohod(&a,&b);
    cout<<a<<" a "<<b<<endl;
    return 0;
=======
#include <iostream>
using namespace std;

void Prohod(int* a, int* b){
    *a += *b;
    *b = *a-*b;
    *a -= *b;
}

int main(){
    int a = 10;
    int b = 20;
    cout<<a<<" a "<<b<<endl;
    Prohod(&a,&b);
    cout<<a<<" a "<<b<<endl;
    return 0;
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
}