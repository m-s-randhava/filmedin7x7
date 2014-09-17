/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app.movieLocations = Backbone.Collection.extend({
    model: app.movieLocation,
    url: function() {
        return 'http://10.0.1.5:5000/film/locations/' + this.location;
    }
});