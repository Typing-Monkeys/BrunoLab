# carica in memoria il dataset
load(data01.m)

# posso vedere cosa c'è in memoria
who

# mostra la dimenzione 
size(x)

# permette di fare grafici
plot([1 2 3], [1 -1 0])

x = 0:2*pi; y = sin(x);
plot(x, y)

x=0:0.001:2*pi
plot(x, y) # il grafico è molto più smooth 😉

x=linspace(0, 2*pi, 100) # un modo alternativo per creare array 😲
plot(x, y)

# axis fa uno zoom nell'area passatagli
axis([0 2 -1 1]) # le virgole negli array sono opzionali

plot(x, y); hold on # con hold on mantiene il vecchio grafo e li stampa insieme

plot(x, y, 'LineWidth', 2)
plot(x, y, 'o') # crea un marker invece di stampare un grafo connesso
plot(x, y, 'o', 'MarkerSize', 10)

# per compito: disegnare un cerchio

axis('equal') # in octave se l'area di stampa è un rettangolo e stampi un cerchio
              # lo vedi come un ellisse, questo lo impedisce.

clear # elimina tutto dalla memoria

load data01.m

who

plot(x, y, 'x', 'MarkerSize', 2); hold on

A = [ones(N, 1) x]
b = y
v = (A'*A)\(A'*b)

plot(x, y, 'x', 'MarkerSize', 2); hold on
plot(x, v(2)*x+v(1))


# SECONDO DATASET
clear
load data02.m
who
plot(x, y)
plot(x, y, 'x', 'MarkerSize', 2)

A = [ones(n, 1) log(x)]
b = y
v = (A'*A)\(A'*b)

plot(x, y, 'x', 'MarkerSize', 2); hold on
plot(x, v(2)*log(x)+v(1))

norm_log = norm(A*v-b)

A = [ones(n, 1) x x.^2]
b = y
v = (A'*A)\(A'*b)

norm_quad = norm(A*v-b)


plot(x, y, 'x', 'MarkerSize', 2); hold on
plot(x, v(2)*x.^2+v(1))

A = [ones(n, 1) x log(x) x.^2]
b = y
v = (A'*A)\(A'*b)

norm_mix = norm(A*v-b)

plot(x, v(2)*x + v(1) + v(3) * log(x) + v(4)x.^2)


polyfit(x, y, 19)
polyval([1 -1 2], 2)

hold on
xx = 0:0.01:2
plot(xx, polyval(polyfit(x, y, 19), xx))


# compito: trovare norma minore con 3 funzioni
