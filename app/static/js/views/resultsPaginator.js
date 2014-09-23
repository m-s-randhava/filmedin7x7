/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

/**
 *  Creates a Backbone.js view bound to the '#results_info' of
 *  the left pane view.  It is tied to a collection that queries
 *  the backend for movies with locations matching currently
 *  searched text:
 *      collectionMovieLocations        =>  FilmsAtLocationsAPI
 *
 */
app.resultsPaginatorView = Backbone.View.extend({
    el: '#results_info',
    //  An underscore.js template to display pagination widget
    template: _.template( $('#paginationTemplate').html() ),

    initialize: function( ) {
        //  Listen to 'reset' events on collection and then render
        this.listenTo( this.collection, 'reset', this.render);
    },

    render: function() {
        $( "#result_count" ).html(this.collection.num_films_at_locations + " results found");
        $( ".alert.alert-info").show();

        //  Retrieve latest pagination information from the collection
        //  that was just reset/refreshed.
        var json = {
            'prev' : this.collection.prev,
            'next' : this.collection.next,
            'current' : this.collection.page,
            'count' : this.collection.num_films_at_locations,
            'pages' : this.collection.pages
        };
        json['parray'] = [];

        for (var i = 1; i <= this.collection.pages; i++) {
            json['parray'].push(i);
        }

        //  Create the pagination widget and populate
        //  with pagination data.
        this.$('ul.pagination').html( this.template( json ) );

        //  Handle a 'click' event on a paginated page
        $('ul.pagination li').click( function(collection) {
            return function(e) {
                var page = e.target.id;

                //  Set the collection's page field to the currently
                //  selected field
                collection.page = page;

                //  Fetch the new page's data from the API
                collection.fetch(function (page, collection) {
                    return {
                        data: $.param({ page: page}),
                        reset: true ,
                        //  Reset to empty on error
                        error: function(model, xhr, options) {
                            this.reset();
                        }.bind(collection)
                    }
                }(page, collection));   //  Closure ...
            }
        }(this.collection)); // Closure ...

        return this;
    }
});