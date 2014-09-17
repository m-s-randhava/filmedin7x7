/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

app.resultsPaginator = Backbone.Model.extend({
    url: function() {
        return 'http://127.0.0.1:5000/film/locations/pagination/' + this.location;
    }
});