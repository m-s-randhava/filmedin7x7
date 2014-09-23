/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app.movieLocations = Backbone.Collection.extend({
    model: app.movieLocation,
    url: function() {
        return 'http://filmedin7x7.herokuapp.com/film/locations/' + this.location;
    }
});