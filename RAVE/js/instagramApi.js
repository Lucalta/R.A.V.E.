function initializeInstagram(){
	jQuery(function($){
		var s = "https://api.instagram.com/v1/tags/{tag}/media/recent?access_token=3905099699.da06fb6.cc2efc9141c24a9c9c1eb2e537e27653";
		s = s.replace("{tag}", decodeURI(page).replace(/_/g, "").split("(")[0]);
		$.getJSON(s, function(data) {  
			s = "<ul>"
			var x = data.data;
			$(x).each(function() {
				try{s += "<li><img src='" + this.images.thumbnail.url + "'></li>";}
				catch(err){}
			});
			s += "</ul>";
			$("#instagramTitle").html("#" + decodeURI(page).replace(/_/g, "").split("(")[0] + " on Instagram");
			$("#instagramTitle").attr("style", "display:block;");
			$("#instagram").html(s);
		});
	});
}