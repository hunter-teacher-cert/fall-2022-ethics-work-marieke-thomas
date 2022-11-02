# Airplane Seating Algorithm

First, seats are assigned to the Economy Plus passengers (simulating allowing them to choose their seats during booking). This is basically the same as the original algorithm. Next, adjacent seats are assigned to any groups who book normal Economy tickets, with the largest groups being seated first. Finally, any passengers with Economy tickets flying alone are randomly seated in the remaining seats.

This will improve equity by allowing (at least some) groups of passengers to sit together.

In terms of implementation, this will be somewhat inefficient as we will need to repeatedly loop over the dictionary in order to seat the largest groups first. Perhaps it would be better to store the Economy ticket-holder information in a list instead of a dictionary and order the list by decreasing group size.

One potential issue here is that there is still the possibility of a group not being able to sit together. For example, if the airplane column is 5 seats wide and a family of 5 books tickets, but the Economy Plus passengers take every window seat, then there won't be 5 remaining adjacent seats in order to seat the family. One alternative solution would be a bulk benefit where any group purchasing multiple Economy tickets automatically gets upgraded to Economy Plus, allowing them to choose their seats at the time of registration.
