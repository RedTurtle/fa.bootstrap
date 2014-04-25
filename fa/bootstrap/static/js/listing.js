/*jslint undef: true */
/*global $, document: false */

$(document).ready(function(){
    "use strict";

    $('ul.pagination').children('a').map(function(index) {$(this).replaceWith('<li><a href="'+ $(this).attr('href') +'">' + $(this).text() + '</a></li>');});
    $('ul.pagination').children('span.active').map(function(index) {$(this).replaceWith('<li class="active"><a href="#">' + $(this).text() + '</a></li>');});
    $('ul.pagination').children('span').map(function(index) {$(this).replaceWith('<li class="disabled"><a href="#">' + $(this).text() + '</a></li>');});
	$('a[href=#]').click(function(ev){ev.preventDefault()});
});
