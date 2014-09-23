/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

app.resultsPaginator = Backbone.Model.extend({
    url: function() {
        return 'http://filmedin7x7.herokuapp.com/film/locations/pagination/' + this.location;
    }
});