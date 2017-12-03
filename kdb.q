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

/ day 3
input:368078
/ Q1
dir:(-1 0 ; 0 1; 1 0; 0 -1)
/ find the right corner of that layer
rc:s*s:s+0=mod[s:ceiling sqrt input;2]
/ find out how many steps should move backward from the right corner to input
d:(rc-input) div (s-1)
r:(rc-input) mod (s-1)
sum abs (c,neg c:s div 2) + dir wsum 4#(d#(s-1)),r,3#0

/Q2
/ a global dict to store coordinates' value
record:(enlist(0;0))!enlist 1
i:0
while[input>last record;i+:1;allcoor:genCoor[i];{total:sumNear . x;record[x]:total}each allcoor]]]
record record binr input  /answer


/ To generate all coordinates in the correct order of the ith layer 
genCoor:{[i]
  ylen:1+2*i;
  rightbound:i,/: til[ylen]-i; // All coordinates of the right-hand boundary, starting from bottom
  1 rotate distinct (,/) neg scan (,/) {x:reverse x;{(y;x)}.' x} scan rightbound
  };
/ Given a coordinate, get the sum of all of its neighbour (only those already stored in record) - order of the route is important
sumNear:{
  x:x,(-1 1)+x;
  y:y,(-1 1)+y;
  co:1_raze x,/:\:y;
  sum record@co
  };