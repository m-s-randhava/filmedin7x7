/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

/**
 *  Creates a Backbone.js view that creates a new 'div' to hold
 *  movie/location information.
 *  It is tied to a model that a collection maintains and is
 *  instantiated by a separate view (either the movieLocations.js
 *  or movieLocationsNearMe.js view).
 *
 *      model (models/movieLocations.js)       =>  [No Backend API association]
 *
 */
app.movieLocationView = Backbone.View.extend({
    tagName: 'div',
    className: 'row-fluid item-list',
    template: _.template( $('#movieLocationTemplate').html() ),

    render: function(movieLocationListIcon) {
        var json = this.model.toJSON();
        json['listIcon'] = movieLocationListIcon;
        this.$el.html( this.template( json ) );
        return this;
    }
});