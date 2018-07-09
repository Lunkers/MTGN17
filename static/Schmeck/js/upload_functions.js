uploadMedia = function() {
    // funktion för uppladning av bilder till servern
    var outputData = [];
    var fileSelect = document.getElementById("files");
    var files = fileSelect.files;
    var name = $("#name").val(); // den som laddar upp bilderna
    var week = $("#week").val(); // veckan bilden togs
    var event = $("#event").val(); // eventet bilden togs under
    var links = $("#videos").val();
    var linkList = links.split(","); 
    linkList = linkList.filter(v =>v!="");
    var form_data = new FormData();

    for (var i = 0; i < files.length; i++ ){
        var file = files[i];
        form_data.append("files", file, file.name)
    }
    form_data.append("uploadedby", name);
    form_data.append("week", week);
    form_data.append("event", event);
    
    
    for (var j = 0; j < linkList.length; j++ ){
        var link = linkList[j];
        form_data.append("videos", link);
    }
    console.log(form_data.get("videos"));
    $.ajax({
        url: "/api/media",
        type: "POST",
        data: form_data,
        contentType: false, 
        processData:false,
        success: function(){
            window.location.href = "/media";
        }
    })
};

uploadDocument = function(){
    var fileSelect = document.getElementById("files");
    var files = fileSelect.files;
    

    var form_data = new FormData();

    for (var j = 0; j < files.length; j++){
        var file = files[j];
        console.log(file);
        form_data.append("files", file, file.name);
    }

    $.ajax({
        url: "/api/blandaren",
        type: "POST",
        data: form_data,
        contentType: false,
        processData: false,
       
    })
};