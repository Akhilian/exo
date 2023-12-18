import unittest

from app.adapter import import_csv
from app.infrastructure.models import Passenger


class ImportCSV(unittest.TestCase):
    def test_import_with_missing_cabin(self):
        # Given
        csv = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S'''

        # When
        passengers = import_csv(csv)

        # Then
        self.assertEqual([
            Passenger(passengerId=1, survived=0, pclass=3, name='Braund, Mr. Owen Harris', sex='male', age='22',
                      sibSp=1, parch=0, ticket='A/5 21171', fare=7.25, cabin=None, embarked='S')
        ], passengers)

    def test_import_with_a_cabin(self):
        # Given
        csv = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C'''

        # When
        passengers = import_csv(csv)

        # Then
        self.assertEqual([
            Passenger(passengerId=2, survived=1, pclass=1, name='Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
                      sex='female', age='38',
                      sibSp=1, parch=0, ticket='PC 17599', fare=71.2833, cabin='C85', embarked='C')
        ], passengers)

    def test_import_with_rounded_fare(self):
        # Given
        csv = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S'''

        # When
        passengers = import_csv(csv)

        # Then
        self.assertEqual(passengers[0].fare, 16.0)

    def test_import_particuliar_tickets(self):
        # Given
        csv = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S'''

        # When
        passengers = import_csv(csv)

        # Then
        self.assertEqual([
            Passenger(
                passengerId=3, survived=1, pclass=3, name='Heikkinen, Miss. Laina', sex='female', age='26',
                sibSp=0, parch=0, ticket='STON/O2. 3101282', fare=7.925, cabin=None, embarked='S'
            )
        ], passengers)

    def test_import_missing_embarked(self):
        # Given
        csv = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
62,1,1,"Icard, Miss. Amelie",female,38,0,0,113572,80,B28,'''

        # When
        passengers = import_csv(csv)

        # Then
        self.assertEqual([Passenger(passengerId=62, survived=1, pclass=1, name='Icard, Miss. Amelie', sex='female',
                                    age='38', sibSp=0, parch=0, ticket='113572', fare=80.0, cabin='B28',
                                    embarked=None)],
                         passengers)

    def test_import_with_age_that_is_not_round(self):
        # Given
        csv = '''PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
58,0,3,"Novel, Mr. Mansouer",male,28.5,0,0,2697,7.2292,,C'''

        # When
        passengers = import_csv(csv)

        # Then
        self.assertEqual([Passenger(passengerId=58, survived=0, pclass=3, name='Novel, Mr. Mansouer', sex='male',
                                    age='28.5', sibSp=0, parch=0, ticket='2697', fare=7.2292, cabin=None,
                                    embarked='C')],
                         passengers)


if __name__ == '__main__':
    unittest.main()
