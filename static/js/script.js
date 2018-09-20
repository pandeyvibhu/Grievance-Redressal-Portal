$(document).ready(function(){
	console.log("js working");
	$('nav.tabs li').click(function(){
		var tab_id= $(this).attr('data-tab');

		$('nav.tabs li').removeClass('active');	
		$('.tab-content').removeClass('current');

		$(this).addClass('active');
		$("#"+tab_id).addClass('current');
    	})
	
	$('div.solution ul li').click(function(){
		$(this).siblings().removeClass('selected');
		$(this).addClass('selected');
	})

	$('.select.categories span').click(function(){			
		$(this).toggleClass('selected');
		var nxtValue="";
		$('.select.categories span').each(function(){
			if ( $(this).hasClass('selected') ) {
				nxtValue = nxtValue+(" "+$(this).attr('data-category'));
			}
		});
		nxtValue= nxtValue.trim();	
		$(this).parent().siblings('.categories_input').val(nxtValue);
		console.log($(this).parent().siblings('.categories_input').val());
	})

	$('i.fa.fa-pencil').click(function(){
		$(this).siblings('span.selected').addClass('hidden');
		$(this).addClass("hidden");
		$(this).siblings('form').removeClass('hidden');
		$(this).siblings('i.fa.fa-check').removeClass('hidden');
		$(this).siblings('i.fa.fa-times').removeClass('hidden');
	})

	$('i.fa.fa-times').click(function(){
		$(this).siblings('span.selected').removeClass('hidden');
		$(this).siblings('i.fa.fa-pencil').removeClass('hidden');
		$(this).siblings('form').addClass('hidden');
		$(this).siblings('i.fa.fa-check').addClass('hidden');
		$(this).addClass('hidden');
	})

	$('i.fa.fa-check').click(function(){
		$(this).siblings('form').submit();
	})
})
