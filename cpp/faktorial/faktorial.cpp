#include <iostream>
using namespace std;

int main(){
    int cislo;
    cout<<"zadejte cislo:"<<endl;
    cin>>cislo;
    int fakt = 1;
    for (int i = 1;i <=cislo;i++){
        fakt *= i;
    }
    cout<<fakt;
    return 0;
}
