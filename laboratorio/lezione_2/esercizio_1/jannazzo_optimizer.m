load data02.m

warning('off', 'all');
best_norm = 0.482666
best_exp_1 = -0.6739
best_exp_2 = 0.001
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
