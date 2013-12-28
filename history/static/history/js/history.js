function Entry(evnt) {
    var base = $("<div></div>").addClass("workshops_exchanges type-workshops_exchanges status-publish hentry finished");
    var headline = $("<h2></h2>").html('<a href = "#">'+evnt.name+'</a>');
    var trainers = $("<div></div>").html("<span>"+evnt.trainers+"</span>");
    var desc = $("<div></div>").text(evnt.description);
    var bottom = $("<img>").attr('src', 'http://eestec-lj.org/wp-content/themes/neutral/img/line.png');
    var br = $("<br/>");
    base.append(headline , trainers , desc , bottom , br).appendTo("#"+evnt.type);
}
function buildtrtevents(){
    $("#training").empty();
    $("#operational").empty();
    $.each( trtevents.container, function( key, val ) {
        Entry(val.fields);
    });
}
$(function(){
    trtevents = new Page("/async/events/", buildtrtevents);
    trtevents.fetch()
    $("#button-operational").click(function(){
        current("operational");
        trtevents.fetch();
        return false;
    });
    $("#button-training").click(function(){
        current("training");
        trtevents.fetch();
        return false;
    });
});
