"""This program simulates the sales of tickets for a specific flight.

A plane is represented by a list. Each element of the list is a row in
the plane (with plane[0] being the front) and each row is also a
list.

Seats can be purchased as economy_plus or regular economy.

Economy_plus passengers select their seats when they purchase their tickts.
Economy passengers are assigned randomly when the flight is closer to full.

New: Economy passengers who book as a group will be seated together if possible.

create_plane(rows,cols):
  Creates and returns a plane of size rowsxcols
  Plans have windows but no aisles (to keep the simulation simple)

get_number_economy_sold(economy_sold):
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex: {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3
    seats, the Lee family 2

    Returns: the total number of seats sold

get_avail_seats(plane,economy_sold):
    Parameters: plane : a list of lists representing plaine
    economy_sold : a dictionary of the economy seats sold but
                   not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats
           that are "avail" or "win" and removes the number of
           economy_sold seats

get_total_seats(plane):
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane

get_plane_string(plane):
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 

purchase_economy_plus(plane,economy_sold,name):
    Params: plane - a list of lists representing a plane

            economy_sold - a dictionary representing the economy
                           sold but not assigned
            name - the name of the person purchasing the seat

    This routine randomly selects a seat for a person purchasing
    economy_plus. Preference is given to window and front seats.

seat_economy(plane,economy_sold,name):
    Similar to purchase_economy_plus but just randomy assigns
    a random seat.

purchase_economy_block(plane,economy_sold,number,name):
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary


fill_plane(plane):
  takes an empty plane and runs our simulation to sell seats and then
  seat the economy passengers. See comments in the function for details. 

main():
  The main driver program - start here

"""
import random


def create_plane(rows, cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists. 

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"] + ["avail"] * (cols - 2) + ["win"]
        plane.append(s)
    return plane


def get_number_economy_sold(economy_sold):
    """
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane, economy_sold):
    """
    Parameters: plane : a list of lists representing plane
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of economy_sold seats
    """
    avail = 0
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail


def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane) * len(plane[0])


def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s" % x for x in r
             ]  # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_economy_plus(plane, economy_sold, name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])

    # total unassigned seats
    seats = get_avail_seats(plane, economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane

    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0]) - 1] == "win":
                plane[row][len(plane[0]) - 1] = name
                return plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not (found_seat):
        r_row = random.randrange(0, rows)
        r_col = random.randrange(0, cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


# # THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
# def seat_economy(plane, economy_sold, name):
#     """
#     This is mostly the same as the purchase_economy_plus routine but 
#     just does the random assignment. 

#     We use this when we're ready to assign the economy seats after most 
#     of the economy plus seats are sold

 
#     """
#     rows = len(plane)
#     cols = len(plane[0])

#     found_seat = False
#     while not (found_seat):
#         r_row = random.randrange(0, rows)
#         r_col = random.randrange(0, cols)
#         if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
#             plane[r_row][r_col] = name
#             found_seat = True
#     return plane

def seat_economy_groups(plane, economy_list):
  for group in economy_list:
    print("seating group " + group[0])
    plane = seat_one_group(plane, group, economy_list)
    print(economy_list)
    print("current plane is:")
    print(get_plane_string(plane))

  return plane

def seat_one_group(plane, group, economy_list):
  seats_needed = group[1]
  rows = len(plane)
  cols = len(plane[0])
  found_seats = False
  for row_num in range(rows):
    for col_num in range(cols-seats_needed+1):
      found_seats= True
      for num in range(seats_needed):
        found_seats *= check_seat(plane, row_num, col_num+num)
        # print("found_seats value is " + str(found_seats))
        if found_seats == 0:
          break
      if found_seats == True:
        print("found " + str(seats_needed) + " seats together at " + str(row_num) + str(col_num))
        for num in range(seats_needed):
          plane[row_num][col_num+num] = group[0]
        return plane
  # If we get to this point without returning, it means the plane doesn't have enough adjacent seats to sit the group
  print("Unable to seat the group together")
  # Split the group into two smaller groups and seat those instead (groups are split in half rather than shrinking by one so that a group of 4 would split into two pairs-- I think this has the best chance of keeping passengers happy)
  # This is slightly messy since the split groups get appended into the list but the earlier booking with the full group isn't removed. It would probably be better to remove the original group from economy_list, but that messes up the for loop. To fix, the for loop would need to be done by index and you could subtract one from the index after removing the original group 
  economy_list.append((group[0], group[1]//2 + group[1]%2))
  economy_list.append((group[0], group[1]//2))
  # Reorder the list so that it's in order by descending group size but then for groups that have the same #, it's ordered alphabetically (which means the groups that booked earlier come first)
  economy_list.sort(key=first_item, reverse=False)
  economy_list.sort(key=second_item, reverse=True)
  return plane

def check_seat(plane, r, c):
  # print("Is there a seat at %s %s" %(str(r), str(c)))
  # print(plane[r][c] == "win" or plane[r][c] == "avail")
  return plane[r][c] == "win" or plane[r][c] == "avail"

def first_item(tuple):
  return tuple[0]

def second_item(tuple):
  return tuple[1]

def sort_largest_group(economy_sold):
  """Takes the dictionary of economy orders and turns it into a list of tuples, then sorts the list by descending number of tickets so that the largest groups are listed first"""
  economy_list = list(economy_sold.items())
  economy_list.sort(key=second_item, reverse=True) 
  print(economy_list)
  return (economy_list)


def purchase_economy_block(plane, economy_sold, number, name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_avail_seats(plane, economy_sold)
    # seats_avail = seats_avail - get_number_economy_sold(economy_sold)

    # print("seats available: " + str(seats_avail))

    if seats_avail >= number:
        economy_sold[name] = number
    return economy_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """

    economy_sold = {}
    total_seats = get_total_seats(plane)

    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number = 1
    u_number = 1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 3
    while total_seats > 1:
        r = random.randrange(100)
        if r > 20:
          plane = purchase_economy_plus(plane, economy_sold,
                                          "ep-%d" % ep_number)
          ep_number = ep_number + 1
          total_seats = get_avail_seats(plane, economy_sold)
          # print("purchasing economy plus ticket")
          # print("total seats avail: " + str(total_seats))
        else:
            economy_sold = purchase_economy_block(
                plane, economy_sold, 1 + random.randrange(max_family_size),
                "u-%d" % u_number)
            u_number = u_number + 1
            total_seats = get_avail_seats(plane, economy_sold)
            # print("purchasing economy tickets")
            # print("total seats avail: " + str(total_seats))

    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section

    economy_sorted = sort_largest_group(economy_sold)

    plane = seat_economy_groups(plane, economy_sorted)

    # for name in economy_sold.keys():
    #     for i in range(economy_sold[name]):
    #         plane = seat_economy(plane, economy_sold, name)

    return plane


def main():
    plane = create_plane(7, 5)
    plane = fill_plane(plane)
    print(get_plane_string(plane))


if __name__ == "__main__":
    main()
