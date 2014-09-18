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

    doSearch: function(target) {
        $('#results_list_container').show();
        $('#results_info').show();

        this.collection.page = 1;
        this.innerResultsView.collection.location = target;
        this.innerPaginationView.model.location = target;

        if (this.innerResultsView.collection.location == "") {
            this.innerResultsView.collection.reset();
             $('#results_list_container').hide();
        } else {
            this.innerResultsView.collection.fetch( {
                data: $.param({ page: this.collection.page}),
                reset: true ,
                error: function(model, xhr, options) {
                    this.reset();
                }.bind(this.innerResultsView.collection)
            } );
        }

    }
});