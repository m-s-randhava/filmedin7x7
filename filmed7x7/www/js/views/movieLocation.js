/**
 * Created by mohanrandhava on 9/15/14.
 */
var app = app || {};

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