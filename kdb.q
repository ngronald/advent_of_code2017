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
/ To generate all coordinates in the correct order of the ith layer 
genCoor:{[i]
  ylen:1+2*i;
  rightbound:i,/: til[ylen]-i; // All coordinates of the right-hand boundary, starting from bottom
  1 rotate distinct (,/) neg scan (,/) {x:reverse x;{(y;x)}.' x} scan rightbound
  };
/ Given a coordinate, get the sum of all of its neighbour (only those already stored in record) - order of the route is important
sumNear:{sum record@(x,y)+/:genCoor[1]}
while[input>last record;i+:1;allcoor:genCoor[i];{total:sumNear . x;record[x]:total}each allcoor]
record record binr input  /answer

/ day 4
/ Q1
sum{count[x]=count distinct x:" "vs x}each read0 `:input/day4.txt
/ Q2
sum{count[x]=count distinct asc@' x:" " vs x} each read0 `:input/day4.txt
/
/ day 5
a1:a2:"I"$read0 `:input/day5.txt;i1:i2:c1:c2:0;
while[(i1>=0) and i1<count a1;oi:i1;i1+:a1[i1];a1[oi]:a1[oi]+1;c1+:1]
while[(i2>=0) and i2<count a2;oi:i2;i2+:a2[i2];a2[oi]:a2[oi]+(-1 1)3>a2[oi];c2+:1]
c1 /Q1
c2 /Q2
\
/ day 6
c:count input:"I"$"\t" vs first read0 `:input/day6.txt;r:()
f:{r,:x;mi:(*)idesc x:(*)x;nx:@[x;mi;:;0];d:x[mi]mod c;enlist nx+(c#x[mi]div c)+neg[1+mi]rotate c##[d;1],c#0}
a:f\[{(*)not in [x;r]}@;enlist input]
count -1_a /Q1
count[-1_a]-(*)r?last a /Q2

/ day 12
dict:raze{x:get@'"<->"vs x;(enlist x 0)!enlist x 1} each read0 `:input/day12.txt
f1:{(count x 1;distinct x[1],raze(where max@'dict in)@/:x[0]_x[1])}
show first q1:f1/[{x[0]<> count x 1}@;(0;enlist 0)]
f2:{nx:x[0],last f1/[{x[0]<> count x[1]}@;(0;enlist x[1])];(nx;first key[dict]except nx)}
show q2:count 1_f2\[{count[dict]<>count x 0};(();0)]