from abc import ABC, abstractmethod
from Util.DBconnenction import DBConnection
from Entity import Booking


class IBooking_system_service_provider(ABC, DBConnection):

    @abstractmethod
    def calculate_booking_cost(self, num_tickets):
        pass

    @abstractmethod
    def book_tickets(self, event_id, num_tickets, booking_date, list_of_customers):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id):
        pass