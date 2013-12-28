function Page(url, rebuild){
    // url: string - URL from which to fetch data;
    // rebuild: function - function which builds html from container;
    this.container=[]; // data fetched will be saved here
    this.lastModified=0;
    this.url=url;
    this.target=target;
    this.element=element;
    function fetch(){
        $.ajax({
            type: "HEAD",
            async: true,
            url: this.url,
            success: function(message,text,response){
                var newModified = response.getResponseHeader("Last-Modified");
                var newModified = new Date(Date.parse(lm));
                if(lm > cversion){
                    $.getJSON(url, function(data,status,xhr){
                        this.lastModified = xhr.getResponseHeader("Last-Modified");
                        this.lastModified = new Date(Date.parse(cversion));
                        this.container=data;
                        rebuild();
                    });
                }
            }
        });
    }
}
function current(which){
    $(".contents").hide();
    $("#"+which).show();
}
