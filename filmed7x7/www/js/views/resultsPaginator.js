/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

app.resultsPaginatorView = Backbone.View.extend({
    el: '#results_info',
    template: _.template( $('#paginationTemplate').html() ),

    initialize: function( ) {
        this.listenTo( this.collection, 'reset', this.update);
        this.listenTo( this.model, 'change', this.render);
    },

    update: function() {
        this.model.fetch(function(collection, model) {
            return {
                data: $.param({ page: collection.page}),
                error: function(model, xhr, options) {
                    this.set({
                        "count": 0,
                        "next": 0,
                        "pages": 0,
                        "prev": 0
                    });
                }.bind(model)
            };
        }(this.collection, this.model));
    },

    render: function() {
        $( "#result_count" ).html(this.model.get('count') + " results found");
        var json = this.model.toJSON();
        json['parray'] = [];

        for (var i = 1; i <= json['pages']; i++) {
            json['parray'].push(i);
        }

        this.$('ul.pagination').html( this.template( json ) );

        $('ul.pagination li').click( function(collection) {
            return function(e) {
                var page = e.target.id;
                collection.page = page;
                collection.fetch(function (page, collection) {
                    return {
                        data: $.param({ page: page}),
                        reset: true ,
//                        success: function(model, xhr, options) {
//                            this.page = page;
//                        }.bind(collection),
                        error: function(model, xhr, options) {
                            this.reset();
                        }.bind(collection)
                    }
                }(page, collection));
            }
        }(this.collection));

        return this;
    }
});