function drop(event) {
	var event = window.event || event;
	event.preventDefault();
	
	let dt = event.dataTransfer
	let files = dt.files
	console.log(files);
	uploadFile(files[0])
}
function allowDrop(event) {
	var event = window.event || event;
	event.preventDefault();
}

function uploadFile(file) {
	var url = '/storeFile'
	var xhr = new XMLHttpRequest()
	var formData = new FormData()
	xhr.open('POST', url, true)
  
	xhr.addEventListener('readystatechange', function(e) {
		if (xhr.readyState == 4 && xhr.status == 200) {
			window.location.href = "/link/" + xhr.responseText;
		}
		else if (xhr.readyState == 4 && xhr.status != 200) {
			console.log("ERROR: Could not upload file")
		}
	})
  
	formData.append('file', file)
	xhr.send(formData)
}