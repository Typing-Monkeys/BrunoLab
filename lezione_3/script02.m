% Laboratorio del 14 ottobre 2022
clear
load data03.m
#{
#Prove mesh e funzioni
plot3(1,2,3,'p')
hold on
plot3(1,2,5,'p')
hold off

x = -4:0.05:4;
y=x;
[xx,yy]=meshgrid(x,y);
zz=xx.^2 + yy.^2;
mesh(xx,yy,zz);

clear
function prova = F(x)
    prova = sin(x)^2+cos(2*x)^2;
end
x = 10
F(x)
#}

plot3(x,y,z,'p'); hold on

# calcolare il piano per i primi 3 punti
#i1 = 1; i2 = 2; i3 = 3;
A0 = [x(1:3) y(1:3) z(1:3)];
b = [1;1;1];
v = A0\b;

# calcolare i piano con 3 punti a caso

i1 = ceil(rand(1)*N);
i2 = ceil(rand(1)*N);
i3 = ceil(rand(1)*N);

A1 = [x(i1) y(i1) z(i1);
      x(i2) y(i2) z(i2);
      x(i3) y(i3) z(i3);];
v1 = A1\b;

#Calcolo del piano con linear least squares applicato su 3 dimensioni
A2 = [x y ones(N,1)];
b2 = z;
v2 = A2\b2;

x = -3:0.1:3;
y = -3:0.1:3;

[xx yy] = meshgrid(x, y);

mesh(xx,yy,v2(1)*xx+v2(2)*yy+v2(3));

x = -3:0.1:3;
y = -3:0.1:3;

[xx yy] = meshgrid(x, y);

mesh(xx,yy,-v1(1)/v1(3)*xx-v1(2)/v1(3)*yy+1/v1(3));
