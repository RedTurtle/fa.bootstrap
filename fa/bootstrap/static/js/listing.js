$(document).ready(function(){
    $('div.pagination ul').children('a').map(function(index) {$(this).replaceWith('<li><a href="'+ $(this).attr('href') +'">' + $(this).text() + '</a></li>')});
    $('div.pagination ul').children('span.active').map(function(index) {$(this).replaceWith('<li class="active"><a href="#">' + $(this).text() + '</a></li>')})
    $('div.pagination ul').children('span').map(function(index) {$(this).replaceWith('<li class="disabled"><a href="#">' + $(this).text() + '</a></li>')})
})
