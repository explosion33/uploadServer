var drop = function(event) {
	var event = window.event || event;
	event.preventDefault();
	
	let dt = event.dataTransfer
	let files = dt.files
	console.log(files);

	if (files.length == 0) {
		errorUploading("no file");
	}
	else if (files.length == 1) {
		uploadFile(files[0])
	}
	else {
		packFiles(files);
	}
}

var dialog = function(event) {
	var event = window.event || event;

	var files = event.target.files; 
	
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

var allowDrop = function(event) {
	var event = window.event || event;
	event.preventDefault();
}

function errorUploading(error) {
	console.log("error " + error);

	let errorDiv = document.getElementById("error-corner");
	let html = "";

	html += `<div class="container">`
	html += `<div class="alert alert-danger alert-dismissible">`;
	html += `<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>`;
	html += "<strong>Error</strong> Could not upload file (" + error + ")";
	html += "</div></div>";

	errorDiv.innerHTML = html;
	
}

//sends a file to /storeFile
function uploadFile(file) {
	var url = '/storeFile'
	var xhr = new XMLHttpRequest()
	var formData = new FormData()
	xhr.open('POST', url, true)
  
	xhr.addEventListener('readystatechange', function(e) {
		if (xhr.readyState == 4 && xhr.status == 200) {
			localStorage.setItem(xhr.responseText, file.name);
			window.location.href = xhr.responseText;
		}
		else if (xhr.readyState == 4 && xhr.status != 200) {
			console.log("ERROR: Could not upload file " + xhr.status);
			errorUploading(xhr.status);
		}
	});

	xhr.upload.addEventListener("progress", function(e) {
		if (e.lengthComputable) {
			var percentComplete = e.loaded / e.total;
			percentComplete = parseInt(percentComplete * 100);
		  
			let bar = document.getElementById("progress-bar");
			bar.style.width = percentComplete + "%";
			if (percentComplete >= 5) {
				bar.innerText = percentComplete + "%";
			}

		}
	  }, false);
  
	let s = "" + file.size;
	console.log(s);
	formData.append('size', file.size);
	formData.append('big', file.size > 1000000000);
	formData.append('file', file);
	xhr.send(formData);
}

var init = function() {
	document.addEventListener('paste', (event) => {
		event.preventDefault()
		let file = event.clipboardData.files[0]

		if (file) {
			uploadFile(file);
		}
	});
}