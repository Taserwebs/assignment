INSERT INTO Venue
    (venue_id, venue_name, address)
VALUES
    (1, 'Concert Hall', '123 Main St, City A'),
    (2, 'Sports Arena', '456 Oak Rd, City B'),
    (3, 'Movie Theater', '789 Elm St, City C'),
    (4, 'Stadium', '321 Pine Ave, City D'),
    (5, 'Auditorium', '159 Maple Ln, City E'),
    (6, 'Concert Venue', '753 Cedar Blvd, City F'),
    (7, 'Sports Complex', '246 Birch Dr, City G'),
    (8, 'Movie Multiplex', '987 Willow Ct, City H'),
    (9, 'Amphitheater', '654 Spruce Way, City I'),
    (10, 'Performing Arts Center', '810 Walnut St, City J');

-- Insert records into Event table
INSERT INTO Event
    (event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type)
VALUES
    (1, 'Rock Concert', '2023-06-15', '19:00:00', 1, 5000, 2500, 75.99, 'Concert'),
    (2, 'Football Match', '2023-07-10', '15:00:00', 2, 50000, 10000, 30.50, 'Sports'),
    (3, 'Blockbuster Movie', '2023-06-20', '18:30:00', 3, 300, 100, 12.99, 'Movie'),
    (4, 'Tennis Tournament', '2023-08-01', '10:00:00', 4, 20000, 8000, 45.75, 'Sports'),
    (5, 'Broadway Show', '2023-09-12', '20:00:00', 5, 2000, 500, 89.99, 'Concert'),
    (6, 'Pop Concert', '2023-07-25', '21:00:00', 6, 10000, 3000, 65.25, 'Concert'),
    (7, 'Basketball Game', '2023-06-10', '19:30:00', 7, 15000, 2000, 25.99, 'Sports'),
    (8, 'Indie Film Festival', '2023-08-15', '14:00:00', 8, 200, 80, 9.99, 'Movie'),
    (9, 'Country Music Concert', '2023-09-20', '18:00:00', 9, 8000, 1500, 55.50, 'Concert'),
    (10, 'Opera Performance', '2023-10-05', '19:30:00', 10, 1500, 300, 120.00, 'Concert');


-- Insert records into Customer table
INSERT INTO Customer
    (customer_id, customer_name, email, phone_number)
VALUES
    (1, 'John Doe', 'john.doe@email.com', '1234567890'),
    (2, 'Jane Smith', 'jane.smith@email.com', '9876543210'),
    (3, 'Michael Johnson', 'michael.johnson@email.com', '5551234567'),
    (4, 'Emily Davis', 'emily.davis@email.com', '7778889990'),
    (5, 'David Wilson', 'david.wilson@email.com', '1112223333'),
    (6, 'Sophia Thompson', 'sophia.thompson@email.com', '4445556666'),
    (7, 'Daniel Anderson', 'daniel.anderson@email.com', '7778889999'),
    (8, 'Olivia Martinez', 'olivia.martinez@email.com', '2223334444'),
    (9, 'William Taylor', 'william.taylor@email.com', '5556667777'),
    (10, 'Ava Garcia', 'ava.garcia@email.com', '8889990000');

-- Insert records into Booking table
INSERT INTO Booking
    (booking_id, customer_id, event_id, num_tickets, total_cost, booking_date)
VALUES
    (1, 1, 1, 2, 151.98, '2023-05-01'),
    (2, 2, 2, 4, 122.00, '2023-06-15'),
    (3, 3, 3, 2, 25.98, '2023-06-10'),
    (4, 4, 4, 3, 137.25, '2023-07-20'),
    (5, 5, 5, 5, 449.95, '2023-08-01'),
    (6, 6, 6, 2, 130.50, '2023-07-01'),
    (7, 7, 7, 4, 103.96, '2023-05-25'),
    (8, 8, 8, 3, 29.97, '2023-07-30'),
    (9, 9, 9, 6, 333.00, '2023-08-15'),
    (10, 10, 10, 2, 240.00, '2023-09-01');