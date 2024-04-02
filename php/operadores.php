<?php
$a = 3;
$b = 4;

$c = $a + $b;
echo $c . "\n";

$c = $a * $b;
echo $c . "\n";

$c = $a - $b;
echo $c . "\n";

if($a < $b){
    echo "Es verdad \n";
}else{
    echo "Es mentira \n";
}

if($a > $b){
    echo "Es verdad \n";
}else{
    echo "Es mentira \n";
}

$a = "4";

if($a === $b){

    echo "Es verdad \n";
    
}else{
    echo "Es mentira \n";
}

if($a == $b){

    echo "Es verdad \n";
    
}else{
    echo "Es mentira \n";
}

$a = 4;
if($a >= $b){
    echo "Es verdad \n";
}else{
    echo "Es mentira \n";
}


$a = 3;
$b = 4;
$z = 5;
$c = $a * $b;

if( $z > $b && $z > $a){
    echo "Es verdad \n";
}else{
    echo "Es mentira\n";
}

if( $z > $b || $z < $a){
    echo "Es verdad \n";
}else{
    echo "Es mentira\n";
}

$a = $a + 1;
$a++;

echo $a;

?>