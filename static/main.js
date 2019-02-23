$(document).ready(function () {
    const ps = new PerfectScrollbar('.scroll');
    
    var dropzone = new Dropzone("#imageInput", {
        url: 'http://13.67.66.80:5000/image',
        method: 'POST',
        clickable: "#imageContainer",
        acceptedFiles: 'image/*',
        maxFiles: 1,
        previewTemplate: '<div style="display:none" class="dz-preview dz-file-preview"></div>'
    });

    dropzone.on('success', function(file){
        addOutputCard(file);
        $('.dz-message').hide();
    });

    dropzone.on('drop', function(file){
        console.log(file);
        $('.dz-message').hide();
    });

    dropzone.on('maxfilesexceeded', function(file){
        dropzone.removeAllFiles();
        dropzone.addFile(file);
    });

    function addOutputCard(file) {
        $('#imageInput').html('<img class="img-fluid" src="'+ file['dataURL'] +'">');
    }


});