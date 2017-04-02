function submitNode() {
	$.ajax({
		type: "post",
		url:"./submit_node/",
		data: {lat: document.getElementById('lat'), lng: document.getElementById('lng')},
		success: function(output) {
			}
	});    
	return false;
}
$('#submit').onclick=submitNode();

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
	var map = new google.maps.Map(document.getElementById('map'), {
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
		infoWindow.setContent("<form><input type='text' id='lat' value='"+submitLat+"'><p><input type='text' id='lng' value='"+submitLng+"'><p><input type='button' value='submit' id='submit'></form>");
		infoWindow.open(map, submitMarker);
	});
}

