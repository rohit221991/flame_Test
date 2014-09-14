$(document).ready(function(){
	function showlocation() {
		   // One-shot position request.
		   navigator.geolocation.getCurrentPosition(callback);
		}
		 
	function callback(position) {
		console.log($('#latitude').value);
		if($('#latitude').length != 0 && $('#latitude')[0].value == "") {
			   document.getElementById('latitude').value = position.coords.latitude;
			   document.getElementById('longitude').value = position.coords.longitude;
		}
	}
	
	showlocation();
	
	$('#back').click(function (e) {
		e.preventDefault();
	    window.history.back();
	});
	
});