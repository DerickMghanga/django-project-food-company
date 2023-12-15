from django.test import TestCase
from datetime import datetime
from.models import Reservation

# Create your tests here.
class ReservationModelTest(TestCase):

    @classmethod
    def setUpData(cls):
        cls.reservation = Reservation.objects.create(
            first_name = "John",
            last_name = 'McDonald',
            contact = "0712345678",
            time = "11:22",
            count = 5,
            notes = "Outdoor table",
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)
        self.assertIsInstance(self.reservation.contact, str)
        self.assertIsInstance(self.reservation.notes, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time, datetime)