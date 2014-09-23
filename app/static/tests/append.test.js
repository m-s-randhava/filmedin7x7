/**
 * Created by mohanrandhava on 9/22/14.
 */

describe("appending strings", function() {
    it("should be able to append 2 strings", function() {
        expect(append).toBeDefined();
    });
    it("should append 2 strings", function() {
        expect(append('hello','world')).toEqual('hello world');
    });
});