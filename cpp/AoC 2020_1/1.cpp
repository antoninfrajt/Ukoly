#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;
int hledejDva(vector<int> v){
    for(int c : v)
        //cout<<c<<endl;
    for(int z : v){
        for(int y : v){
            for(int x : v){
                int soucet;
                soucet = y+x+z;
                //cout<<soucet<<endl;
                if ( soucet == 2020){
                    cout<<"cisla"<<z<<","<<y<<"a"<<x<<endl;
                    return z*y*x;
                }
            }
        }
    }
    return 0;   
}

int hledej(vector<int> v){
    for(int c : v)
        //cout<<c<<endl;
    for(int y : v){
        for(int x : v){
            int soucet;
            soucet = y+x;
            cout<<soucet<<endl;
            if ( soucet == 2020){
                cout<<"cisla"<<y<<"a"<<x<<endl;
                return y*x;
            }
        }
    }
    return 0;
}

void parse(string s){
    ifstream file;
    string line;
    stringstream ss;
    vector<int> cisla;
    int cislo;
    file.open(s);
    while (getline(file,line)){
        cislo = stoi(line);
        cisla.push_back(cislo);
    }
    file.close();
    int vysledek;
    vysledek = hledej(cisla);
    cout<<"task 1:";
    cout<<vysledek<<endl;
    vysledek = hledejDva(cisla);
    cout<<"task 2:"<<vysledek;
}

int main(){
    parse("input.txt");
}

