/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app._7MovieLocationsNearMe = Backbone.Collection.extend({
    model: app.movieLocation,
    url: function() {
        return 'http://filmedin7x7.herokuapp.com/film/7nearme/lat/' + Math.abs(this.lat) + '/p/lng/' + Math.abs(this.lng) + '/n';
    }
});