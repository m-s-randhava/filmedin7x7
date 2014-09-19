/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app.movieLocationsNearMeView = Backbone.View.extend({
    el: '#results_list',

    initialize: function( ) {
        this.render();
        this.listenTo( this.collection, 'reset', this.render);
    },

    render: function() {
        var mLListIcons = ["A.png","B.png","C.png","D.png","E.png","F.png","G.png","H.png","I.png","J.png"];
        var mLListIconsIndex = 0;
        this.$el.hide().empty();
        if (this.collection.location != "") {
            this.collection.each(
                function(mLListIcons, mLListIconsIndex) {
                    return function ( movieLocation ) {
                        this.renderMovieLocation(movieLocation, mLListIcons[mLListIconsIndex++] );
                    };
                }(mLListIcons, mLListIconsIndex),
                this
            );
            this.$el.fadeIn();
        }
    },

    renderMovieLocation: function( movieLocation, movieLocationListIcon ) {
        var movieLocationView = new app.movieLocationView( {
            model: movieLocation
        });
        this.$el.append( movieLocationView.render(movieLocationListIcon).el );
    }
});