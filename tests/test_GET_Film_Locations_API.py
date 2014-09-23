import unittest
import json
import urllib
from flask import current_app, url_for
from app import create_app

class test_GET_Film_Locations_API(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_request_multiple_locations(self):
        """ TESTING IF redis will return all 'Locations' which have words
            within starting with 'mar'

            COMPARING WITH data retrieved from data loaded into MySQL from
            raw file 'film_locations_in_san_francisco.csv' which was
            downloaded from site @ https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?

            The comparison data was retrieved from MySQL using the following
            query:

            SELECT Locations FROM Locations WHERE Locations REGEXP '[[:<:]]Mar.*'
        """
        response = self.client.get(url_for('film_locations',location='mar') + '?page=1')
        expected_response = [{"location_mercator": {"y": 4182217.5768227046, "x": 553196.023683902}, "Title": "Nine Months", "Production Company": "1492 Pictures", "Writer": "Chris Columbus", "Locations": "Marathon Plaza (303 2nd Street)", "Director": "Chris Columbus", "Actor 3": "Richard Chamberlain", "filmid": 605, "Actor 1": "Hugh Grant", "Actor 2": "Julianne Moore", "Fun Facts": "", "Distributor": "Twentieth Century Fox Film Corp.", "Release Year": "1995", "location": {"lat": 37.7857659, "lng": -122.3958604}}, {"location_mercator": {"y": 4181002.146029169, "x": 551129.3831391562}, "Title": "Blue Jasmine", "Production Company": "Perdido Productions", "Writer": "Woody Allen", "Locations": "Marina Blvd from Leguna to Baker", "Director": "Woody Allen", "Actor 3": "Peter Sarsgaard", "filmid": 103, "Actor 1": "Cate Blanchett", "Actor 2": "Alec Baldwin", "Fun Facts": "", "Distributor": "Sony Pictures Classics", "Release Year": "2013", "location": {"lat": 37.7749295, "lng": -122.4194155}}, {"location_mercator": {"y": 4184507.9927710798, "x": 549373.545164412}, "Title": "Blue Jasmine", "Production Company": "Perdido Productions", "Writer": "Woody Allen", "Locations": "Marina Green", "Director": "Woody Allen", "Actor 3": "Peter Sarsgaard", "filmid": 100, "Actor 1": "Cate Blanchett", "Actor 2": "Alec Baldwin", "Fun Facts": "", "Distributor": "Sony Pictures Classics", "Release Year": "2013", "location": {"lat": 37.8066235, "lng": -122.4391137}}, {"location_mercator": {"y": 4181002.146029169, "x": 551129.3831391562}, "Title": "Milk", "Production Company": "Focus Features", "Writer": "Dustin Lance Black", "Locations": "Marine Fireman's Union Headquarters", "Director": "Gus Van Sant", "Actor 3": "", "filmid": 555, "Actor 1": "Sean Penn", "Actor 2": "Emile Hirsch", "Fun Facts": "", "Distributor": "Focus Features", "Release Year": "2008", "location": {"lat": 37.7749295, "lng": -122.4194155}}, {"location_mercator": {"y": 4183890.70775621, "x": 551930.6038088651}, "Title": "Edtv", "Production Company": "Imagine Entertainment", "Writer": "Lowell Ganz", "Locations": "Mario's Bohemian Cigar Store (Washington Square)", "Director": "Ron Howard", "Actor 3": "Rosie Perez", "filmid": 250, "Actor 1": "Matthew McConaughey", "Actor 2": "Jenna Elfman", "Fun Facts": "", "Distributor": "MCA / Universal Pictures", "Release Year": "1999", "location": {"lat": 37.8009182, "lng": -122.410111}}, {"location_mercator": {"y": 4184552.6290951855, "x": 550140.3636977575}, "Title": "Sister Act 2: Back in the Habit", "Production Company": "Touchstone Pictures", "Writer": "Joseph Howard", "Locations": "Maritime Museum, Building 201 (Fort Mason)", "Director": "Bill Duke", "Actor 3": "", "filmid": 702, "Actor 1": "Whoopi Goldberg", "Actor 2": "Maggie Smith", "Fun Facts": "", "Distributor": "Buena Vista Pictures", "Release Year": "1993", "location": {"lat": 37.80698400000001, "lng": -122.4303999}}, {"location_mercator": {"y": 4182854.3167083133, "x": 551909.1962718914}, "Title": "Bullitt", "Production Company": "Warner Brothers / Seven Arts\nSeven Arts", "Writer": "Alan R. Trustman", "Locations": "Mark Hopkins Hotel (999 California Street)", "Director": "Peter Yates", "Actor 3": "Liz Phair", "filmid": 140, "Actor 1": "Steve McQueen", "Actor 2": "Jacqueline Bisset", "Fun Facts": "The Top of the Mark lounge and restaurant at the top of the hotel was formerly a penthouse suite.", "Distributor": "Warner Brothers", "Release Year": "1968", "location": {"lat": 37.7915787, "lng": -122.4104284}}, {"location_mercator": {"y": 4182835.1334341797, "x": 551930.4140441424}, "Title": "D.O.A", "Production Company": "Cardinal Pictures", "Writer": "Russell Rouse", "Locations": "Mark Hopkins Intercontinental Hotel (1 Nob Hill Circle)", "Director": "Rudolph Mate", "Actor 3": "Oliver Platt", "filmid": 225, "Actor 1": "Edmond O'Brien", "Actor 2": "Pamela Britton", "Fun Facts": "The Top of the Mark lounge and restaurant at the top of the hotel was formerly a penthouse suite.", "Distributor": "United Artists", "Release Year": "1950", "location": {"lat": 37.7914046, "lng": -122.4101888}}, {"location_mercator": {"y": 4182835.1334341797, "x": 551930.4140441424}, "Title": "Innerspace", "Production Company": "Amblin Entertainment", "Writer": "Chip Proser", "Locations": "Mark Hopkins Intercontinental Hotel (1 Nob Hill Circle, Nob Hill)", "Director": "Joe Dante", "Actor 3": "Chazz Palminteri", "filmid": 417, "Actor 1": "Dennis Quaid", "Actor 2": "Martin Short", "Fun Facts": "The Top of the Mark lounge and restaurant at the top of the hotel was formerly a penthouse suite.", "Distributor": "Warner Bros. Pictures", "Release Year": "1987", "location": {"lat": 37.7914046, "lng": -122.4101888}}, {"location_mercator": {"y": 4182835.1334341797, "x": 551930.4140441424}, "Title": "Sudden Impact", "Production Company": "Warner Bros. Pictures", "Writer": "Harry Julian Fink", "Locations": "Mark Hopkins Intercontinental Hotel (1 Nob Hill Circle, Nob Hill)", "Director": "Clint Eastwood", "Actor 3": "Artie Lang", "filmid": 745, "Actor 1": "Clint Eastwood", "Actor 2": "Sondra Locke", "Fun Facts": "The Top of the Mark lounge and restaurant at the top of the hotel was formerly a penthouse suite.", "Distributor": "Warner Bros. Pictures", "Release Year": "1983", "location": {"lat": 37.7914046, "lng": -122.4101888}}]
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(2, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(8, int(response.headers.get('pages')))
        self.assertEquals(71, int(response.headers.get('num_films_at_locations')))

    def test_request_non_existent_location(self):
        response = self.client.get(url_for('film_locations',location='zzzzzz') + '?page=1')
        expected_response = []
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(0, int(response.headers.get('pages')))
        self.assertEquals(0, int(response.headers.get('num_films_at_locations')))

    def test_request_non_existent_numeric_location(self):
        response = self.client.get(url_for('film_locations',location='12345') + '?page=1')
        expected_response = []
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(0, int(response.headers.get('pages')))
        self.assertEquals(0, int(response.headers.get('num_films_at_locations')))

    def test_request_non_existent_non_alphanumeric_location(self):
        response = self.client.get(url_for('film_locations',location='!#$%@') + '?page=1')
        expected_response = []
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(0, int(response.headers.get('pages')))
        self.assertEquals(0, int(response.headers.get('num_films_at_locations')))

    def test_request_single_location_multiple_films(self):
        location = urllib.quote('Japanese Tea Garden (Hagiwara Tea Garden Drive, Golden Gate Park)')
        response = self.client.get(url_for('film_locations',location=location) + '?page=1')
        expected_response = [{"location_mercator": {"y": 4180451.363177985, "x": 546663.6273682178}, "Title": "Jade", "Production Company": "Paramount Pictures", "Writer": "Joe Eszterhas", "Locations": "Japanese Tea Garden (Hagiwara Tea Garden Drive, Golden Gate Park)", "Director": "William Friedkin", "Actor 3": "", "filmid": 448, "Actor 1": "David Caruso", "Actor 2": "Linda Fiorentino", "Fun Facts": "The Japanese Hagiwara family invented \"Chinese\" fortune cookies in the tea-garden", "Distributor": "Paramount Pictures", "Release Year": "1995", "location": {"lat": 37.7702043, "lng": -122.4701584}}, {"location_mercator": {"y": 4180451.363177985, "x": 546663.6273682178}, "Title": "Petulia", "Production Company": "Warner Brothers / Seven Arts", "Writer": "Lawrence B. Marcus", "Locations": "Japanese Tea Garden, Hagiwara Tea Garden Drive, Golden Gate Park", "Director": "Richard Lester", "Actor 3": "", "filmid": 636, "Actor 1": "Julie Christie", "Actor 2": "George C. Scott", "Fun Facts": "The Japanese Hagiwara family invented \"Chinese\" fortune cookies in the tea-garden", "Distributor": "Warner Brothers / Seven Arts", "Release Year": "1968", "location": {"lat": 37.7702043, "lng": -122.4701584}}, {"location_mercator": {"y": 4180451.363177985, "x": 546663.6273682178}, "Title": "The Wedding Planner", "Production Company": "Columbia Pictures", "Writer": "Pamela Falk", "Locations": "Japanese Tea Garden (Hagiwara Tea Garden Drive, Golden Gate Park)", "Director": "Adam Shankman", "Actor 3": "", "filmid": 969, "Actor 1": "Jennifer Lopez", "Actor 2": "Matthew McConaughey", "Fun Facts": "The Japanese Hagiwara family invented \"Chinese\" fortune cookies in the tea-garden", "Distributor": "Sony Pictures Entertainment", "Release Year": "2001", "location": {"lat": 37.7702043, "lng": -122.4701584}}]
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(1, int(response.headers.get('pages')))
        self.assertEquals(3, int(response.headers.get('num_films_at_locations')))

    def test_request_existing_alphanumeric_single_location_single_film(self):
        location = urllib.quote('100 Block of Lombard Street')
        response = self.client.get(url_for('film_locations',location=location) + '?page=1')
        expected_response = [{"location_mercator": {"y": 4184021.396444749, "x": 551170.1049553965}, "Title": "The Love Bug", "Production Company": "Walt Disney Productions", "Writer": "Bill Walsh", "Locations": "100 Block of Lombard Street", "Director": "Robert Stevenson", "Actor 3": "Ed Harris", "filmid": 902, "Actor 1": "Dean Jones", "Actor 2": "Michele Lee", "Fun Facts": "Lombard Street is not actually the crookedest in SF. That honor goes to Potrero Hill's Vermont Street between 22nd and 23rd.", "Distributor": "Buena Vista Distribution", "Release Year": "1968", "location": {"lat": 37.802139, "lng": -122.41874}}]
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(1, int(response.headers.get('pages')))
        self.assertEquals(1, int(response.headers.get('num_films_at_locations')))

    def test_request_existing_alphabetic_single_location_single_film(self):
        location = urllib.quote('Alioto Park')
        response = self.client.get(url_for('film_locations',location=location) + '?page=1')
        expected_response = [{"location_mercator": {"y": 4179220.676574393, "x": 551252.3294737589}, "Title": "Dawn of the Planet of the Apes", "Production Company": "Fox Louisiana Productions, LLC", "Writer": "Rick Jaffa", "Locations": "Alioto Park", "Director": "Matt Reeves", "Actor 3": "Andy Serkis", "filmid": 196, "Actor 1": "Gary Oldman", "Actor 2": "Keri Russell", "Fun Facts": "", "Distributor": "Twentieth Century Fox", "Release Year": "2014", "location": {"lat": 37.7588666, "lng": -122.4181453}}]
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(1, int(response.headers.get('pages')))
        self.assertEquals(1, int(response.headers.get('num_films_at_locations')))

    def test_request_existing_alphabetic_single_location_exact_match(self):
        location = urllib.quote('Alco Plaza')
        response = self.client.get(url_for('film_locations',location=location) + '?page=1&ac_selected=True')
        expected_response = [{"location_mercator": {"y": 3874241.6097306004, "x": 732801.9287159997}, "Title": "Freebie and the Bean", "Production Company": "Warner Bros. Pictures", "Writer": "Robert Kaufman", "Locations": "Alco Plaza", "Director": "Richard Rush", "Actor 3": "Katherine Hepburn", "filmid": 317, "Actor 1": "Alan Arkin", "Actor 2": "James Caan", "Fun Facts": "", "Distributor": "American Broadcasting Company (ABC)", "Release Year": "1974", "location": {"lat": 34.9840089, "lng": -120.4495793}}]
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(1, int(response.headers.get('pages')))
        self.assertEquals(1, int(response.headers.get('num_films_at_locations')))

    def test_request_existing_alphabetic_single_location_partial_match(self):
        location = urllib.quote('Alco Plaza')
        response = self.client.get(url_for('film_locations',location=location) + '?page=1')
        expected_response = [{"location_mercator": {"y": 3874241.6097306004, "x": 732801.9287159997}, "Title": "Freebie and the Bean", "Production Company": "Warner Bros. Pictures", "Writer": "Robert Kaufman", "Locations": "Alco Plaza", "Director": "Richard Rush", "Actor 3": "Katherine Hepburn", "filmid": 317, "Actor 1": "Alan Arkin", "Actor 2": "James Caan", "Fun Facts": "", "Distributor": "American Broadcasting Company (ABC)", "Release Year": "1974", "location": {"lat": 34.9840089, "lng": -120.4495793}}, {"location_mercator": {"y": 4183294.827063401, "x": 552893.9434000009}, "Title": "The Conversation", "Production Company": "American Zoetrope", "Writer": "Francis Ford Coppola", "Locations": "Alcoa Building (1 Maritime Plaza)", "Director": "Francis Ford Coppola", "Actor 3": "", "filmid": 795, "Actor 1": "Gene Hackman", "Actor 2": "", "Fun Facts": "A partially-above ground parking structure near the building made it necessary for architects to make the Alcoa Building's diagonal bracing visible, instead of placing it inside and drastically reducing the amount usable interior space. ", "Distributor": "Paramount Pictures", "Release Year": "1974", "location": {"lat": 37.7954924, "lng": -122.3992123}}]
        self.assertEquals(expected_response, json.loads(response.get_data()))
        self.assertEquals(0, int(response.headers.get('prev')))
        self.assertEquals(0, int(response.headers.get('next')))
        self.assertEquals(1, int(response.headers.get('page')))
        self.assertEquals(1, int(response.headers.get('pages')))
        self.assertEquals(2, int(response.headers.get('num_films_at_locations')))