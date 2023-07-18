$(function(){
	$('.header__menu').click(function(event) {
		$('body').toggleClass('open-menu');
		return false;
	});
	
	$('.header__item').on('hover', function() {
		$('.header__item').each(function() {
			console.log(this);
			$(this).toggleClass('active');
		});
	});

});	