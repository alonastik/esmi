TRAIN_DATA = [
    # ("exit", {"entities": [(0, 4, "ACTION")]}),
    ("create a meeting on 12.2.2019 9:00AM for fuseday at tikal",
     {"entities": [(0, 6, "ACTION"),
                   (20, 36, "DATE"),
                   (41, 48, "PURPOSE"),
                   (52, 57, "LOCATION")]}),
    ("delete a meeting on 30.3.2019 10:00PM",
     {"entities": [(0, 6, "ACTION"),
                   (20, 37, "DATE")]}),
    ("set an appointment for miri review on 12.2.2019 11:00AM at the office",
     {"entities": [(0, 3, "ACTION"),
                   (23, 34, "PURPOSE"),
                   (38, 55, "DATE"),
                   (59, 69, "LOCATION")]})]

