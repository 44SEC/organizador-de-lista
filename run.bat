@echo off

echo "[!] Executando algoritmo 1: BubbleSort"
findstr /C:"[?] O programa levou" bubblesort.py

echo "[!] Executando algoritmo 2: MergeSort"
findstr /C:"[?] O programa levou" mergesort.py

echo "[!] Executando algoritmo 3: QuickSort"
findstr /C:"[?] O programa levou" quicksort.py
