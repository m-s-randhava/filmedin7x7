/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

/**
 *  Creates a Backbone.js view bound to the '.col-md-8' of
 *  the right pane view.  It is tied to a collection that queries
 *  the backend for 7 movies with near the user's current position
 *  in the world:
 *
 *      collectionMovieLocationsNearMe (collections/7MovieLocationsNearMe.js)  =>  FindNearestFilmsAtLocationAPI
 *
 */
app.mapNearestLocationsToMe = Backbone.View.extend({
    el: '.col-md-8',

    initialize: function( ) {
        //  Listen to 'reset' events on collection and then render
        this.listenTo( this.collection, 'reset', this.render);
    },

    render: function() {
        //  Current position of user in the world
//        var myLatLng = new google.maps.LatLng(this.collection.lat, this.collection.lng);
        var myLatLng = new google.maps.LatLng(37.779390, -122.418432);

        //  Initialize map settings, centered on SF City Hall
        var myOptions = {
          zoom: 13,
          center: myLatLng,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        //  New Google Map
        map = new google.maps.Map($("#map_canvas")[0],myOptions);

        /**
         * Data for the markers consisting of a name, a LatLng and a zIndex for
         * the order in which these markers should display on top of each
         * other.
         */

        //  Icons for the markers
        var mLIcons = [ "filmlocationA.png","filmlocationB.png","filmlocationC.png",
                        "filmlocationD.png","filmlocationE.png","filmlocationF.png",
                        "filmlocationG.png","filmlocationH.png","filmlocationI.png",
                        "filmlocationJ.png"];

        //  Create a set of images for each marker to place on map
        var locations = this.collection.map(
            function(mLIcons, index) {
                return function(item) {
                    var image = {
                        url: 'static/img/' + mLIcons[index],
                        // This marker is 20 pixels wide by 32 pixels tall.
                        size: new google.maps.Size(40, 40),
                        // The origin for this image is 0,0.
                        origin: new google.maps.Point(0,0),
                        // The anchor for this image is the base of the flagpole at 0,32.
                        anchor: new google.maps.Point(0, 40)
                    };
                    var location = item.get("location");
                    return [item.get("Title"), location["lat"], location["lng"], ++index, image];
                };
            }(mLIcons, 0)
        );

        //  Add markers to the map
        function setMarkers(map, locations) {
          // Add markers to the map
            console.log("Number of markers:   " + locations.length)
                for (var i = 0; i < locations.length; i++) {
                var location = locations[i];
                var myLatLng = new google.maps.LatLng(location[1], location[2]);
                var marker = new google.maps.Marker({
                    position: myLatLng,
                    map: map,
                    animation: google.maps.Animation.DROP,
                    icon: location[4],
                    title: location[0],
                    zIndex: location[3]
                });
            }
        }

        //  Mark user's current position
        function setMyPositionMarker(map, myLatLng) {
            // Add markers to the map
            var marker = new google.maps.Marker({
                position: myLatLng,
                map: map,
                animation: google.maps.Animation.DROP,
                icon: 'static/img/blue-pushpin.png',
                title: 'I am here.',
                zIndex: 11
            });
        }

        //  Mark 7 seven nearest films and user's position
        setMarkers(map, locations);
        setMyPositionMarker(map, myLatLng);
    }
});