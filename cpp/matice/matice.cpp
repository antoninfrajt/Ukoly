#include <iostream>
#include <vector>
#include <random>
using namespace std;

vector<vector<int>> NovaMatice(int v, int s){
    vector<vector<int>> matice;
    vector<int> doc;
    random_device generator;
    for (int i = 0;i < v;i++){
        for (int j = 0;j< s;j++){
            doc.push_back(generator() %10 );
        }
        matice.push_back(doc);
        doc.clear();
    }
    return matice;
}

void VytiskniMatici(vector<vector<int>> m){
    for (vector<int> i : m){
        for (int j : i){
            cout<<j<<" ";
        }
        cout<<endl;
    }
}
vector<vector<int>> Operace(vector<vector<int>> m, vector<vector<int>> n, char o){
    vector<vector<int>> v;
    vector<int> doc;
    switch (o)
    {
    case '+':
        cout<<"scitam"<<endl;
        if (m.size() == n.size() && m[0].size() == n[0].size()){
            for (int i = 0;i<m.size();i++){
                for (int j = 0; j<m[i].size(); j++){
                    int soucet;
                    soucet = m[i][j] + n[i][j];
                    doc.push_back(soucet);
                }
                v.push_back(doc);
                doc.clear();
            }
            cout<<"soucet je:"<<endl;
        }
        else{
            cout<<"matice nejde scitat"<<endl;
        }
        break;
    case '-':
        cout<<"odcitam"<<endl;
        if (m.size() == n.size() && m[0].size() == n[0].size()){
            for (int i = 0;i<m.size();i++){
                for (int j = 0; j<m[i].size(); j++){
                    int soucet;
                    soucet = m[i][j] - n[i][j];
                    doc.push_back(soucet);
                }
                v.push_back(doc);
                doc.clear();
            }
            cout<<"rozdil je:"<<endl;
        }
        else{
            cout<<"matice nejde odcitat"<<endl;
        }
        break;
    case '*':
        cout<<"nasobim"<<endl;
        if (m[0].size() == n.size()){
            for (int i = 0;i<m.size();i++){
                for (int j = 0; j<n[0].size(); j++){
                    int soucet;
                    soucet = 0;
                    for (int k = 0; k<m[0].size();k++)
                    soucet += m[i][k] * n[k][j];
                    doc.push_back(soucet);
                }
                v.push_back(doc);
                doc.clear();
            }
            cout<<"soucin je:"<<endl;
        }
        else{
            cout<<"matice nejde nasobit"<<endl;
        }
        break;
        
    default:
        cout<<"nic"<<endl;
        return v;
        break;
    }
    return v;
}

int main()
{
    int vyska;
    int sirka;
    cout<<"Zadejte vysku a sirku 1. matice:"<<endl;
    cin>>vyska>>sirka;
    vector<vector<int>> maticejedna = NovaMatice(vyska,sirka);
    VytiskniMatici(maticejedna);
    cout<<"Zadejte vysku a sirku 2. matice:"<<endl;
    cin>>vyska>>sirka;
    vector<vector<int>> maticedva = NovaMatice(vyska,sirka);
    VytiskniMatici(maticedva);
    cout<<"vyberte operaci(scitani +, odcitani -, nasobeni *):";
    char op;
    cin>>op;
    vector<vector<int>> vysledek = Operace(maticejedna,maticedva, op);
    VytiskniMatici(vysledek);
}
