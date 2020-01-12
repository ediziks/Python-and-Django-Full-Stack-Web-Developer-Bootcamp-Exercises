var res = document.querySelector("#res")

// or <button onClick="window.location.reload();">Refresh Page</button>
// in html file for refreshing page
res.addEventListener("click", function(){
	window.location.reload()
})

var squares = document.querySelectorAll("td")

function changeMarker() {
	if (this.textContent === "") {
		this.textContent = "X"
	}else if (this.textContent === "X") {
		this.textContent = "O"
	}else {
		this.textContent = ""
	}
}

for (var i = 0; i < squares.length; i++ ) {
	squares[i].addEventListener("click", changeMarker)
}


// LONG VERSION

// var td1 = document.querySelector("#td1")
// var td2 = document.querySelector("#td2")
// var td3 = document.querySelector("#td3")
// var td4 = document.querySelector("#td4")
// var td5 = document.querySelector("#td5")
// var td6 = document.querySelector("#td6")
// var td7 = document.querySelector("#td7")
// var td8 = document.querySelector("#td8")
// var td9 = document.querySelector("#td9")

// td1.addEventListener("click", function(){
// 	if (td1.textContent === "") {
// 		td1.textContent = "X"
// 	}else if (td1.textContent === "X") {
// 		td1.textContent = "O"
// 	}else {
// 		td1.textContent = ""
// 	}
// })

// td2.addEventListener("click", function(){
// 	if (td2.textContent === "") {
// 		td2.textContent = "X"
// 	}else if (td2.textContent === "X") {
// 		td2.textContent = "O"
// 	}else {
// 		td2.textContent = ""
// 	}
// })

// td3.addEventListener("click", function(){
// 	if (td3.textContent === "") {
// 		td3.textContent = "X"
// 	}else if (td3.textContent === "X") {
// 		td3.textContent = "O"
// 	}else {
// 		td3.textContent = ""
// 	}
// })

// td4.addEventListener("click", function(){
// 	if (td4.textContent === "") {
// 		td4.textContent = "X"
// 	}else if (td4.textContent === "X") {
// 		td4.textContent = "O"
// 	}else {
// 		td4.textContent = ""
// 	}
// })

// td5.addEventListener("click", function(){
// 	if (td5.textContent === "") {
// 		td5.textContent = "X"
// 	}else if (td5.textContent === "X") {
// 		td5.textContent = "O"
// 	}else {
// 		td5.textContent = ""
// 	}
// })

// td6.addEventListener("click", function(){
// 	if (td6.textContent === "") {
// 		td6.textContent = "X"
// 	}else if (td6.textContent === "X") {
// 		td6.textContent = "O"
// 	}else {
// 		td6.textContent = ""
// 	}
// })

// td7.addEventListener("click", function(){
// 	if (td7.textContent === "") {
// 		td7.textContent = "X"
// 	}else if (td7.textContent === "X") {
// 		td7.textContent = "O"
// 	}else {
// 		td7.textContent = ""
// 	}
// })

// td8.addEventListener("click", function(){
// 	if (td8.textContent === "") {
// 		td8.textContent = "X"
// 	}else if (td8.textContent === "X") {
// 		td8.textContent = "O"
// 	}else {
// 		td8.textContent = ""
// 	}
// })

// td9.addEventListener("click", function(){
// 	if (td9.textContent === "") {
// 		td9.textContent = "X"
// 	}else if (td9.textContent === "X") {
// 		td9.textContent = "O"
// 	}else {
// 		td9.textContent = ""
// 	}
// })