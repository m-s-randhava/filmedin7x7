/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

$( function() {
    $('.ui-helper-hidden-accessible').hide();

    $('#results_list_container').hide();
    $('#results_info').hide();

    var collection = new app.movieLocations();

    new app.movieLocationsSearchView({
        collection: collection
    });

    new app.mapMovieLocationsView({
        collection: collection
    });

});