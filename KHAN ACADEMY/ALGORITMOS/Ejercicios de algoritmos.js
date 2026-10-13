// let animals = ["gnu", "zebra", "antelope", "aardvark", "yak", "iguana"];
// animals.sort();
// console.log(animals);

// var array = [18, 6, 66, 44, 9, 22, 14];

// for (var i = 0; i < array.length; i++) {
//     console.log(array[i]);
// }

// console.log(array);


//······························Ordenamiento por selección·····························

// var swap = function(array, firstIndex, secondIndex) {
//     var temp = array[firstIndex];
//     array[firstIndex] = array[secondIndex];
//     array[secondIndex] = temp;
// };

// var indexOfMinimum = function(array, startIndex) {
//     var minValue = array[startIndex];
//     var minIndex = startIndex;

//     for(var i = minIndex + 1; i < array.length; i++) {
//         if(array[i] < minValue) {
//             minIndex = i;
//             minValue = array[i];
//         }
//     } 
//     return minIndex;
// }; 

// var selectionSort = function(array) {
//     var changeNumber;
//     for(var i = 0; i < array.length; i++) {
//         changeNumber = indexOfMinimum(array, i);
//         swap(array, i, changeNumber);
//     }
// };

// var array = [22, 11, 99, 88, 9, 7, 42];
// selectionSort(array);
// println(array);


//-----------------------Explicacion de la complejidad de selection sort-----------------------

// FÓRMULA PARA SUMAR 1+2+3+...+n:
// (número más pequeño + número más grande) × número de parejas
// = (1 + n) × (n/2)
// = n²/2 + n/2


// POR QUÉ IMPORTA:
// Si duplicas el tamaño del arreglo (n), 
// el tiempo de ejecución se CUADRUPLICA (no se duplica).

// Por eso selection sort es ineficiente para arreglos grandes.
// Algoritmos como merge sort (Θ(n log n)) son mucho más rápidos 
// para datos grandes.

//-----------------------Ejercicios de selection sort-----------------------
 

var xLoc  =160; // left edge of display
var xSpan = 30; // horizontal distance between values
var yLoc  = 50; // top of display
var ySpan = 50; // vertical distance between values

var displayArray = function(array, x, y, minIndex, toIndex){
    textFont(createFont("monospace"), 12);
    for(var i=0; i < array.length; i++){
        if( i === minIndex) {
            fill(255, 0, 0);
        } else {
            fill(0, 0, 0);
        }
        text(array[i], x+ (i*xSpan), y); 
    }
    
    if(i !== array.length -1){
        line(x + (minIndex + 0.25) * xSpan, y+3, 
             x + (toIndex + 0.25) * xSpan, y + ySpan-12         );
    } 
};

var swap = function(array, firstIndex, secondIndex){
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexMinimum = function(array, startIndex){
    var minValue = array[startIndex];
    var minIndex = startIndex;
    
    for(var i = minIndex + 1 ; i < array.length; i++){
        if(array[i] < minValue){
        minIndex = i;
        minValue = array[i];
        }
    }
    return minIndex;
};

var selectionSort = function(array) {
 var changeNumber;
 var yLoc_local = yLoc;
     for(var i = 0; i < array.length; i++) {
         //yLoc_local = yLoc + i*ySpan;
        changeNumber = indexMinimum(array, i);
        
        yLoc_local += ySpan;
        displayArray(array, xLoc, yLoc_local, changeNumber, i);
         
         swap(array, i, changeNumber);
     }
    
     displayArray(array, xLoc, yLoc_local, -1, -1);
};

var array = [99, 2, 1, 55, 30];
selectionSort(array);
println(array);