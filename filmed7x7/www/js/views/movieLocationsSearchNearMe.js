/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app.movieLocationsSearchNearMeView = Backbone.View.extend({
    el: '.col-md-4',

    events: {
        'click #search': 'doSearch'
    },

    initialize: function( ) {
        this.innerResultsView = new app.movieLocationsNearMeView( {
            collection: this.collection
        } );
    },

    doSearch: function(target) {
        $('#results_list_container').show();
        $('#results_info').hide();

        console.log("Finding nearest 7 locations to me ...");

        // Try W3C Geolocation (Preferred)
        var foundLocation;

        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(collection) {
                return function(position) {
                    foundLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);

                    console.log("pLat:   " + position.coords.latitude);

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

                    collection.fetch( {
                        reset: true,
                        error: function(model, xhr, options) {
                            this.reset();
                        }.bind(collection)
                    } );

                };
            } (this.innerResultsView.collection), null);
        }
        else {
            alert("Sorry, we could not find your location.");
        }

    }
});