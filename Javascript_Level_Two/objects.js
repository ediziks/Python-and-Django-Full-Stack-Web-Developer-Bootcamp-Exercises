var smpl = {
	prop: "Hello",
	myMethod: function(){
		console.log("myMethod was called")
	}
}

var myObj = {
	name: "edz",
	greet: function(){
		console.log("Hello "+ this.name)
	}
}