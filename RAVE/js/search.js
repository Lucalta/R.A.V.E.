jQuery(function($){
	$("#search").click(function(){
		window.location = "http://site1753.web.cs.unibo.it/wiki/" + $("#searchText").val().replace(/ /g, "_");
	});
	$('#searchText').keydown(function(e){
		if(e.keyCode == 13){
			window.location = "http://site1753.web.cs.unibo.it/wiki/" + $("#searchText").val().replace(/ /g, "_");
		}
	});
});