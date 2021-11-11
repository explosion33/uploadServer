var drop = function (event) {
	var event = window.event || event;
	event.preventDefault();
	
	let dt = event.dataTransfer
	let files = dt.files
	console.log(files);
}

var allowDrop = function (event) {
  	var event = window.event || event;
	event.preventDefault();
}