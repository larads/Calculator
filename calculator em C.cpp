#include <stdio.h>

int main() {
  double num1, num2;
  char operador;
  double result;
  
  printf("Introduce el primer numero: ");
  scanf("%lf", &num1);
  
  printf("Introduce el segundo numero: ");
  scanf("%lf", &num2);
  
  printf("Introduce el operador (+, -, *, /): ");
  scanf(" %c", &operador);
  
  switch (operador) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      result = num1 / num2;
      break;
    default:
      printf("Operador no valido.\n");
      return 0;
  }
  
  printf("%.1lf %c %.1lf = %.1lf\n", num1, operador, num2, result);
  
  return 0;
}
