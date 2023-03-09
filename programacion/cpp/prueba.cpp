#include<iostream>
using namespace std;

string nombreYEdad(string nombre, string edad){
	return "Te llamas "+nombre+" y tienes "+edad+ "años";
}


int main(){
	string tablero[3][3] = {{"x","x","x"}, {" "," "," "}, {" "," "," "}};
	int filas = sizeof(tablero);

	for (int i = 0; i <= filas; i++){
		for (int a = 0; a <= filas; a++){
			cout<<tablero[i][a]<<endl;
		}
		
	}
	
	return 1;


}