<<<<<<< HEAD
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

struct Question {
    string question;
    string a;
    string b;
    string c;
    char corectAnswer;
};

struct Questionnaire {
    Question* questions;
    int length;
};

Questionnaire * buildQuestionnaire(string path){
    ifstream file; 
    string line;
    int pocet = 0;
    file.open(path);
    while (getline(file,line)){
        pocet++;
        //cout<<"pocet radku:"<<pocet<<endl;
    }
    file.close();
    Questionnaire* quiz = new Questionnaire {new Question[pocet],0};
    stringstream ss;
    file.open(path);
    while (getline(file,line)){
        //cout<<line<<endl;
        ss.clear();
        ss<<line;
        getline(ss, quiz->questions[quiz->length].question, ';');
        getline(ss, quiz->questions[quiz->length].a, ';');
        getline(ss, quiz->questions[quiz->length].b, ';');
        getline(ss, quiz->questions[quiz->length].c, ';');
        ss >> quiz->questions[quiz->length].corectAnswer;
        quiz->length++;
    }
    file.close();

    return quiz;
}
int runQuestionnaire(Questionnaire * quiz){
    char odpoved;
    int score=0;
    for(int i=0;i<quiz->length;i++){
        cout<<quiz->questions[i].question<<endl<<"a)"<<quiz->questions[i].a<<endl<<"b)"<<quiz->questions[i].b<<endl<<"c)"<<quiz->questions[i].c<<endl;
        cin>>odpoved;
        if (odpoved == quiz->questions[i].corectAnswer){
            cout<<"spravna odpoved"<<endl;
            score++;
        }
        else{
            cout<<"spatna odpoved"<<endl;
        }
    };
    return score;
}
void reallocate(Question** old_arr, int old_size, int new_size){

}
void delQuestions(Questionnaire* quiz){
    
}

int main(){
    string path;
    cout << "Zadej cestu k souboru s otazkami (název souboru): ";
    cin >> path;
    Questionnaire * quiz = buildQuestionnaire(path);
    int score = runQuestionnaire(quiz);
    cout<< "Tve skore je: " << score;
    //delQuestions(quiz);
    //delete quiz;
    return 0;
}
=======
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

struct Question {
    string question;
    string a;
    string b;
    string c;
    char corectAnswer;
};

struct Questionnaire {
    Question* questions;
    int length;
};

Questionnaire * buildQuestionnaire(string path){
    ifstream file; 
    string line;
    int pocet = 0;
    file.open(path);
    while (getline(file,line)){
        pocet++;
        //cout<<"pocet radku:"<<pocet<<endl;
    }
    file.close();
    Questionnaire* quiz = new Questionnaire {new Question[pocet],0};
    stringstream ss;
    file.open(path);
    while (getline(file,line)){
        //cout<<line<<endl;
        ss.clear();
        ss<<line;
        getline(ss, quiz->questions[quiz->length].question, ';');
        getline(ss, quiz->questions[quiz->length].a, ';');
        getline(ss, quiz->questions[quiz->length].b, ';');
        getline(ss, quiz->questions[quiz->length].c, ';');
        ss >> quiz->questions[quiz->length].corectAnswer;
        quiz->length++;
    }
    file.close();

    return quiz;
}
int runQuestionnaire(Questionnaire * quiz){
    char odpoved;
    int score=0;
    for(int i=0;i<quiz->length;i++){
        cout<<quiz->questions[i].question<<endl<<"a)"<<quiz->questions[i].a<<endl<<"b)"<<quiz->questions[i].b<<endl<<"c)"<<quiz->questions[i].c<<endl;
        cin>>odpoved;
        if (odpoved == quiz->questions[i].corectAnswer){
            cout<<"spravna odpoved"<<endl;
            score++;
        }
        else{
            cout<<"spatna odpoved"<<endl;
        }
    };
    return score;
}
void reallocate(Question** old_arr, int old_size, int new_size){

}
void delQuestions(Questionnaire* quiz){
    
}

int main(){
    string path;
    cout << "Zadej cestu k souboru s otazkami (název souboru): ";
    cin >> path;
    Questionnaire * quiz = buildQuestionnaire(path);
    int score = runQuestionnaire(quiz);
    cout<< "Tve skore je: " << score;
    //delQuestions(quiz);
    //delete quiz;
    return 0;
}
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
