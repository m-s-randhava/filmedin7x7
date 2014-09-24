![alt tag](http://filmedin7x7.herokuapp.com/static/img/filmedin7x7_10.jpg) 
filmedin7x7 -- An implementation of "SF Movies"
==================================================

An application listing which films have been filmed in SF and where they have been filmed.

This is a full-stack implementation:

    A.  A Backend implemented in Python using the Flask framework to implement a RESTful
        API, also employing other Flask aspects like Flask-Testing, to implement a 
        rudimentary automated testing framework.
    
    B.  A Frontend implemented using Bootstrap.css and Backbone.js.
        
        [NOTE:  The layout template was taken from an open source template available @
        http://derekeder.com/searchable_map_template/.  The template was stripped down and
        adjusted for this use case, and all the logic is not used.  All logic is my own
        development.]
        
    C.  The Google Maps API was used for all maps display, geocoding of locations, and
        "Find my Location" functionality.

**IMPORTANT!**
        [I took the opportunity to learn the Flask framework.  I have never before
        employed a framework in Python, though I have used frameworks in other languages.  
        While at the latest startup, we actually implemented our own lightweight framework,
        both for the backend and frontend.]

**IMPORTANT!**
        [I took the opportunity to learn the Bootstrap CSS framework.  Also, 
        though I've used Backbone.js in the past, I never devoted an in-depth study of the
        framework which I did for this project.]
        
This application has implemented additional features than those detailed in the spec for
"SF Movies."

    A.  Implemented 'partial' and 'exact' matching upon the 'Locations' field for the movies.
    B.  Implemented a "Find Nearest 7 Movie Locations" to my current location (especially
        relevant for mobile devices).
    C.  Implemented a mobile iOS version of this application, tested live successfully while
        in SF.

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


RESTful API Endpoints
--------------------------------------------------

### Autocompletion Endpoint ###

    GET http://filmedin7x7.herokuapp.com/filmedin7x7.herokuapp.com/film/locations/autocomplete?term=[LOCATION_PREFIX]

### Film-Locations Endpoint ###

    GET http://filmedin7x7.herokuapp.com/filmedin7x7.herokuapp.com/film/locations/[LOCATION_PREFIX]?page=1

### Films-Near-Me  Endpoint ###

    GET http://filmedin7x7.herokuapp.com/film/7nearme/lat/[absolute_value([LATITUDE - float])]/<string:lat_sign>/[p|n]/[absolute_value([LATITUDE - float])]/[p|n]

Feature #1:     Autocompletion
--------------------------------------------------

### Front-End ###

    To provide the Autocompletion dropdown UI functionality this application is employing 
    the jQuery Autocomplete widget, and it is using the remote functionality to retrieve
    results as you type from the "Autocompletion Endpoint" (found above).
    

### Back-End ###

    Since the size of searchable feature set feeding the autocomplete functionality is
    not overly large, and since autocompletion demands a very rapid response, this 
    application employs Redis as a fast memory store of the results.  In the course of
    investigation and implementation, an existing python package using Redis to provide
    autocompletion was found, 'redis-completion.'  It essentially leans of Redis' ability
    to provide simple queryable data structures, and in this case it store prefixes of all
    components of all locations within a sorted set and uses the ZRANGE and ZINTERSECT
    functionality to perform matching.  Because of these existing data structures so well
    suited to the autocompletion demands within an in-memory fast store like Redis, it 
    made for a very apt solution.
    
    The validity of using Redis for autocomplete was verified by performing similar
    searches within MySQl and verifying that the Redis results were the same as those
    returned by MySQL.

    [IMPORTANT!  I took the opportunity to learn here again, more about Redis than I had
    already known, how to interact with Redis via Python, and employing it to solve a 
    well-known problem.  Autocompletion could also have been achieved simply by using 
    MySQL or some other NoSQL backing store, but I chose Redis for its performance and
    to learn something anew.]


Feature #2:     RESTful API (Backend)
--------------------------------------------------

### Back-End ###

    In addition to Flask there is a very simple and elegant package called Flask-RESTful,
    that provides a framework to allow for clean and robust implementation of a REST API.
    
    Capabilities of the Flask-RESTful framework were used such as the ability to enforce
    correct urls.
    
    [NOTE!  I would imagine a service like this might be provided free to the public,
    perhaps selling ads against the service.  As such, authorization was not enforced on
    the API's.  Additionally, though it was not implemented here, it would be wise to put
    rate-limiting of the API's in place as well.]    
    
    The Flask-RESTful API was used to provide the 3 REST API's detailed above.
    
    For calls made to the 'Film-Locations Endpoint,' pagination was employed upon the 
    results.  The results were returned 10 at a time for each request and pagination
    information was sent back in the header response, keeping things cleanly
    RESTful.
    
    The Flask testing framework was used to test the API's from request to response.


Feature #3:     Single-Page UI (Frontend)
--------------------------------------------------

### Front-End ###

    The front-end is a single page UI.  There are essentially no page refreshes required.
    
    Employing Backbone.js's MVC framework allows separate views to update themselves 
    whenever the composed collection fetches anew from its associated REST API endpoint.
    
    This allows for a very fast response, achieving things like filtration of results as 
    you type.
    
Feature #4:     Find Nearest 7 (Backend)
--------------------------------------------------

### Front-End ###

    To ascertain the user's location, if a device had a 'navigator.geolocation' available,
    the position was determined in that way.
    

### Back-End ###

    To perform an O(ln) search for nn points nearest a given point, I decided to employ
    a basic data structure called a kd-tree.  I found that the hallowed python scipy
    library has a well-known kd-tree implementation available.  To make use of the
    kd-tree, I needed to treat the geolocated lat/lng positions as 2D points.  To achieve
    this I found I needed to convert them to UTM (Universal Transverse Mercator) projection
    points.  Once this is done, and the kd-tree is built, for any user derived point
    7 nearest points can be quickly found.
    
    The validity of this approach and the correctness of the kd-tree's operation was 
    validated through testing.  In particular, a point was chosen manually on a Google
    Map and 15 other locations, 7 of which could be visually ascertained to be closest
    to the chosen point with certainty.  The kd-tree functionality correctly identified
    these 7.
    
    Once the point was found, the actual films at those locations needed to be returned,
    and so an inverted index was built to allow for hashing points to films.
    
    These structures are built only once at application startup.  They are made available
    via the application context to those requests specifically requiring their use, which
    is the one for the Films-Near-Me  Endpoint.
    
    [IMPORTANT!  I wanted to really understand the problem of geolocalized search since
    it interests me a great deal.  I am aware of GeoSpatial databases and NoSQL options
    (e.g., MongoDB).  I opted not to use these so that I could understand this problem
    at a more fundamental level.  I will be studying those GeoSpatial option now in 
    more detail now that I understand the problem.]    


Feature #5:     Data
--------------------------------------------------

    A form of ETL had to occur, at least to clean the data to some extent.  Certain
    unicode errors, non-alphanumeric elements, etc. had to cleaned up and standard-
    ized.  
    
    When querying Google's Maps API for geolocalization, you had to be careful to 
    limit the search to within San Francisco's confines.  Additionally, sometimes
    a location's description or certain non-standard ways of representing addresses
    could not be correctly geolocalized, as verified by testing.  This brings up
    an interesting and important question as to how to verify that all geolocalizations
    are correct when the data is large-scale and what to do when those errors are
    identified.

Feature #6:     Mapping
--------------------------------------------------

    Maps and markers and geolocalization are all provided by making use of the 
    Google Maps API.  
    
    Marker icons have been created by me.
    
    As markers are added to the map, I made use of drop animation to alert the user
    to the fact that things were changing and filtering as a search was being 
    performed.
    
    Clicking on a marker brings up an info window describing that location and its
    film relevance.

Feature #7:     Tests
--------------------------------------------------

### Front-End ###

    Ideally, time permitting, it would have been possible to employ Jasmine/Karma 
    for front-end unit testing of the UI.  This was not possible owing to 
    constraints of time.

### Back-End ###

    The Back-End has been as thoroughly tested as time would allow.  It is definitely
    possible to add more tests, and this can be done easily, by following the pythonic
    unittest examples employing Flask's testing library functionality found in the 
    '/tests' folder.
    
    These tests run against the RESTful API and verify correctness.
    
    They are automated and can be run by typing the following in the directory
    that contains the code contents:
    
        python manage.py test
        

Feature #8:     Mobile App
--------------------------------------------------

    I created a mobile application from this application, as I thought the use case
    was most suited for mobile, and again, to learn.
    
    I employed Phonegap to convert the app into an iOS application.  Additionaly
    tweaking had to be done to the iOS to get the app to look polished and as
    production ready as possible.
    
    Bootstrap.css made things work quite well.
    
    The app displays the search bar as the top element, and the results pane, the
    pagination widget, and the map, all appear in order below.  All other features
    of operation remain the same.

### Mobile App UI Step-Through ###

*   Mobile App landing page with elements placed vertically

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m1.PNG)

*   Autocompletion, clear, and works well

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m2.PNG)

*   Results pane clear, scrollable

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m3.PNG)

*   Results pane clear, scrollable

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m4.PNG)

*   Results pane clear, scrollable, and pagination widget is clear and functional

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m5.PNG)

*   Markers appear clearly

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m6.PNG)

*   Marker info is clear and fully visible

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m7.PNG)

*   Attempting to "Find Near Me," being asked for permission by iOS

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m8.PNG)

*   Live "Find Near Me" results in SF (steps of City Hall)

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m9.PNG)

*   Live "Find Near Me" results in SF (near Montgomery St.)

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m10.PNG)

*   The app as it appears on the iOS homescreen (pardon my daughter!)

![alt tag](http://filmedin7x7.herokuapp.com/static/img/m11.PNG)
