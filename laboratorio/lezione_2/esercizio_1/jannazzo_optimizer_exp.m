load data02.m

warning('off', 'all');
best_norm = 0.470794
best_exp_1 = 0.97
best_exp_2 = 0.972
best_exp_3 = 0


for i=1:800
    for j=1:800
        for h=1:800
            tmp_exp_1 = (i*.01); # -> .01
            tmp_exp_2 = (j*.01);
            tmp_exp_3 = (h*.01);
            A=[x.^tmp_exp_1 x.^tmp_exp_2 x.^tmp_exp_3];
            b=y;
            v=(A'*A)\(A'*b);
            tmp_norm = norm(A*v-b);
            if (tmp_norm < best_norm);
                best_norm = tmp_norm;
                best_exp_1 = tmp_exp_1;
                best_exp_2 = tmp_exp_2;
                best_exp_3 = tmp_exp_3;
                printf("%d\n", i)
            endif
        endfor
    endfor
endfor


printf("Norma: %d EXP: (%d, %d, %d)\n", best_norm, best_exp_1, best_exp_2, best_exp_3)

