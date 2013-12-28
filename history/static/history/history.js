history=new Page("async/history/",buildHistory);
function Entry(evnt) {
    var base=$("<div></div>").addClass("workshops_exchanges type-workshops_exchanges status-publish hentry finished");
    var headline=$("<h2></h2>").html('<a href="#">'+evnt.name+'</a>');
    var trainers=$("<div></div>").html("<span>"+evnt.trainers+"</span>");
    var desc=$("<div></div>").text(evnt.description);
    var bottom=$("<img>").attr('src', 'http://eestec-lj.org/wp-content/themes/neutral/img/line.png');
    var br=$("<br/>");
    base.append(headline,trainers,desc,bottom,br).appendTo("#"+evnt.type);
}
function buildHistory(){
    $("#training").empty();
    $("#operational").empty();
    $.each( history, function( key, val ) {
        Entry(val.fields);
    });
}
$(function(){
    getEvents();
    $("#button-operational").click(function(){
        current("operational");
        history.fetch();
    });
    $("#button-training").click(function(){
        current("training");
        history.fetch();
    });
});
