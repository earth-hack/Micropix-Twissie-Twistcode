$(document).ready(function () {
    const ps = new PerfectScrollbar('.scroll');
    
    var dropzone = new Dropzone("#imageInput", {
        url: window.location.href+'image',
        method: 'POST',
        clickable: "#imageContainer",
        acceptedFiles: 'image/*',
        maxFiles: 1,
        thumbnailHeight: 510,
        thumbnailWidth: 688,
        thumbnailMethod: 'contain',
        maxThumbnailFilesize: 100,
        previewTemplate: '<div style="display:none" class="dz-preview dz-file-preview"></div>'
    });

    dropzone.on('success', function(file){
        data = JSON.parse(file.xhr.response) 
        $('#outputContainer').html('<p class="mb-0">Output: '+data['output']['results']+'</p><p>Confidence: '+data['output']['confidence']+'%</p>');
        $('.lds-facebook').hide();
        $('.dz-message').hide();
    });

    dropzone.on('addedfile', function(file){
        $('#outputContainer').html('');
        $('.lds-facebook').show();
        $('.dz-message').hide();
    });

    dropzone.on('thumbnail', function(file, dataURL){
        addOutputCard(dataURL);
        $('.dz-message').hide();
    });

    dropzone.on('maxfilesexceeded', function(file){
        dropzone.removeAllFiles();
        dropzone.addFile(file);
    });

    function addOutputCard(dataURL) {
        $('#imageInput').html('<img class="img-fluid" src="'+ dataURL+'">');
    }


});