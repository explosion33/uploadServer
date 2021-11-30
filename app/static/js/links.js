var loadLinks = async function() {
    let links = {}
    

    for (let i = 0; i<localStorage.length; i++) {
        let link = localStorage.key(i);
        let name = localStorage.getItem(link);

        links[link] = name;
    }


    links = await validateLinks(links);
    console.log(links);

    let container = document.getElementById("link_container");
    container.innerHTML = "";

    let num = 0;
    for (var link in links) {
        let name = links[link];
        container.innerHTML += "<div class='row text-center'><div class='col-lg-6 offset-lg-3'><a href='" + link + "'>" + name + "&nbsp</a></div></div>"
        num ++;
    }
    if (num == 0) {
        container.innerHTML = "<div class='row text-center'><div class='col-lg-6 offset-lg-3'>No Files Found</div></div>";
        container.innerHTML += "<div class='row text-center'><div class='col-lg-6 offset-lg-3'>You have no files, or they have been previously removed</div></div>"
    }

}


function validateLinks(links) {
    var xhr = new XMLHttpRequest()

    return new Promise(function(resolve, reject) {
        let url = '/validateLinks'
        
        xhr.open('POST', url, true)

        xhr.addEventListener('readystatechange', function(e) {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log("recieved validated links")
                console.log(JSON.parse(xhr.responseText));
                return resolve(JSON.parse(xhr.responseText));
            }
            else if (xhr.readyState == 4 && xhr.status != 200) {
                console.log("ERROR: Could not validate links" + xhr.status);
                return reject(xhr.status)
            }
        });

        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.send(JSON.stringify(links));
    });
}