/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

$( function() {
    $('.ui-helper-hidden-accessible').hide();

    $('#results_list_container').hide();
    $('#results_info').hide();

    var collection = new app.movieLocations();

    var searchView = new app.movieLocationsSearchView({
        collection: collection
    });

    var mapMovieLocationsView = new app.mapMovieLocationsView({
        collection: collection
    });

    $("#search_location").autocomplete(function(typed, searchView){
        return {
            source: "film/locations/autocomplete",
//            minLength: 2,
            response: function( event, ui ) {
                console.log("autocomplete response called ...");
                $('.ui-helper-hidden-accessible').hide();
                searchView.doSearch($('#search_location').val());
            },
            select: function ( event, ui ) {
                console.log("autocomplete select called ...");
                $('.ui-helper-hidden-accessible').hide();
                searchView.doSearch(ui.item.value);
                console.log("autocomplete select search completed ...");
                console.log(ui.item ?
                      "Selected: " + ui.item.value + " aka " + ui.item.id :
                      "Nothing selected, input was " + this.value);
            }
        }
    }($("#search_location").val(),searchView));

  // Look for changes in the value
   $("#search_location").bind("propertychange keyup input paste", function(mapView,searchView){
       return function(event){
           console.log("input events called ...");
           console.log("input changed...");
           if (event.target.value.length == 0) {
//               mapView.reset();
               searchView.doSearch(event.target.value);
           }
       };
   }(mapMovieLocationsView,searchView));

//    $("#search_location").bind("change", function(mapView){
//        return function (e) {
//            console.log("input value:  " + e.target.value);
//            console.log("input value length:  " + e.target.value.length);
//
//            if(e.target.value.length == 0) {
//                mapView.render(true);
//            }
//        }
//    }(mapMovieLocationsView));

});