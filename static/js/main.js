//
jQuery(document).ready(function ($) {
  $(".live-search-list tr").each(function () {
    $(this).attr("data-search-term", $(this).text().toLowerCase());
  });

  $(".live-search-box").on("keyup", function () {
    var searchTerm = $(this).val().toLowerCase();

    $(".live-search-list tr").each(function () {
      if (
        $(this).filter("[data-search-term *= " + searchTerm + "]").length > 0 ||
        searchTerm.length < 1
      ) {
        $(this).show();
      } else {
        $(this).hide();
      }
    });
  });
});

//
$(function () {
  var $ppc = $(".progress-pie-chart"),
    percent = parseInt($ppc.data("percent")),
    deg = (360 * percent) / 100;
  if (percent > 50) {
    $ppc.addClass("gt-50");
  }
  $(".ppc-progress-fill").css("transform", "rotate(" + deg + "deg)");
  $(".ppc-percents span").html(percent + "%");
});

//
$(function () {
  $(".chart").easyPieChart({
    size: 130,
    barColor: "#065fd4",
    scaleLength: 0,
    lineWidth: 10,
    trackColor: "#f1f1f1",
    lineCap: "circle",
    animate: 2000,
  });
});

// show Login error message
function showMessage() {
  document.getElementById("msg").style.visibility = "hidden";
}
setTimeout("showMessage()", 3000);
