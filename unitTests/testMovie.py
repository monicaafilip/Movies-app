import unittest
from domain.movie import movie
class testMovie(unittest.TestCase):

    def setUp(self):
        self.__id=1
        self.__title="Divergent"
        self.__description="The best"
        self.__genre="Action"

    def tearDown(self):
        pass
    
    def testMovie(self):
        self._movie=movie(self.__id,self.__title,self.__genre,self.__description)
        self.assertEqual(self.__id, 1)
        self.assertEqual(self.__title,"Divergent" )
        self.assertEqual(self.__genre,"Action")
        self.assertEqual(self.__description,"The best")
        self.assertEqual(self._movie,movie(self.__id,self.__title,self.__genre,self.__description))
    
    
if __name__ == "__main__":
    unittest.main()
    