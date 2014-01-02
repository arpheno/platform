function NEntry(entry) {
    var base=$("<div></div>").addClass("post");
    var headline=$("<h2></h2>").html('<a href="#">'+entry.headline+'</a>');
    headline.addClass("post_title");
    var pub=$("<ul></ul>").html('<li>'+entry.pub_date+'</li>');
    var content=$("<div></div>").addClass("post_content").html(entry.message);
    var meta=$("<div></div>").addClass("post_meta").html(' <div class="post_meta"> <ul class="clearfix"> <li class="post_category"> Published in <a href="#" title="View all posts in News" rel="category tag">News</a>, <a href="#" title="View all posts in TrainingTeam" rel="category tag">Training Team</a> </li> </ul> </div>');
    base.append(headline,pub,content,meta).appendTo("#news");
}
function buildtrtnews(){
    $("#news").empty();
    $.each( trtnews.container, function( key, val ) {
        NEntry(val.fields);
    });
}
$(function(){
    trtnews = new Page("/async/news/", buildtrtnews);
    trtnews.fetch()
    $("#button-news").click(function(){
        current("news");
        trtnews.fetch();
    });
});
