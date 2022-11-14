# Airplane Seating Algorithm

This airplane seating algorithm first seats all of the Economy Plus passengers (as before). It then takes all of the economy reservations and orders them by group size, from highest to lowest. When comparing economy bookings that are the same number of passengers, the family that booked first has priority. The algorithm then searches for adjacent seats and books the group in those seats. If it is not possible to book a group in adjacent seats (within the same row), then the group is split in half and the two smaller groups are added to the list of economy bookings (which is then ordered as before). The economy passengers are booked until all are seated.

As an example, let's say that this is the current list of economy groups that haven't been booked yet (listed with the number of seats in the booking):

[(u-2, 3), (u-1, 2), (u-4, 2), (u-7, 2), (u-3, 1), (u-5, 1), (u-6, 1)]

If there are not 3 adjacent seats, then the u-2 booking will be split into two bookings, one with one person and one with two. Those two bookings will be ordered after the u-1 booking but before any other bookings. The remaining bookings that the algorithm would then consider are:

[(u-1, 2), (u-2, 2), (u-4, 2), (u-7, 2), (u-2, 1),(u-3, 1), (u-5, 1), (u-6, 1)]

It's worth noting that the original (u-2, 3) booking will still exist in the list of economy bookings but will be ignored by the algorithm once it's been split.

The algorithm is fully implemented and working as described.