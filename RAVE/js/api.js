



function loadApi(){
	jQuery(function(){
		
		initializeInstagram();		
		
		initializeMap();
		
		$.getJSON("http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&api_key=f996e46c0741a8a1fb0fd3f983f24d08&format=json&limit=5&artist=" + decodeURI(page).replace(/_/g, "").split("(")[0].replace("'",""), function(data) {  
			var statData = [];
			try{
				var x = data.toptracks.track;
				$(x).each(function() {
					statData.push({text: this.name, count: this.playcount});
				});
			}
			catch(err){}
			try {
				initializeChart(statData);
				$("#statsTitle").attr("style", "display:block;");
			}
			catch(err){
				try {
					var band;
					$(".infobox tbody tr").each(function(index){
						if ($(this).find("th").text().replace("\n", "") == "Associated acts") band = $(this).find("td").text().split("\n")[0].split(",")[0];
					});
					$.getJSON("http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&api_key=f996e46c0741a8a1fb0fd3f983f24d08&format=json&limit=5&artist=" + band, function(data) {  
						var statData = [];
						try{
							var x = data.toptracks.track;
							$(x).each(function() {
								statData.push({text: this.name, count: this.playcount});					
							});
						}
						catch(err){}
						try {	
							initializeChart(statData);
							$("#statsTitle").attr("style", "display:block;");
						}
						catch(err){}
					});		
					
				}
				catch (err){}
			}			
		});
		
		
	});
}