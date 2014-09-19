/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app._7MovieLocationsNearMe = Backbone.Collection.extend({
    model: app.movieLocation,
    url: function() {
        return '/film/7nearme/lat/37.779390/p/lng/122.418432/n';
//        return '/film/7nearme/lat/' + Math.abs(this.lat) + '/' + this.lat_sign + '/lng/' + Math.abs(this.lng) + '/' + this.lng_sign;
    }
});