#include <typeinfo>
#include <iostream>
using namespace std;
int main() {
    int i;
    cin >> i;
    cout << i << " " << typeid(i).name() << '\n';
    double n = (double)i;
    cout << n << " " << typeid(n).name() << '\n';

    return 0;
    system("Pause");
}