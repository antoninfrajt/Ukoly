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
}