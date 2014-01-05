function Page(url, rebuild) {
    // url: string - URL from which to fetch data;
    // rebuild: function - function which builds html from container;
    var self = this;
    self.container = []; // data fetched will be saved here
    self.lastModified = 0;
    self.newModified = 0;
    self.url = url;
    self.rebuild = rebuild;
    self.hardfetch = function (data, status, xhr) {
        console.log(self.url + " is out of date, getting new Data.");
        self.lastModified = self.newModified;
        self.container = data;
        self.rebuild();
    }
    self.check = function (message, text, response) {
        console.log("Checking " + self.url + " for new data.");
        var header = response.getResponseHeader("Last-Modified");
        self.newModified = new Date(Date.parse(header));
        if (self.newModified > self.lastModified) {
            $.getJSON(url, self.hardfetch);
        }
    }
    self.fetch = function () {
        $.ajax({
            type: "HEAD",
            async: true,
            url: self.url,
            success: self.check,
        });
    }
}
function current(which) {
    history.pushState({"which": which}, which, "/" + which + "/");
    $("section").hide();
    $("section#"+which).show();
}
function Event(evnt) {
    var base = $("<div></div>").addClass("workshops_exchanges type-workshops_exchanges status-publish hentry finished");
    var headline = $("<h2></h2>").html('<a href = "#">'+evnt.name+'</a>');
    headline.addClass("post_title");
    var trainers = $("<div></div>").html("<span>"+evnt.trainers+"</span>");
    var desc = $("<div></div>").text(evnt.description);
    var bottom = $("<img>").attr('src', 'http://eestec-lj.org/wp-content/themes/neutral/img/line.png');
    var br = $("<br/>");
    return base.append(headline , trainers , desc , bottom , br);
}

function New(entry) {
    var base = $("<div></div>").addClass("post");
    var headline = $("<h2></h2>").html('<a href="#">' + entry.headline + '</a>');
    headline.addClass("post_title");
    var pub = $("<ul></ul>").html('<li>' + entry.pub_date + '</li>');
    var content = $("<div></div>").addClass("post_content").html(entry.message);
    var meta = $("<div></div>").addClass("post_meta").html(' <div class="post_meta"> <ul class="clearfix"> <li class="post_category"> Published in <a href="#" title="View all posts in News" rel="category tag">News</a>, <a href="#" title="View all posts in TrainingTeam" rel="category tag">Training Team</a> </li> </ul> </div>');
    return base.append(headline, pub, content, meta);
}
function buildnews() {
    $("section#news").empty();
    $.each(News.container, function (key, val) {
        $("section#news").append(new New(val.fields));
    });
}
function buildevents(){
    $("section#training").empty();
    $("section#operational").empty();
    $.each( Events.container, function( key, val ) {
        $("section#"+val.fields.type).append(new Event(val.fields));
    });
}
function linkbutton(name){
    $("button#"+name).click(function(){
        current(name);
        $("section#"+name).load("/"+name);
        return false;
    });
};
$(function () {
    // Deal with basic event binding(history)
    window.addEventListener('popstate', function(event) {
        if (event.state!= null){
            console.log('popstate fired!');
            $("section").hide();
            $("section#"+event.state['which']).show();
        }});
    $(document).mouseup(function (e){
        e.preventDefault();
        var container = $("button.signin");

        if (!container.is(e.target) // if the target of the click isn't the container...
            && container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            $("#signin_menu").hide("slow");
        }
        var con = $("button.signup");

        if (!con.is(e.target) // if the target of the click isn't the container...
            && con.has(e.target).length === 0) // ... nor a descendant of the container
        {
            $("#signup_menu").hide("slow");
        }
    });
    //// Set up content retrieval
    News = new Page("/async/news/", buildnews);
    Events = new Page("/async/events/", buildevents);
    News.fetch()
    Events.fetch()

    // Form binding
    $("#signup").submit(function() {
            $("#loader").show();
            $.ajax({
                type: "POST",
                url: "{% url 'register' %}",
                data: $("#signup").serialize(), // serializes the form's elements.
                success: function(data){
                    $("#loader").hide();
                    if(data.status=="success"){
                        alert("Please check your email to activate your account.");
                        $("fieldset#signup_menu").hide("slow");
                        $("fieldset#signin_menu").show("slow");
                    }else if(data.status=="failure"){
                        alert("This email is already registered.");
                    }else if(data.status=="notatrainer"){
                        alert("The eestec Training Team platform is currently in beta, and only available to EESTEC trainers and EESTEC training candidates. If you are a trainer and are seeing this message, please make sure you register your account with the email adress you're registered with on the trainings@eestec.net mailing list. If the problem persists, please contact the admin at arpheno@gmail.com.");
                    }
                }
            });
            return false; // avoid to execute the actual submit of the form.
        });
    $("#signin").submit(function() {
        console.log("LOL");
            $.ajax({
                type: "POST",
                url: "/account/login/",
                data: $("#signin").serialize(), // serializes the form's elements.
                success: function(data){
                    if(data.status=="success"){
                        $(".authed").show("slow");
                        $(".anon").hide("slow");
                        if(data.staff==true){
                        $(".staffed").show("slow");
                        }
                    }else if(data.status=="inactive"){
                        alert("Your account has been deactivated. Please Contact the system administrator.");
                        $("#signin_menu").hide("slow");
                    }
                    else{
                        alert("No such combination of E-Mail and Password. Please try again");
                        $(".userinput").val("");
                    }
                }
            });
            return false; // avoid to execute the actual submit of the form.
        });
    // Bind buttons

    linkbutton("materials");
    linkbutton("account");
    linkbutton("pool");
    $("button#contact").click(function(){
        current("contact"); return false
    });
    $("button#operational").click(function () {
        current("operational");
        Events.fetch();
        return false;
    });
    $("button#training").click(function () {
        current("training");
        Events.fetch();
        return false;
    });
    $("button#news").click(function () {
        current("news");
        News.fetch();
        return false;
    });
    $(".signin").click(function(e) {
        $("fieldset#signin_menu").show("slow");
    });
    $("button.signup").click(function(e) {
        $("fieldset#signup_menu").show("slow");
    });
});
