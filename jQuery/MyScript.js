$('h1').click(function(){
	console.log("Here's my click!")
})

$('li').click(function(){
	console.log('any li was clicked!')
})

$('h2').click(function(){
	$(this).text('I WAS CLICKED MAN!')
})

$('input').eq(0).keypress(function(){
	$('h3').toggleClass('turnBlue')
})