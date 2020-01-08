var fn = prompt("First name: ")
var ln = prompt("Last name: ")
var height = prompt("Height: ")
var age = prompt("Age: ")
var pet = prompt("Pet name: ")
alert("Thanks for the info!")

if (fn[0] === ln[0] && height >= 170 && 21 <= age <= 29 && pet.slice(-1) === "y"){
	console.log("Welcome SPY!")
}else {
	console.log("Nothing to see here")
}