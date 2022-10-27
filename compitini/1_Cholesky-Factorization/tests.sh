#!/bin/bash
size=5000
seed=20
jit=""
method="column"


function cholesky() {
    python main.py -tm benchmark -alg cholesky --method ${method} --size $size --seed $seed -v $jit
}

function gauss () {
    python main.py -tm benchmark -alg gauss --size $size --seed $seed -v
}


function cholesky_test_3() {
    # se viene passato 1 avvia lo script con il flag --jit
    if [ $1 -eq 1 ]
    then
        jit="--jit"
    fi

    for m in column row diagonal
    do
        method=$m
        mkdir $method
        for i in {1..3}
        do 
            cholesky
            mv "cholesky_${method}_${size}_${seed}.json" "cholesky_${method}_${size}_${seed}_${i}.json"
        done
        mv *.json $method
    done
}


function main() {
    # cholesky_test_3 1 # avvia lo script con il flag --jit
    # cholesky_test_3
    
    size=40000
    jit="--jit"
    method="diagonal"
    cholesky 
}

main