clear
load data04c.m %frame del cubo
%load data04t.m %frame del triangolo
clf
plot3(f1(1,:),f1(2,:),f1(3,:));hold on
axis([-3 3 -3 3 -3 3]);
[az el] = view;
axis('equal')
% generare una rotazione a caso 
% (è generabile con fattorizzazione QR di matrice casuale)
N = 0; t=0.1;
for ell = 1:N
    [Q R] = qr(randn(3));
    f2 = Q*f1;
    plot3(f2(1,:),f2(2,:),f2(3,:)); 
    pause(t);
end

v = [1;0;0];
N = 100; t = 0.05;
theta = 1;
G = [1 0 0;
    0 cos(theta) -sin(theta);
    0 sin(theta) cos(theta);];
for ell = 1:N
    f1 = G*f1;
    plot3(f1(1,:),f1(2,:),f1(3,:)); 
    pause(t);
end
    