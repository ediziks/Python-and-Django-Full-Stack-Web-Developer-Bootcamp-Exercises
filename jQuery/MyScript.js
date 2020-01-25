$('h1').click(function(){
	console.log("Here's my click!")
})

$('li').click(function(){
	console.log('any li was clicked!')
})

$('h2').click(function(){
	$(this).text('I WAS CLICKED MAN!')
})

// keypress
$('input').eq(0).keypress(function(){
	$('h3').toggleClass('turnBlue')
})

// on
$('h1').on('dblclick', function(){
	$(this).toggleClass('turnBlue')
})

$('h2').on('mouseenter', function(){
	$(this).toggleClass('turnRed')
})

// page fades out in 1000ms(turns whitepage)
$('input').eq(1).on('click', function(){
	$('.container').fadeOut(1000)
})