$(document).ready(function() {
	var version = "0.0.1";
	var public_key = "3f7e2d601f40b4a08e4e397680a03fa1"; // oh no! an api key! lol
	var wcl_base = "https://www.warcraftlogs.com:443/v1/"

	$('#input_submit').click(function(){
		var code = $('input#wcl_id').val()
		$('#output').text('') // Clear the output stream

		out('Xan\'shi Evaluator Started -- Using version ' + version)
		out('WCL ID: ' + code)

		// $.getJSON('/assets/cgi-bin/wcl.py', {
			
		// })
		// $.ajax ({
		// 	dataType: "json",
		// 	url: wcl_base + "reports/events/" + code + "?api_key="+public_key,
		// 	function(data) {
		// 		alert(data);
		// 	}
		// });
	});

	function out(a) {
		$('#output').append('<div id="js_out_temp">' + a + '</div>')
	}

	function hget(url) {
		var xmlHttp = new XMLHttpRequest();
		xmlHttp.open("GET", url, false);
		xmlHttp.send(null);
		return xmlHttp.responseText;
	}
});

