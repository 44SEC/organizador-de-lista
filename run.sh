#!/bin/bash

echo "[!] Executando algoritmo 1: BubbleSort"
resultado1=$(python3 bubblesort.py | grep -m 1 '\[?\] O programa levou:')
echo $resultado1

echo "[!] Executando algoritmo 2: MergeSort"
resultado2=$(python3 mergesort.py | grep -m 1 '\[?\] O programa levou:')
echo $resultado2

echo "[!] Executando algoritmo 3: QuickSort"
resultado3=$(python3 quicksort.py | grep -m 1 '\[?\] O programa levou:')
echo $resultado3
