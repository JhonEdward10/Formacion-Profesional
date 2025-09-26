//Capitulo 1

// console.log("Hola mundo!");
// console.log("Jhon Edward Mendez Tovar");
// console.log(2000);
// console.log("abc", "def", "ghi");
// console.log("Jhon Edward Mendez", "(2000)");
// console.log("Jhon"+"Edward"+"Mendez"+"(2000)");

//___________________________________________________________________________________________

//Capitulo 2

// var height;
// console.log(height); // -> undefined
// console.log(weight); // -> Uncaught ReferenceError: weight is not defined

// var height;
// var height;
// console.log(height);

// let height;
// let height;
// console.log(height);

// let height = 180;
// let anotherHeight = height;
// let weight;
// console.log(height); // -> 180
// console.log(anotherHeight); // -> 180
// weight = 70;
// console.log(weight); // -> 70

// "use strict"
// height = 180;
// console.log(height); // -> 180

// let steps = 100;
// console.log(steps); // -> 100
// steps = 120; 
// console.log(steps);// -> 120
// steps = steps + 200;
// console.log(steps); // -> 320

// let greeting = "Hello!";
// let counter = 100;
// greeting = greeting + counter;
// console.log(greeting);

// const greeting = "Hello!";
// greeting = "Hi!";
// console.log(greeting);

// let counter; 
// console.log(counter);
// {
//   counter = 1;
//   console.log(counter);
// }

// counter = counter + 1;
// console.log(counter);

// let height = 180;
// {
//     let weight = 70;
//     console.log(height);
//     console.log(weight); 
// }
// console.log(height); 
// console.log(weight); 

// let height = 200;
// {
//     let weight = 100;
//     {
//     let info = "tall";
//     console.log(height); // -> 200
//     console.log(weight); // -> 100
//     console.log(info); // -> tall
//     }
//     console.log(height); // -> 200
//     console.log(weight); // -> 100
//     // console.log(info); // -> Uncaught ReferenceError: info is not defined
//    }
// //    console.log(weight);

//______________________________________________________________________________________

// "use strict"
// var height = 180;
// {
//     var weight = 70;
//     console.log(height); // -> 180
//     console.log(weight); // -> 70
// }
// console.log(height); // -> 180
// console.log(weight); // -> 70

//___________________________________________________________________________________________

//Un poco acerca de las funciones

// function testDePrueba(){
//     console.log("Hello");
//     console.log("World!");
// }

// testDePrueba();
//_____________________________________________________________________________________-
// var globalGreeting = "Good ";
   
// function testFunction() {
//     var localGreeting = "Morning ";
//     console.log("function:");
//     console.log(globalGreeting);
//     console.log(localGreeting);
// }
   
// testFunction();

// console.log("main program:");
// console.log(globalGreeting);
// console.log(localGreeting);

// let counter = 100;
// console.log(counter); // -> 100
// {
//     counter = 200;                             // Mucho cuidado con este tipo de procedimientos, no es aconsejable
//     console.log(counter); // -> 200
// }
// console.log(counter); // -> 200

// let counter = 100;
// console.log(counter); // -> 100
// {
//     let counter = 200;                              // Esto es lo que se debe hacer para no tener problemas futuros
//     console.log(counter); // -> 200
// }
// console.log(counter); // -> 100

//________________________________________________________________________________________

//Elevacion

// "use strict"
// var height = 180;
// console.log(height); // -> 180
// console.log(weight); // -> Uncaught ReferenceError: weight is not defined
// var weight = 70;          // Esto es interpretado de la siguiente manera
// console.log(weight);


// var weight;
// var height = 180;
// console.log(height); // -> 180
// console.log(weight); // -> undefined
// weight = 70;            //Asi es interpretado y se va a ver igual que lo anterior
// console.log(weight); // -> 70


//Pero esto funciona diferente con las variables const y let
//_____________________________________________________________


// //Ejercicios
// function empresaDeFlores(){
//     const precioDeUnaRosa = 8;
//     const precioDeUnTulipan = 2;
//     const precioDeUnLirio = 10;

//     let numeroDeRosas = 70;
//     let numeroDeTulipanes = 120;
//     let numeroDeLirios = 50;

//     let precioTotalRosas = (precioDeUnaRosa * numeroDeRosas);
//     let precioTotalTulipanes = (precioDeUnTulipan * numeroDeTulipanes);
//     let precioTotalLirios = (precioDeUnLirio * numeroDeLirios);

//     let SumaTotalTodasLasFlores = (precioTotalTulipanes+precioTotalLirios+precioTotalRosas);

//     console.log("Rosas - Unidad:", precioDeUnaRosa, ", Cantidad de rosas:", numeroDeRosas);
//     console.log("Tulipanes - Unidad:", precioDeUnTulipan, ", Cantidad de tulipanes:", numeroDeTulipanes);
//     console.log("Lirios - Unidad:", precioDeUnLirio, ", Cantidad de lirios:", numeroDeLirios);
//     console.log("Precios de todas las rosas:", precioTotalRosas, ", Precio de todos los tulipanes:", precioTotalTulipanes, ", Precios de todos los lirios:", precioTotalLirios);
//     console.log("Precio Total de todas las flores:", SumaTotalTodasLasFlores);



//     numeroDeRosas = numeroDeRosas - 20;
//     numeroDeLirios = numeroDeLirios - 30;
//     precioTotalRosas = (precioDeUnaRosa * numeroDeRosas);
//     precioTotalTulipanes = (precioDeUnTulipan * numeroDeTulipanes);
//     precioTotalLirios = (precioDeUnLirio * numeroDeLirios);

//     SumaTotalTodasLasFlores = (precioTotalTulipanes+precioTotalLirios+precioTotalRosas);

//     console.log("Rosas - Unidad:", precioDeUnaRosa, ", Cantidad de rosas:", numeroDeRosas);
//     console.log("Tulipanes - Unidad:", precioDeUnTulipan, ", Cantidad de tulipanes:", numeroDeTulipanes);
//     console.log("Lirios - Unidad:", precioDeUnLirio, ", Cantidad de lirios:", numeroDeLirios);
//     console.log("Precios de todas las rosas:", precioTotalRosas, ", Precio de todos los tulipanes:", precioTotalTulipanes, ", Precios de todos los lirios:", precioTotalLirios);
//     console.log("Precio Total de todas las flores:", SumaTotalTodasLasFlores);
// }

// empresaDeFlores();

//______________________________________________________________________________________________________________

// const name1 = "Maxwell Wright";
// const number1 = "0191 719 6495";
// const email1 = "Curabitur.egestas.nunc@nonummyac.co.uk";

// const name2 = "Raja Villareal";
// const number2 = "0866 398 2895";
// const email2 = "posuere.vulputate@sed.com";

// const name3 = "Helen Richards";
// const number3 = "0800 1111";
// const email3 = "libero@convallis.edu";


// console.log("Name: "+ name1,"/", "Number: "+ number1,"/", "Email: "+ email1);
// console.log("Name: "+ name3,"/", "Number: "+ number3,"/", "Email: "+ email3);

//______________________________________________________________________________________________________________

//Capitulo 2.1

//Operador typeof

// const email3 = true;
// console.log(typeof(email3));

// let year = 1990;
// console.log(typeof (year)); // -> number
// console.log(typeof 1991); // -> number
   
// let name = "Alice";
// console.log(typeof name); // -> string
// console.log(typeof "Bob"); // -> string
   
// let typeOfYear = typeof year;
// console.log(typeOfYear); // -> number
// console.log(typeof typeOfYear); // -> string

//Booleanos
// let isDataValid = true;
// let isStringTooLong = false;
// let isGameOver = false;
// continueLoop = true;
   
// console.log(false); // -> false
// console.log(typeof false); // -> boolean
// console.log(isDataValid); // -> true
// console.log(typeof isDataValid); // -> boolean

//Numeros
const year = 1991;
let delayInSeconds = 0.00016;
let area = (16 * 3.14);
let halfArea = area / 2;
   
console.log(year); // -> 1991;
console.log(typeof year); // -> number;
console.log(delayInSeconds);
console.log(area);
console.log(halfArea);
console.log(typeof halfArea); // -> number;


console.log("Hello");