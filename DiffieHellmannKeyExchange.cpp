#include <iostream>
#include <cmath>
using namespace std;
int power(int a, int b, int P){
	if (b == 1){
		return a;
	}
	else{
		return (((int)pow(a, b)) % P);
	}
}
int main(){
	// P and G should be prime numbers
	int P = 23;
	int G = 9;

	int a;
	cout << "Enter Private key a for Ricky: ";
	cin >> a;
	cout << "Enter Private key b for Anamika: ";
	int b;
	cin >> b;

	int x, y, ka, kb;

	x = power(G, a, P);
	cout << "x is: " << x << endl;
	y = power(G, b, P);
	cout << "y is: " << y << endl;

	ka = power(y, a, P);
	cout << "ka is: " << ka << endl;
	kb = power(x, b, P);
	cout << "kb is: " << kb << endl;

	if (ka == kb){
		cout << "Symmetric Key!" << endl;
	}
	else{
		cout << "Asymmetric Key!" << endl;
	}
}
