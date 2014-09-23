/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

/**
 *  Creates a Backbone.js view bound to the '.col-md-4' of
 *  the left pane view.  It is tied to a collection that queries
 *  the backend for 7 movies with near the user's current position
 *  in the world:
 *
 *      collectionMovieLocationsNearMe (collections/7MovieLocationsNearMe.js)  =>  FindNearestFilmsAtLocationAPI
 *
 */
app.movieLocationsSearchNearMeView = Backbone.View.extend({
    el: '.col-md-4',

    //  Bind to the search text box's 'click' event and
    //  call doSearch
    events: {
        'click #search': 'doSearch'
    },

    initialize: function( ) {
        /**
         *  Creates a Backbone.js inner view.  It is tied to a collection that
         *  queries the backend for 7 movies with near the user's current position
         *  in the world:
         *
         *      collectionMovieLocationsNearMe  =>  FindNearestFilmsAtLocationAPI
         *
         */
        this.innerResultsView = new app.movieLocationsNearMeView( {
            collection: this.collection
        } );
    },

    //  Tells the collection to fetch the 7 closest movies filmed
    //  near this current lcoation
    doSearch: function(target) {
        //  Show the results pane
        $('#results_list_container').show();
        //  Hide the pagination and info pane, since 7 results are
        //  always returned and pagination not needed
        $('#results_info').hide();

        console.log("Finding nearest 7 locations to me ...");

        // Try W3C Geolocation (Preferred)
        var foundLocation;

        //  Leveraging the device's 'navigator' object if available
        if(navigator.geolocation) {
            //  Get current position and call callback
            navigator.geolocation.getCurrentPosition(function(collection) {
                return function(position) {
                    //  Use google to create a Lat/Lng tuple
                    foundLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);

                    console.log("pLat:   " + position.coords.latitude);

                    //  We need to get sign of coordinates and store separately,
                    //  since ultimately the call to the API will be made with
                    //  the absolute value of both Lat/Lng due to a quirk in the
                    //  API's framework implementation.
                    if (position.coords.latitude >= 0) {
                        collection.lat_sign = "p"
                    } else {
                        collection.lat_sign = "n"
                    }
                    collection.lat = position.coords.latitude;

                    console.log("pLng:   " + position.coords.longitude);

                    if (position.coords.longitude >= 0){
                        collection.lng_sign = "p"
                    } else {
                        collection.lng_sign = "n"
                    }
                    collection.lng = position.coords.longitude;

                    //  Call the Nearest API
                    collection.fetch( {
                        reset: true,
                        error: function(model, xhr, options) {
                            this.reset();   // Simply reset on error
                        }.bind(collection) //   Closure ...
                    } );

                };
            } (this.innerResultsView.collection), null); // Closure ...
        }
        else {
            alert("Sorry, we could not find your location.");
        }

    }
});