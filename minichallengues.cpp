
// Día 8 – Suma de Números (C++)

#include <iostream>
int main() {
    int a, b;
    std::cout << "Primer número: ";
    std::cin >> a;
    std::cout << "Segundo número: ";
    std::cin >> b;
    std::cout << "Suma = " << a + b << '\n';
    return 0;
}



// Día 9 – Ordenamiento de un Array (C++)

#include <iostream>
#include <vector>
#include <algorithm>
int main() {
    int n;
    std::cout << "¿Cuántos elementos? ";
    std::cin >> n;
    std::vector<int> v(n);
    std::cout << "Ingresa " << n << " enteros:\n";
    for (int &x : v) std::cin >> x;
    std::sort(v.begin(), v.end());           // orden ascendente
    std::cout << "Array ordenado: ";
    for (int x : v) std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}


// Día 10 – Palíndromo (C++)

#include <iostream>
#include <algorithm>
#include <cctype>
int main() {
    std::string texto;
    std::cout << "Ingresa una cadena: ";
    std::getline(std::cin, texto);

    // eliminar espacios y pasar a minúsculas
    std::string limpio;
    for (char c : texto)
        if (!std::isspace(static_cast<unsigned char>(c)))
            limpio += std::tolower(static_cast<unsigned char>(c));

    std::string inverso = limpio;
    std::reverse(inverso.begin(), inverso.end());

    if (limpio == inverso)
        std::cout << "Es palíndromo\n";
    else
        std::cout << "No es palíndromo\n";
    return 0;
}
