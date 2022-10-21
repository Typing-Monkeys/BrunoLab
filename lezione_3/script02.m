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
#{
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
hold off
#}
%Continuo laboratorio del 14 ottobre 2022

%Idealmente vogliamo un piano che passa per tutti i punti
%ovvero fare il minimo quadrato su tutti i punti
%due equazioni diverse ma dovrebbero dare lo stesso risultato
clear
clf
load data03.m
plot3(x,y,z,'p'); hold on
A3 = [x y z];
b3 = ones(N,1);
v3 = A3\b3;

x0 = -3:0.1:3;
y0 = -3:0.1:3;

[xx yy] = meshgrid(x0, y0);

mesh(xx,yy,(1-v3(1)*xx-v3(2)*yy)/v3(3));

%trovare la rotazione da fare nel piano
%poi applicarla a tutti i punti del dataset
%e trovare il nuovo piano con i minimi quadrati

vn = v3;

G = givens(vn(2),vn(1));
G1 = [G' zeros(2,1);0 0 1];
vn = G1*vn;
G2 = givens(vn(3),vn(2));
G3 = [1 0 0; zeros(2,1) G2'];
vn = G3*vn;

Q=G3*G1;

%Dato che traspongo i vettori 
%x y z è come se moltiplico ogni piunto per Q
w = Q*[x';y';z'];
%Q*[x(1);y(1);z(1)]

plot3(w(1,:),w(2,:),w(3,:),".")

v4 = w'\b3;

x0 = -5:0.1:5;
y0 = -5:0.1:12;

[xx yy] = meshgrid(x0, y0);

mesh(xx,yy,(1-v4(1)*xx-v4(2)*yy)/v4(3));

%Rotazione tramite QR factorization (Questa funziona)
clear
clf
load data03.m
plot3(x,y,z,'p'); hold on
A3 = [x y z];
b3 = ones(N,1);
v3 = A3\b3;

P = [0 0 1; 0 1 0; 1 0 0]; %Matrice che scambia x e z
[Q0 R] = qr(P*v3);
Q = P * Q0' * P;
w = Q*[x';y';z'];
%Q*[x(1);y(1);z(1)]
plot3(w(1,:),w(2,:),w(3,:),"p")

x0 = -3:0.1:3;
y0 = -3:0.1:3;

[xx yy] = meshgrid(x0, y0);

mesh(xx,yy,(1-v3(1)*xx-v3(2)*yy)/v3(3));