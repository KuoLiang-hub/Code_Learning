// Learning C++ 
// Exercise 03_02
// Classes, by Eduardo Corpeño 
/*
    similar to python and java class.
*/
#include <iostream>
#include <string>

using namespace std;

enum cow_purpose { dairy, meat, hide, pet };

//by default, class attribute are private.
class cow{
public:
    cow(string name_i, int age_i, unsigned char purpose_i){
        //constructor 
        name = name_i;
        age = age_i;
        purpose = purpose_i;
    }
    string get_name(){
        return name;
    }
    int get_age(){
        return age;
    }
    unsigned char get_purpose(){
        return purpose;
    }
    void set_age(int new_age){
        age = new_age;
    }
private:
    string name;
    int age;
    unsigned char purpose;
};

int main(){
    cow my_cow("Hildy",7,pet);
    cout << my_cow.get_name() << " is a type-" << (int)my_cow.get_purpose() << " cow." << endl;
    cout << my_cow.get_name() << " is " << my_cow.get_age() << " years old." << endl;
    return (0);
}







