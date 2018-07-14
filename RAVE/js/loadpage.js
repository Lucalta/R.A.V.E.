jQuery(function($){
	if (page != "index.html") {		
		$.getJSON("https://en.wikipedia.org/w/api.php?action=parse&format=json&disableeditsection=1&disabletoc=1&callback=?&origin=*&page=" + page, function(data) {                               
			try{
				$("#mainContent").html(data.parse.text["*"]);
				$("#pageTitle").text(decodeURI(page).replace(/_/g, " "));
				startAnnotator();
				$.getJSON("https://en.wikipedia.org/w/api.php?format=json&action=query&origin=*&prop=categories&cllimit=max&titles=" + page, function(data) {                               
					try{						
						var x = data.query.pages[Object.keys(data.query.pages)[0]].categories;
						$(x).each(function() {
							if (this.title == "Category:English rock singers") {
								
								$.getJSON("https://api.crossref.org/works?rows=10&query=" + page.replace(/_/g, "+"), function(data) {                               
									try{
										s = "<ul>";
										var z = data.message.items;
										$(z).each(function() {
											s += "<li><a href='" + this.URL + "'>" + this.title[0] + "</a></li>";
										});
										s += "</ul>";
										$("#crossrefTitle").attr("style", "display:block;");
										$("#crossref").html(s);
										loadApi();
									}
									catch(err){}
								});
									
								
							}
						});						
					}
					catch(err){}
				});
			}
			catch(err){$("#error404").attr("style", "display:block;")}
		});
	}
});