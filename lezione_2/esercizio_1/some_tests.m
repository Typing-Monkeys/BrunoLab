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

# compito: trovare norma minore con 3 funzioni


A=[ones(n,1) x.^0.2 log(x)]
b=y
v=(A'*A)\(A'*b) 


norm(A*v-b) 

A=[ones(n,1) log(x) x.^-4]
b=y
v=(A'*A)\(A'*b)
norm_posta = norm(A*v-b)


plot(x, y, 'p'); hold on
plot(x, v(1) + v(2)*log(x) + v(3) * x.^-4)
#0.5317

A=[ones(n,1) 0.5*log(x) x.^2]
b=y
v=(A'*A)\(A'*b)
norm(A*v-b) 
plot(x, y, 'p'); hold on
plot(x, v(1) + v(2)*0.5*log(x) + v(3)*x.^2)


clear
load data02.m

A=[ones(n,1) log(x) x.^-10]
b=y
v=(A'*A)\(A'*b)
norm(A*v-b)

plot(x, y, 'p'); hold on
plot(x, v(1) + v(2)*log(x) + v(3) * x.^-10)
#0.5317

A=[x log(x) x.^-4]
b=y
v=(A'*A)\(A'*b)
norm(A*v-b) 
plot(x, y, 'p'); hold on
plot(x, v(1)*x + v(2)*log(x) + v(3) * x.^-4)


# FORSE CI SIAMO
warning('off', 'all');
best_norm = 1
best_exp_1 = -4
best_exp_2 = 0.01
for i=1:8000
    for j=1:8000
        tmp_exp_1 = -(i*.001); # -> .01
        tmp_exp_2 = (j*.001);
        A=[ones(n,1) x.^tmp_exp_1 x.^tmp_exp_2];
        b=y;
        v=(A'*A)\(A'*b);
        tmp_norm = norm(A*v-b);
        if (tmp_norm < best_norm);
            best_norm = tmp_norm;
            best_exp_1 = tmp_exp_1;
            best_exp_2 = tmp_exp_2;
            # printf("Trovata norm migliore con %d con valore: %d\n", best_exp, best_norm);
            printf("%d\n", i)
        endif
    endfor
endfor

printf("Norma: %d EXP: (%d, %d)\n", best_norm, best_exp_1, best_exp_2)
# best_norm 0.482666 exp (-0.675, -0.673)


A=[x.^0.45 x.^0.48 x.^0.47];
b=y
v=(A'*A)\(A'*b)
norm(A*v-b) 
plot(x, y, 'p'); hold on
plot(x, v(1)*x.^0.45 + v(2)*x.^0.48  + v(3)*x.^0.47)

