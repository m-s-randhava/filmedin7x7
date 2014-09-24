![alt tag](http://filmedin7x7.herokuapp.com/static/img/filmedin7x7_10.jpg) 
filmedin7x7 -- An implementation of "SF Movies"
==================================================

An application listing which films have been filmed in SF and where they have been filmed.

This application does the following:

    1.  Allows users to search a Google map centered at San Francisco City Hall by "location,"
        surfacing films that may or may not have been filmed at a matching location
        a.  This serves as a neat discovery mechanism, for users can simply either:
            i.    Type into the text box to surface partial matches
                -   Typing "Alco" will retrieve 2 results:
                    *   "Movie Title" : "Freebie and the Bean", 
                        "Movie Location" : "Alco Plaza"
                    *   "Movie Title" : "The Conversation", 
                        "Movie Location" : "Alcoa Building (1 Maritime Plaza)"
            ii.   Select one of the continually updating 'autocompletion' results that appear
                  in a dropdown to retrieves exact matches to the selection
                -   While typing "Mar," the location "Marina Green" will appear in an 
                    autocompletion dropdown, and if selected, the only matching movie will 
                    appear:
                    *   "Movie Title" : "Blue Jasmine", 
                        "Movie Location" : "Marina Green"
        b.  While typing in the text box, four events are occurring:
            i.    A set of results detailing film titles and their associated locations is 
                  continually being refined and filtered by matching movie locations closer 
                  and closer to what is being typed
            ii.   Since only 10 matching results are displayed at a time to prevent the map 
                  from becoming cluttered, the results are paginated, and a pagination widget 
                  beneath the set of results is continually being updated
            iii.  A set of markers is continually, animatedly, being dropped onto the map to 
                  reflect the newly updated results as one types, alerting the user that changes 
                  are occurring
            iv.   While typing, a set of matching movie locations is continually being updated
                  and presented in an autocompletion dropdown which allows users to navigate
                  its results and choose a location it itself provides rather than relying
                  on manual input
    2.  Presents a button named "Find Nearest 7 Locations" which, when pressed, will show the
        7 closest movies filmed near the user's current position (obviously this is only 
        meaningful if the user is currently in the city at that time).

Stepping through the UI
--------------------------------------------------

*   The Landing Page

![alt tag](http://filmedin7x7.herokuapp.com/static/docs/H.png) 


*   As soon as you begin typing, the autocomplete dropdown continually makes matching location
    suggestions
*   Additionally, all matching films are retrieved, paginated, and markers for the first ten
    results are place on the map
*   Note the results are labeled by letter in the results pane and their associated marker icons
    on the map are also labeled


![alt tag](http://filmedin7x7.herokuapp.com/static/docs/Autocomplete.png) 


*   An example of the ongoing refinement of Autocomplete suggestions and retrieved results, from
    entering a simple 'm' above to 'mari' here
*   At this point there are 2 pages of results

![alt tag](http://filmedin7x7.herokuapp.com/static/docs/Autocomplete_refinement.png)


*   Clicking on page 2 of the pagination widget

![alt tag](http://filmedin7x7.herokuapp.com/static/docs/Pagination.png)


*   Clicking on any marker on the map brings up an info window which displays all the film meta-
    data

![alt tag](http://filmedin7x7.herokuapp.com/static/docs/Marker_Info.png)


*   For the user's current location, on City Hall's steps, these are the 7 closest films made near
    that location

![alt tag](http://filmedin7x7.herokuapp.com/static/docs/Find_nearest.png)


*   In these results, the bottom two movies are at the same location and so they overlap

![alt tag](http://filmedin7x7.herokuapp.com/static/docs/Films_at_same_location_1.png)


*   In these results, the bottom two movies also are at the same location and so they overlap

![alt tag](http://filmedin7x7.herokuapp.com/static/docs/Films_at_same_location_2.png)
