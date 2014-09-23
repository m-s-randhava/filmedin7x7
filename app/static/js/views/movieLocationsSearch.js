/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

/**
 *  Creates a Backbone.js view bound to the '.col-md-4' of
 *  the left pane view.  It is tied to a collection that queries
 *  the backend for films with locations matching the searched for
 *  words or phrase:
 *
 *      collectionMovieLocations (collections/movieLocations.js)  =>  FilmsAtLocationsAPI
 *
 */
app.movieLocationsSearchView = Backbone.View.extend({
    el: '.col-md-4',

    initialize: function( ) {
        /**
         *  Creates a Backbone.js inner view.
         *
         *  It is tied to a collection that queries the backend for
         *  films with locations matching the searched for words or
         *  phrase.  It displays the results of the search:
         *
         *      collectionMovieLocations  =>  FilmsAtLocationsAPI
         *
         */
        this.innerResultsView = new app.movieLocationsView( {
            collection: this.collection
        } );

        /**
         *  Creates a Backbone.js inner view.
         *
         *  It is tied to a collection that queries the backend for
         *  films with locations matching the searched for words or
         *  phrase.  It displays the pagination widget for the search:
         *
         *      collectionMovieLocations  =>  FilmsAtLocationsAPI
         *
         */
        this.innerPaginationView = new app.resultsPaginatorView({
            collection: this.collection,
        });
    },

    //  Tells the collection to fetch the results for the 'search phrase'
    doSearch: function(target) {
        //  Show the results pane
        $('#results_list_container').show();
        //  Show the pagination widget
        $('#results_info').show();

        //  Start by asking for page 1 of results
        this.collection.page = 1;
        this.innerResultsView.collection.location = target;

        //  If the search location set on the collection is empty
        //  reset the collection, else fetch the results
        if (this.innerResultsView.collection.location == "") {
            this.innerResultsView.collection.reset();
            $('#results_list_container').hide();
            $('#results_info').hide();
        } else {
            //  Pass ac_selected as True if this collection
            //  indicates the search is for a selected item in
            //  the autocomplete dropdown.
            if (this.collection.ac_selected == 'True') {
                this.innerResultsView.collection.fetch( {
                    //  Fetch parameters
                    data: $.param({ page: this.collection.page, ac_selected: 'True'}),
                    reset: true ,
                    //  Reset on error
                    error: function(model, xhr, options) {
                        this.reset();
                    }.bind(this.innerResultsView.collection)
                } );
            } else {
                this.innerResultsView.collection.fetch( {
                    //  Fetch parameters
                    data: $.param({ page: this.collection.page}),
                    //  Reset on error
                    reset: true ,
                    error: function(model, xhr, options) {
                        this.reset();
                    }.bind(this.innerResultsView.collection)
                } );
            }
        }

    }
});