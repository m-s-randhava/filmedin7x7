/**
 * Created by mohanrandhava on 9/12/14.
 */

$(function() {
  function log(message) {
      $("<div>").text(message).prependTo("#log");
      $("#log").scrollTop(0);
  }

  $("#birds").autocomplete({
          source: "film/locations/autocomplete",
          minLength: 2,
          select: function (event, ui) {
              console.log(ui.item ?
                      "Selected: " + ui.item.value + " aka " + ui.item.id :
                      "Nothing selected, input was " + this.value);
          }
      });
});