function drop(event) {
	var event = window.event || event;
	event.preventDefault();
	
	let dt = event.dataTransfer
	let files = dt.files
	console.log(files);

	if (files.length == 0) {
		errorUploading(0);
	}
	else if (files.length == 1) {
		uploadFile(files[0])
	}
	else {
		packFiles(files);
	}

}
function allowDrop(event) {
	var event = window.event || event;
	event.preventDefault();
}

function errorUploading(numFiles) {
	console.log("error " + numFiles);
}

//sends a file to /storeFile
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