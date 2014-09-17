/**
 * Created by mohanrandhava on 9/16/14.
 */
var app = app || {};

app.resultsPaginator = Backbone.Model.extend({
    url: function() {
        return '/film/locations/pagination/' + this.location;
    }
});