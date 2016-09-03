$(document).ready(function() {
  // sort the list
  var ls = $(".item");
  ls.sort(function(a,b) {
    return $(a).children("h3").text().localeCompare($(b).children("h3").text());
  });

  $(ls).each(function(n, el) {
    $("#main_content").append(el);
  });
  $("#cw-num").text($(ls).length);

  $("#search-input").keyup(function() {
    var t = $("#search-input").val();
    // console.log($("#search-input").val());
    $(".item").each(function(n, el) {
      if($(el).children("h3").text().indexOf(t) == -1) {
        $(el).fadeOut("fast");
      } else {
        $(el).fadeIn("fast");
      }
    });
  });
});