<<<<<<< HEAD
#include <iostream>
using namespace std;
void koruna(int v){
    for(int i=1;i <(v+1);i++){
        int m = v-i;
        int z = i+(i-1);
        for(int j=1;j<=m;j++){
            cout<<" ";
        }
        for(int j=1;j<=z;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
void kmen(int v,int k,int vk){
    for (int i=0;i<vk;i++){
        int m = v-(k/2)-1;
        for (int j=0;j<m;j++){
            cout<<" ";
        }
        for (int j=0;j<k;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
int main(){
    int vyska = 4;
    int sirka = 4;
    int VyskaK = 2;
    cout<<"Zadejte vysku koruny a sirku a vysku kmene:";
    cin>>vyska>>sirka>>VyskaK;
    koruna(vyska);
    kmen(vyska,sirka,VyskaK);
    return 0;
=======
#include <iostream>
using namespace std;
void koruna(int v){
    for(int i=1;i <(v+1);i++){
        int m = v-i;
        int z = i+(i-1);
        for(int j=1;j<=m;j++){
            cout<<" ";
        }
        for(int j=1;j<=z;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
void kmen(int v,int k,int vk){
    for (int i=0;i<vk;i++){
        int m = v-(k/2)-1;
        for (int j=0;j<m;j++){
            cout<<" ";
        }
        for (int j=0;j<k;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
int main(){
    int vyska = 4;
    int sirka = 4;
    int VyskaK = 2;
    cout<<"Zadejte vysku koruny a sirku a vysku kmene:";
    cin>>vyska>>sirka>>VyskaK;
    koruna(vyska);
    kmen(vyska,sirka,VyskaK);
    return 0;
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
}