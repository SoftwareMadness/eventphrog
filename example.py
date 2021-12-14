from eventphrog import EventPhrog


phrog = EventPhrog()

phrog.create_driver()
phrog.open_event(##Your URL##)
print(phrog.getRatio()) # Get How many Seats are booked
phrog.close()
