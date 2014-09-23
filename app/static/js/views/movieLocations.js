/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

/**
 *  Creates a Backbone.js view bound to the '#results_list' of
 *  the left pane view.  It is tied to a collection that queries
 *  the backend for films with locations matching the searched for
 *  words or phrase:
 *
 *      collectionMovieLocations (collections/movieLocations.js)        =>  FilmsAtLocationsAPI
 *
 */
app.movieLocationsView = Backbone.View.extend({
    el: '#results_list',

    initialize: function( ) {
        this.render();
        //  Listen to 'reset' events on collection and then render
        this.listenTo( this.collection, 'reset', this.render);
    },

    //  Create the results list
    render: function() {
        //  A List of the icon names, to be associated in order with the results retrieved,
        //  for the purposes of enumerating the results and identifying marker icons on the map
        var mLListIcons = ["A.png","B.png","C.png","D.png","E.png","F.png","G.png","H.png","I.png","J.png"];
        var mLListIconsIndex = 0;
        //  Hide and empty the current results pane ...
        this.$el.hide().empty();
        if (this.collection.location != "") {
            //  Render each movie location
            this.collection.each(
                function(mLListIcons, mLListIconsIndex) {
                    return function ( movieLocation ) {
                        this.renderMovieLocation(movieLocation, mLListIcons[mLListIconsIndex++] );
                    };
                }(mLListIcons, mLListIconsIndex), //    Closure ...
                this
            );
            //  Fade in the new results pane ...
            this.$el.fadeIn();
        }
    },

    //  Renders each movie location by creating its own view and appending
    //  that view to the results pane
    renderMovieLocation: function( movieLocation, movieLocationListIcon ) {
        /**
         *  Creates a Backbone.js view for the movie location.
         *  It is tied to a model that is associated with that film location.
         *  It displays the film location:
         *
         *      movieLocation  =>  [No Backend API association]
         *
         */
        var movieLocationView = new app.movieLocationView( {
            model: movieLocation
        });
        this.$el.append( movieLocationView.render(movieLocationListIcon).el );
    }
});