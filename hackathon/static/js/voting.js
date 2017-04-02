$(document).ready(function() {
    
});

function sendVote(id,action) {
    $.ajax({
       type: "post",
       url:"./submit_voting/",
       data: {node:id, action:action},
       success: function(output) {
       }
    });
    if (action == 'up') {
        var numVotes = $('#up-'+id).text();
        $('#up-'+id).html("<span class='glyphicon glyphicon-arrow-up'></span> "+(parseInt(numVotes)+1));
    } else {
        var numVotes = $('#down-'+id).text();
        $('#down-'+id).html("<span class='glyphicon glyphicon-arrow-down'></span> "+(parseInt(numVotes)+1));
    }
    
    return false;
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
