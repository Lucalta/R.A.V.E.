	var geocoder;
	var map;
	
function initializeMap() {
	jQuery(function($){
		var address = $(".birthplace").text();
		var nosplit = false;
		var died = false;
		if (!address) {
			$(".infobox tbody tr").each(function(index){
				if ($(this).find("th").text() == "Born") address = $(this).find("td").text();
				if ($(this).find("th").text() == "Origin") {address = $(this).find("td").text(); nosplit = true;}
				if ($(this).find("th").text() == "Died") died = true;
			});
			while (address.indexOf(')') > -1 && !died && !nosplit) address = address.split(")")[2];
			if (!nosplit && died) address = address.split("\n")[1];
		}
		geocoder = new google.maps.Geocoder();
		var latlng = new google.maps.LatLng(-34.397, 150.644);
		var mapOptions = {
			zoom: 8,
			center: latlng
		}
		map = new google.maps.Map(document.getElementById('map'), mapOptions);


		geocoder.geocode( { 'address': address}, function(results, status) {
		  if (status == 'OK') {
			map.setCenter(results[0].geometry.location);
			var marker = new google.maps.Marker({
				map: map,
				position: results[0].geometry.location
			});
			$("#map").attr("class","mapVisible");
			$("#mapsTitle").attr("style", "display:block;");
		  } else {
		  }
		});
	});
}