$(document).ready(function () {
    // Side Nav Bar
    $("#open-nav-btn").click(function () {         
        $("#side-navbar").removeClass("translate-x-[-100%]");
        $("#side-navbar").addClass("translate-x-0");
    });

    $("#close-nav-btn").click(function () { 
        console.log("clicked");
        $("#side-navbar").removeClass("translate-x-0");
        $("#side-navbar").addClass("translate-x-[-100%]");
        
    });

    // Profile Dropdown
    $("#profile-nav").hover(function () {
            // over
            $("#profile-dropdown").removeClass("hidden");
            
        }, function () {
            // out
            setTimeout(() => {
                $("#profile-dropdown").addClass("hidden"); 
            }, 1000);
            
        }
    );
});