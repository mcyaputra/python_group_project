import unittest
from core.utils import *

class TestMergeKeywords(unittest.TestCase):

    def setUp(self):
        self.keywords = ['Ford', 'Toyota', 'BYD']

    def test_merge_0_result(self):
        expected_result = None
        result = merge_keywords()

        self.assertEqual(result, expected_result)

    def test_merge_1_result(self):
        expected_result = "Ford"
        result = merge_keywords(self.keywords[0])
        
        self.assertEqual(result, expected_result)

    def test_merge_2_result(self):
        expected_result = "Ford%OR%Toyota"
        result = merge_keywords(self.keywords[0], self.keywords[1])

        self.assertEqual(result, expected_result)

    def test_merge_3_result(self):
        expected_result = "Ford%OR%Toyota%OR%BYD"
        result = merge_keywords(self.keywords[0], self.keywords[1], self.keywords[2])

        self.assertEqual(result, expected_result)

class TestConvertCountriesName(unittest.TestCase):

    def setUp(self):
        self.countries = ['Australia', 'Europe', 'China']

    def test_convert_australia(self):
        excepted_result = 'au'
        result = convert_countries_name_for_processing(self.countries[0])

        self.assertEqual(result, excepted_result)

    def test_convert_europe(self):
        excepted_result = 'eu'
        result = convert_countries_name_for_processing(self.countries[1])

        self.assertEqual(result, excepted_result)

    def test_convert_china(self):
        excepted_result = 'cn'
        result = convert_countries_name_for_processing(self.countries[2])

        self.assertEqual(result, excepted_result)

class TestMergeCountries(unittest.TestCase):

    def setUp(self):
        self.countries = ['Australia', 'Europe', 'China']

    def test_merge_0_country(self):
        expected_result = None
        result = merge_countries()

        self.assertEqual(result, expected_result)

    def test_merge_1_countries(self):
        expected_result = 'au'
        result = merge_countries(self.countries[0])

        self.assertEqual(result, expected_result)

    def test_merge_2_countries(self):
        expected_result = 'au,eu'
        result = merge_countries(self.countries[0], self.countries[1])

        self.assertEqual(result, expected_result)

    def test_merge_3_countries(self):
        expected_result = 'au,eu,cn'
        result = merge_countries(self.countries[0], self.countries[1], self.countries[2])

        self.assertEqual(result, expected_result)

class TestUnpackResponse(unittest.TestCase):

    def test_unpack_response(self):

        data = {'news': [{'id': 219198230,
                'title': 'Cannes 2024: Megalopolis movie review – Francis Ford Coppola’s wildly ambitious project comes to fruition',
                'text': '4/5 stars Francis Ford Coppola returns with a bang, with his long-cherished and divisive project Megalopolis. Unveiled in competition at the Cannes Film Festival, it is the director’s first film since 2011’s Twixt, and one he has dreamed of making since 1977. An intriguing blend of science fiction and political satire, it begins with a voice-over: “Our American Republic is not all that different from old Rome.” It is a conceit that Coppola pursues, with his lead character named Cesar Catalina (Adam Driver) and the setting a 21st century metropolis called New Rome. Surely a figure to be compared to Coppola, Catalina is an architect who schemes of creating a city of the future for the people, named Megalopolis. It is a unique vision, built with a substance called megalon, which some believe is unsafe. Catalina’s reputation is being called into question wherever he goes. Dubbed an “obsessive-compulsive wacko” and a “reckless dreamer”, he is gathering enemies like some collect stamps. Among the most powerful is Mayor Franklyn Cicero (Breaking Bad’s Giancarlo Esposito), whose daughter Julia (Nathalie Emmanuel) soon becomes the object of the architect’s desire. With nods to Shakespeare and other writers and thinkers across human history, Coppola’s erudite script will not be for some. Characters speak in aphorisms or poetical flourishes (“time, show me the future”), but it is an ornate style that you eventually ease into. Some of it does not work, plainly. But some of it is inspired. At one point, the film drifts into the arena of live theatre. At the screening this writer attended, an actor came on stage in front of the screen, a spotlight beamed on him. It seems unlikely this will be the case for every showing, but it was a thrilling moment, albeit one that some will call a baffling gimmick. Visually, there are sublime touches, like a shot of Megalopolis inside a snow globe or the sight of Driver, whose character can manipulate time, standing on the mechanics of a giant clock. Performance-wise, Megalopolis is all over the shop. Aubrey Plaza is excellent as a ruthless TV reporter, while Shia LaBeouf is barmy and over-the-top as a rival to Catalina – one who craves his power and influence. With chariot races, Elvis impersonators and party scenes to rival those in Damien Chazelle’s Babylon, this is a bonkers meditation on life, the universe and everything. With allusions to Citizen Kane, Coppola has crafted what might be a unique sign-off to one of cinema’s great careers. Megalopolis is daring, daft and never dull. Want more articles like this? Follow SCMP Film on Facebook',
                'summary': 'With nods to Shakespeare and Citizen Kane, Coppola mixes science fiction and satire in this long-awaited, daft but daring saga of an architect (Adam Driver) building a 21st century metropolis.',
                'url': 'https://www.scmp.com/lifestyle/entertainment/article/3262986/cannes-2024-megalopolis-movie-review-francis-ford-coppolas-wildly-ambitious-project-comes-fruition',
                'image': 'https://cdn.i-scmp.com/sites/default/files/d8/images/canvas/2024/05/17/25efab9c-6a74-4dfd-9bac-17f99479e2f9_b7f8378b.jpg',
                'video': None,
                'publish_date': '2024-05-17 00:30:34',
                'author': 'James Mottram',
                'authors': ['James Mottram'],
                'language': 'en',
                'source_country': 'cn',
                'sentiment': 0.57}]}
        
        expected_result = ['Cannes 2024: Megalopolis movie review – Francis Ford Coppola’s wildly ambitious project comes to fruition']

        result,_,_,_,_,_,_ = unpack_response(data)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()