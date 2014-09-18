/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

app.mapNearestLocationsToMe = Backbone.View.extend({
    el: '.col-md-8',

    initialize: function( ) {
        this.listenTo( this.collection, 'reset', this.render);
    },

    render: function() {
        var myOptions = {
          zoom: 13,
          center: MapsLib.map_centroid,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        map = new google.maps.Map($("#map_canvas")[0],myOptions);

        /**
         * Data for the markers consisting of a name, a LatLng and a zIndex for
         * the order in which these markers should display on top of each
         * other.
         */
        var mLIcons = ["filmlocationA.png","filmlocationB.png","filmlocationC.png","filmlocationD.png","filmlocationE.png","filmlocationF.png","filmlocationG.png","filmlocationH.png","filmlocationI.png","filmlocationJ.png"];
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

        setMarkers(map, locations);
    }
});