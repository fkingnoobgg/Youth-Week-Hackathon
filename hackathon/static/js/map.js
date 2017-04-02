function submitNode() {
	$.ajax({
       type: "post",
       url:"./submit_node/",
       data: {lat:$('#lat').val(), lng: $('#lng').val(), name: $('#name').val(), description: $('#description').val()},
       success: function(output) {
       }
    });
}

var map;

function addHotspotsToMap(){
	$.ajax({
		type: "GET",
		url: "./query_node/",
		dataType: "json",
		success: function(jsonHotspotList){
			for (i=0; i < jsonHotspotList.length; i++){
				console.log(jsonHotspotList[i]);
				var lat = jsonHotspotList[i]['lat'];
				var lng = jsonHotspotList[i]['lng'];
				var id = jsonHotspotList[i]['id'];
				var name = jsonHotspotList[i]['name'];
				new google.maps.Marker({title: name, position: {'lat': lat, 'lng': lng}}).setMap(map);
			}
		}
	});
}

function getCookie(name) {
	var cookieValue = null;
	var i = 0;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (i; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
	crossDomain: false, // obviates need for sameOrigin test
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type)) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});


function initMap() {
	var myLatLng = {lat: -25.363, lng: 131.044};
	map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: myLatLng
    });

	var submitMarker = new google.maps.Marker({position: {lat: 0, lng: 0}});
	var infoWindow = new google.maps.InfoWindow({content: "if youre seein this its not working"});

	google.maps.event.addListener(map, 'click', function(event) {
		submitMarker.setPosition(event.latLng);
		submitMarker.setMap(map);
		var submitLat = submitMarker.getPosition().lat();
		var submitLng = submitMarker.getPosition().lng();
		infoWindow.setContent("<form><input type='hidden' id='lat' value='"+submitLat+"'><input type='hidden' id='lng' value='"+submitLng+"'><label for='name'>Hotspot Name</label><input type=text id='name' name='name'><p><label for='description'>Description</label><input type=text id='description' name='description'><p><input type='button' value='submit' id='submit' onclick='submitNode()'></form>");
		infoWindow.open(map, submitMarker);
	});

	google.maps.event.addListener(infoWindow,'closeclick',function(){
		submitMarker.setMap(null);
	});

	addHotspotsToMap();
}
