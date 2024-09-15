#include <typeinfo>
#include <iostream>
using namespace std;
int main(){
    int i;
    cin >> i;
    cout << i  << endl << typeid(i).name() << endl;
    double n = (double)i;
    cout << n << endl << typeid(n).name() << endl;

    return 0;
    system("Pause");
}