/**
 * Created by mohanrandhava on 9/12/14.
 */

$( document ).ready(function() {
    function log(message) {
      $("<div>").text(message).prependTo("#log");
      $("#log").scrollTop(0);
    };

    $("#search_location").autocomplete({
          source: "http://10.0.1.5:5000/film/locations/autocomplete",
          minLength: 2,
          select: function (event, ui) {
              console.log(ui.item ?
                      "Selected: " + ui.item.value + " aka " + ui.item.id :
                      "Nothing selected, input was " + this.value);
          }
    });
});