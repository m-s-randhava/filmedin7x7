/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

app.movieLocationsSearchView = Backbone.View.extend({
    el: '.col-md-4',

    events: {
        'click #search': 'doSearch'
    },

    initialize: function( ) {
        var model = new app.resultsPaginator();

        this.innerResultsView = new app.movieLocationsView( {
            collection: this.collection
        } );
        this.innerPaginationView = new app.resultsPaginatorView({
            collection: this.collection,
            model: model
        });
    },

    doSearch: function() {
        $('#results_list_container').show();
        $('#results_info').show();

        this.collection.page = 1;
        this.innerResultsView.collection.location = $('#search_location').val();
        this.innerPaginationView.model.location = $('#search_location').val();
//        this.innerPaginationView.model.fetch({
//            error: function(model, xhr, options) {
//                this.set({
//                    "count": 0,
//                    "next": 0,
//                    "pages": 0,
//                    "prev": 0
//                });
//            }.bind(this.innerPaginationView.model)
//        });
        this.innerResultsView.collection.fetch( {
            data: $.param({ page: this.collection.page}),
            reset: true ,
            error: function(model, xhr, options) {
                this.reset();
            }.bind(this.innerResultsView.collection)
        } );
    }
});