/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

$( function() {
    /**
     *  jQuery 'autocomplete' and bootstrap do not play well together.
     *  Hides a spurious 'autocomplete' element that appears at base of window.
     */
    $('.ui-helper-hidden-accessible').hide();

    /**
     *  Hide the results list and pagination information at first load.
     */
    $('#results_list_container').hide();
    $('#results_info').hide();

    /**
     *  Assumption: Bootstrap.css has split the window into 2, panes left and right.
     */

    /**
     *  Creates 2 Backbone.js collections tied to the backend API that
     *  are central to all UI functionality:
     *      collectionMovieLocations (collections/movieLocations.js)        =>  FilmsAtLocationsAPI
     *      collectionMovieLocationsNearMe (collections/7MovieLocationsNearMe.js)  =>  FindNearestFilmsAtLocationAPI
     */
    var collectionMovieLocations = new app.movieLocations();
    var collectionMovieLocationsNearMe = new app._7MovieLocationsNearMe();

    /**
     *  Creates Backbone.js view bound to the left portion of the app,
     *  that contains the 'autocomplete' search text field, the results pane,
     *  and pagination widget.
     *
     *  It is bound to the collection that fetches full film metadata by location.
     */
    var searchView = new app.movieLocationsSearchView({
        collection: collectionMovieLocations
    });

    /**
     *  Creates Backbone.js view bound to the the 'Find7NearestMe'
     *  button.
     *
     *  It is bound to the collection that fetches 7 nearby films to a user's
     *  current position in the world.
     */
    var searchNearMeView = new app.movieLocationsSearchNearMeView({
        collection: collectionMovieLocationsNearMe
    });

    /**
     *  Creates Backbone.js view bound to the the right pane,
     *  containing the Google Map, responsible for displaying results
     *  of 'autocomplete' or 'user-entered' searches.
     *
     *  It is also bound to the collection that fetches full film metadata by
     *  location.
     */
    var mapMovieLocationsView = new app.mapMovieLocationsView({
        collection: collectionMovieLocations
    });

    /**
     *  Creates another Backbone.js view bound to the the right pane,
     *  containing the Google Map, responsible for displaying results
     *  of clicking 'Find7NearestMe' button.
     *
     *  It is also bound to the collection that fetches full film metadata by
     *  location.
     */
    var mapNearestLocationsToMeView = new app.mapNearestLocationsToMe({
        collection: collectionMovieLocationsNearMe
    });

    /**
     *  Binds the jQuery Autocomplete functionality to the input text
     *  search field, which will send any entered text, as it is entered,
     *  to the collectionMovieLocations as a call to its 'doSearch'
     *  method which will result in results being fetched nearly
     *  instantaneously as you type.
     */
    $("#search_location").autocomplete(function(typed, searchView){
        return {
            //  url of the AutocompleteAPI
            //  jQuery autocomplete passes the entered text as a
            //  query parameter 'term' of this request.
            source: "film/locations/autocomplete",
            response: function( event, ui ) {
                console.log("autocomplete response called ...");
                //  jQuery 'autocomplete' and bootstrap do not play well together.
                //  Hides a spurious 'autocomplete' element that appears at base of window.
                $('.ui-helper-hidden-accessible').hide();
                //  Reset whether the user selected something via the autocomplete
                //  dropdown or typed it in manually
                searchView.collection.ac_selected = 'False';
                //  Tell the collection to fetch results for what was entered now.
                searchView.doSearch($('#search_location').val());
            },
            select: function ( event, ui ) {
                console.log("autocomplete select called ...");
                //  jQuery 'autocomplete' and bootstrap do not play well together.
                //  Hides a spurious 'autocomplete' element that appears at base of window.
                $('.ui-helper-hidden-accessible').hide();
                //  Set the flag indicating the user selected something
                // via the autocomplete dropdown
                searchView.collection.ac_selected = 'True';
                //  Tell the collection to fetch results for what was selected now.
                searchView.doSearch(ui.item.value);
                console.log("autocomplete select search completed ...");
                console.log(ui.item ?
                      "Selected: " + ui.item.value + " aka " + ui.item.id :
                      "Nothing selected, input was " + this.value);
            }
        }
    }($("#search_location").val(),searchView)); //  Closure ...

    //  Needed to detect user events in the text field itself, for the
    //  purposes of resetting the entire view if the field was cleared.
    $("#search_location").bind("propertychange keyup input paste", function(mapView,searchView){
       return function(event){
           console.log("input events called ...");
           console.log("input changed...");
           //   If field is empty, reset the view
           //   by telling the collection to fetch nothing
           if (event.target.value.length == 0) {
                //  Reset whether the user selected something via the autocomplete
                //  dropdown or typed it in manually
               searchView.collection.ac_selected = false;
               searchView.doSearch(event.target.value);
           }
       };
    }(mapMovieLocationsView,searchView)); //  Closure ...


});