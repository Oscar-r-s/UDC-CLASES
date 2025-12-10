clear all
clc
disp('Regra de Simpson composta')
syms x
%Solicitamos información: función, intervalo, número de subintervalos:
f(x) =input('Introduce a función f(x):');
a =input('Introduce o punto a: ');
b =input('Introduce o punto b: ');
n =input('Número de subintervalos (debe ser par): ');
integralexacta=int(f(x),x,[a,b]);
if (rem(n,2) ~= 0)
disp('o número de subintervalos debe ser par')
return
end
%Representación da función en [a,b]
fplot(f,[a,b]);
grid,title('\bf Regra de Simpson composta')
%Calculamos a lonxitude de cada subintervalo
h=(b-a)/n;
j=0;
for i=2:2:n-1
x=a+h*i;
j=j+f(x);
end
k=0;
for i=1:2:n-1
x=a+h*i;
k=k+f(x);
end
%Introducimos a expresión da fórmula de Simpson composta
integral=(h/3)*(f(a)+ 4*k + 2*j + f(b));
%Imprimimos resultado en pantalla
fprintf('\n Aproximación da integral=\n');
disp(double(integral))
%Imprimimos valor exacto da integral
fprintf('\n Valor exacto da integral=\n');
disp(integralexacta)