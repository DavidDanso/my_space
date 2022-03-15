$(".toggle-password").click(function () {
  $(this).toggleClass("fa-eye fa-eye-slash");
  var input = $($(this).attr("toggle"));
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});

// show Login error message
function showMessage() {
  document.getElementById("msg").style.visibility = "hidden";
}
setTimeout("showMessage()", 3000);

//
//Query All input fields
var form_fields = document.getElementsByTagName("input");
form_fields[1].placeholder = "Username..";
form_fields[2].placeholder = "Email..";
form_fields[3].placeholder = "Enter password...";
form_fields[4].placeholder = "Re-enter Password...";
