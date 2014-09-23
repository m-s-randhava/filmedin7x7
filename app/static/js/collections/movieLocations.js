/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app.movieLocations = Backbone.Collection.extend({
    model: app.movieLocation,
    url: function() {
        return '/film/locations/' + this.location;
    }
    ,
    parse: function(response, xhr) {
        this.prev = xhr.xhr.getResponseHeader('prev');
        this.next = xhr.xhr.getResponseHeader('next');
        this.page = xhr.xhr.getResponseHeader('page');
        this.num_films_at_locations = xhr.xhr.getResponseHeader('num_films_at_locations');
        this.pages = xhr.xhr.getResponseHeader('pages');
        return response;
    }
});