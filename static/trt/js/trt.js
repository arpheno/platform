function current(which) {
    history.pushState({"which": which}, which, "/" + which + "/");
    $("section").hide("slow");
    $("section."+which).show("slow");
}
function linkbutton(name){
    $("button."+name).click(function(){
        current(name);
        $("section."+name).load("/"+name);
        return false;
    });
};
function Page(which) {
    // url: string - URL from which to fetch data;
    // rebuild: function - function which builds html from container;
    var self = this;
    self.lastModified = 0;
    self.newModified = 0;
    self.which = which;
    self.fetch = function () {
        // Public function to keep page data up-to-date.
        $.ajax({
            type: "HEAD",
            async: true,
            url: "/" + self.which +  "/",
            success: self._check,
        });
    }
    self._check = function (message, text, response) {
        // Method will check if data still up-to-date with a HEAD request.
        console.log("Checking " + self.which + " for new data.");
        var header = response.getResponseHeader("Last-Modified");
        self.newModified = Date.parse(header);
        if (self.newModified > self.lastModified) {
            console.log(self.which + " is out of date, getting new Data.");
            $("section."+self.which).load("/" + which + "/")
            console.log("Got new data for "+self.which);
            self.lastModified = self.newModified;
        }
    }
}
$(function () {
    // Deal with basic event binding(history)
    window.addEventListener('popstate', function(event) {
        if (event.state!= null){
            console.log('popstate fired!');
            $("section").hide();
            $("section."+event.state['which']).show();
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

        Training = new Page("training");
        Pool = new Page("pool");
        News = new Page("news");
        linkbutton("materials");
        linkbutton("account");
        Training.fetch();
        Pool.fetch();
        News.fetch();
        $("button.pool").click(function () {
            current("pool");
            Pool.fetch();
            return false;
        });
        $("button.training").click(function () {
            current("training");
            Training.fetch();
            return false;
        });
        $("button.news").click(function () {
            current("news");
            News.fetch();
            return false;
        });
        $("button.contact").click(function () {
            current("contact");
            return false;
        });
        $("button.logout").click(function () {
            current("news");
            $("body").load("/account/logout/")
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
