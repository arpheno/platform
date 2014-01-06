function Page(url, rebuild) {
    // url: string - URL from which to fetch data;
    // rebuild: function - function which builds html from container;
    var self = this;
    self.container = []; // Data fetched will be saved here
    self.lastModified = 0;
    self.newModified = 0;
    self.url = url;
    self.rebuild = rebuild;
    self.fetch = function () {
        // Public function to keep page data up-to-date.
        $.ajax({
            type: "HEAD",
            async: true,
            url: self.url,
            success: self._check,
        });
    }
    self._check = function (message, text, response) {
        // Method will check if data still up-to-date with a HEAD request.
        console.log("Checking " + self.url + " for new data.");
            var header = response.getResponseHeader("Last-Modified");
        self.newModified = Date.parse(header);
        if (self.newModified > self.lastModified) {
            $.getJSON(url, self._hardfetch);
        }
    }
    self._hardfetch = function (data, status, xhr) {
        // Method will fetch new data if the current is old.
        console.log(self.url + " is out of date, getting new Data.");
        self.lastModified = self.newModified;
        self.container = data;
        self.rebuild();
    }
}
function current(which) {
    history.pushState({"which": which}, which, "/" + which + "/");
    $("section").hide("slow");
    $("section#"+which).show("slow");
}
function Event(evnt) {
    var base = $("<article>").addClass("workshops_exchanges type-workshops_exchanges status-publish hentry finished");
    var headline = $("<h2></h2>").html('<a href = "#">'+evnt.name+'</a>');
    var trainers = $("<div></div>").html("<span>"+evnt.trainers+"</span>");
    var desc = $("<div></div>").text(evnt.description);
    var bottom = $("<img>").attr('src', 'http://eestec-lj.org/wp-content/themes/neutral/img/line.png');
        var br = $("<br/>");
    return base.append(headline , trainers , desc , bottom , br);
}
function Trainer(data){
    var pass=data;
    var base=$("<li></li>").addClass("user-image");
    var image=new Image();
    image.src=data.im;
    var meta = $("<div></div>").addClass("comment");
    var il = $("<ul></ul>")
    $.each(data.meta, function (key, val) {
        il.append($("<li></li>").html(key + ": "+ val));
    });
    base.click(function(){
        buildtrainer(pass);
        current('profile');
    });
    return base.append( image, meta.append(il))
}
function New(entry) {
    var base = $("<article></article>");
    var headline = $("<h2></h2>").text(entry.headline)
    var pub = $("<ul></ul>").html('<li>' + entry.pub_date + '</li>');
    var content = $("<p></p>").addClass("post_content").html(entry.message);
    var meta = $("<div></div>").addClass("post_meta").html(' <div class="post_meta"> <ul class="clearfix"> <li class="post_category"> Published in <a href="#" title="View all posts in News" rel="category tag">News</a>, <a href="#" title="View all posts in TrainingTeam" rel="category tag">Training Team</a> </li> </ul> </div>');
    return base.append(headline, pub, content, meta);
}
function buildtrainer(data) {
    $("section#profile").empty();
    var base=$("<li></li>");
    var image=new Image();
    image.src=data.im;
    var meta = $("<div></div>");
    var il = $("<ul></ul>");
    $.each(data.meta, function (key, val) {
        il.append($("<li></li>").html(key + ": "+ val));
    });
    $("section#profile").append(base.append(image, il));
}
function buildpool() {
    $("section#pool").html('<h2 class="post_title">Trainers</h2><ul></ul>');
    $.each(Pool.container, function (key, val) {
        if(val.im=="None"){;
        }else{
            $("section#pool ul").append(new Trainer(val));
        }
    });
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
        Pool = new Page("/async/pool/", buildpool);
        News.fetch()
        Pool.fetch()
        Events.fetch()

        // Form binding
        $("#signup").submit(function() {
            $("#loader").show();
            $.ajax({
                type: "POST",
                url: "/account/register/",
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
        $("button#contact").click(function(){
            current("contact"); return false
        });
        $("button#pool").click(function () {
            current("pool");
            Events.fetch();
            return false;
        });$("button#operational").click(function () {
            current("operational");
            Events.fetch();
            return false;
        });
        $("button#training").click(function () {
            current("training");
            Events.fetch();
            return false;
        });
        $("button#logout").click(function () {
            current("news");
            $("body").load("/account/logout/")
            News.fetch();
            return false;
        }); $("button#news").click(function () {
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
