var copy = function(data) {
    if (!navigator.clipboard) {
        let input = document.createElement('textarea');
        input.innerHTML = data;
        document.body.appendChild(input);
        input.focus();
        input.select();
    

        try {
            document.execCommand('copy');
            console.log('Fallback: Copying text with workaround');
        } catch (err) {
            console.error('Fallback: Could not copy text: ', err);
        }
        document.body.removeChild(input);

    }
    else {
        console.log("secure connection, using navigator");
        navigator.clipboard.writeText(data);
    }
}