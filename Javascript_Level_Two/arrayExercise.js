// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
function addNew() {
	var name2add = prompt("Name: ")
	roster.push(name2add)
}

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT
function remove() {
	var name2remove = prompt("Name: ")
	// const creates read only reference to a value
	// but var also can be used in this case
	const index = roster.indexOf(name2remove)
	roster.splice(index, 1)
}

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER
function display() {
	console.log(roster)
}

// Create a function called display that prints out the roster to the console.


// Start by asking if they want to use the web app
var use = prompt("Would u like to use the app? y/n: ")

if (use==="y") {
	while (true) {
		var action = prompt("add/remove/display/quit: ")
		if (action === "add" ) {
			addNew()
		}else if (action === "remove") {
			remove()
		}else if (action === "display") {
			display()
		}else if (action === "quit") {
			break
		}else {
			alert("Wrong input.")
		}
	}
}
alert("Thanks for using! Refresh to restart.")

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
