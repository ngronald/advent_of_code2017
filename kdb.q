/ advent of code 2017

/ day 1
/ Q1
sum x where x=-1 rotate x:"I"$/:first read0 `:input/day1.txt
/ Q2 
sum x where x=(count[x]div 2) rotate x:"I"$/:first read0 `:input/day1.txt

/ day 2
/ Q1
sum {x:"I"$"\t" vs x;max[x]-min[x]} each read0 `:input/day2.txt
/ Q2
sum{
 x:"I"$"\t" vs x;
 sum q wsum (q<>1) & 0=mod[;1] q:x %/:\:x
 } each read0 `:input/day2.txt 
