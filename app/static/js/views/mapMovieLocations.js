/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

/**
 *  Creates a Backbone.js view bound to the '.col-md-8' of
 *  the right pane view.  It is tied to a collection that queries
 *  the backend for films with locations matching the searched for
 *  words or phrase:
 *
 *      collectionMovieLocations (collections/movieLocations.js)        =>  FilmsAtLocationsAPI
 *
 */
app.mapMovieLocationsView = Backbone.View.extend({
    el: '.col-md-8',
    map_centroid: new google.maps.LatLng(37.780870, -122.419204), //center that map defaults to (San Francisco City Hall)

    initialize: function( ) {
        //  Listen to 'reset' events on collection and then render
        this.listenTo( this.collection, 'reset', this.render);
    },

    reset: function() {
        //  Initialize map settings, centered on SF City Hall
        var myOptions = {
            zoom: 13,
            center: this.map_centroid,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        //  New Google Map
        map = new google.maps.Map($("#map_canvas")[0], myOptions);
    },

    //  Render a new map with any associated markers
    render: function() {
        //  Initialize map settings, centered on SF City Hall
        var myOptions = {
          zoom: 13,
          center: this.map_centroid,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        map = new google.maps.Map($("#map_canvas")[0],myOptions);

        /**
        * Data for the markers consisting of a name, a LatLng and a zIndex for
        * the order in which these markers should display on top of each
        * other.
        */

        //  Icons for the markers
        var mLIcons = ["filmlocationA.png","filmlocationB.png","filmlocationC.png","filmlocationD.png","filmlocationE.png","filmlocationF.png","filmlocationG.png","filmlocationH.png","filmlocationI.png","filmlocationJ.png"];

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
                    return [item.get("Title"), location["lat"], location["lng"], ++index, image, item];
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

                //  Add clickable film location info for map icon
                var contentString = '<div id="content">'+
                  '<div id="siteNotice">'+
                  '</div>'+
                  '<h1 id="firstHeading" class="firstHeading">' + location[5].get('Title') + '</h1>'+
                  '<div id="bodyContent">'+
                  '<p><b>Production Company:  </b>' + location[5].get('Production Company') + '</p>'+
                  '<p><b>Locations:     </b>' + location[5].get('Locations') + '</p>'+
                  '<p><b>Director:      </b>' + location[5].get('Director') + '</p>'+
                  '<p><b>Actor 1:       </b>' + location[5].get('Actor 1') + '</p>'+
                  '<p><b>Actor 2:       </b>' + location[5].get('Actor 2') + '</p>'+
                  '<p><b>Actor 3:       </b>' + location[5].get('Actor 3') + '</p>'+
                  '<p><b>Fun Facts:     </b>' + location[5].get('Fun Facts') + '</p>'+
                  '<p><b>Distributor:   </b>' + location[5].get('Distributor') + '</p>'+
                  '<p><b>Release Year:  </b>' + location[5].get('Release Year') + '</p>'+
                  '<p><b>Writer:        </b>' + location[5].get('Writer') + '</p>'+
                  '</div>'+
                  '</div>';

                var infowindow = new google.maps.InfoWindow({
                  content: contentString,
                  maxWidth: 200
                });

                //  A listener to display info window for content
                google.maps.event.addListener(marker, 'click', function (marker, infowindow) {
                    return function() {
                        infowindow.open(map,marker);
                    }
                }(marker, infowindow)); //  Closure ...
            }
        }

        //  Add markers to map
        setMarkers(map, locations);
    }

});