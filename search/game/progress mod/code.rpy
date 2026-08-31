################################################################################
## Classes v0.35.0-01 2024-01-10
################################################################################

#
# Overview of how the mod works:
#
# 1. Game creates Event and Girl objects at launch based on files in progress mod\variables\
#     - event_list.rpy contains information for all events such as their triggers
#     - variables.rpy contains information for all girls and other misc vars
# 2. When the progress screen is opened, functions in update status.rpy are run
# 3. When the progress screen/hint tracker is opened:
#     1. ProgressMod.update_all() is run, causing 50 to 75 Event objects to
#        run Event.update_status(), updating their vars and generating a new event hint 
#

init python:

    # Class for information about the game's events
    class Event:

        import string

        def __init__(self, var_name, name, girl, chapter, event_type, reqs, skip_var = None, miss_preq = None, reqs1 = None, reqs2 = None, hint_girl = None):
            self.var_name = var_name                                    # the event's variable name in the game
            self.name = name                                            # the event's displayed name
            self.girl = girl                                            # the girl associated with the event (Girl object)
            self.hint_girl = hint_girl                                  # the girl to be used for the hint text (if different from self.girl)
            self.event_number = None                                    # the event's number in the girl's event list
            self.chapter = chapter                                      # the chapter the event appears in
            self.type = event_type                                      # the type of event (i.e, how it is triggered)
            self.reqs = reqs                                            # requirements to trigger the event
            self.skip_var = skip_var                                    # the variable indicating the event has been skipped, if any
            self.miss_preq = miss_preq                                  # the event's missable prerequisites, if any
            self.event_time = "day"                                     # used for distinguishing time of day when needed

            self.or_event = False                                       # does the event have an "or" in its requirements
            self.or_reqs = ""                                           # original set of requirments including "or"
            self.reqs1 = reqs1                                          # first set of requirements (used if the switch is true)
            self.reqs2 = reqs2                                          # second set of requirements (used if the switch is false)

            self.triggers = dict()                                      # dictionary to hold event's triggers

            self.ready = False                                          # is the event ready to fire?
            self.hint = ""                                              # the event hint text to be displayed
            self.attention = False                                      # whether to add (!) flag to event hint
            self.attention_type = 0                                     # the type of explanation to give for the (!) flag
            self.second_attention = 0                                   # for events that require two explanations for the (!) flag
            self.explain_text = ""
            self.second_explain_text = ""
            self.completed = False                                      # has the event been completed?
            self.missed = False                                         # has the event been permanently missed?
            self.blocked = True                                         # is something blocking this event's hint from the tracker?
            self.blocked_reason = ""                                    # why the event is blocked

            self.previous_event = "None"                                # previous event (when event is part of a chain)
            self.cutoff_event = "None"                                  # event that indicates that an event should not be blocked
            self.chain_processed = False                                # whether the event has been processed (if a chain event)

            self.handle_attention_hints()
            self.convert_or_requirements()
            self.process_triggers()
            self.process_lists()

        def handle_attention_hints(self):

            if "_att" in self.type:
                self.attention = True
                self.attention_type = int(self.type[-2:])
                self.type = self.type[0:self.type.find("_att")]   
            if self.type == "chain_lust_adv":
                if self.attention_type == 0:
                    self.attention_type = 2
                else:
                    self.second_attention = self.attention_type
                    self.attention_type = 2

        def convert_or_requirements(self):

            if " or " in self.reqs:
                self.or_handling()
                self.reqs = self.reqs2
                if self.or_choice() == 1:
                    self.reqs = self.reqs1

        def process_lists(self):

            self.girl.event_list.append(self)
            self.event_number = self.girl.event_list.index(self)
            if not self.type in ["chain", "chain_lust_adv", "firsthall"]:
                temp_list = self.determine_list()
                temp_list.append(self)

        # Method to determine which of a girl's lists an event belongs in (and creates it if necessary)
        def determine_list(self):

            if not "date" in self.type:
                if self.type in self.girl.event_lists.keys():
                    temp_list = self.girl.event_lists[self.type]
                else:
                    self.girl.event_lists[self.type] = []
                    temp_list = self.girl.event_lists[self.type]
            else:
                if "date" in self.girl.event_lists.keys():
                    temp_list = self.girl.event_lists["date"]
                else:
                    self.girl.event_lists["date"] = []
                    temp_list = self.girl.event_lists["date"]
            return temp_list

        # Method to break down an event's triggers (as found in self.reqs) by type
        def process_triggers(self):

            self.triggers["event_checks"] = []
            self.triggers["stat_checks"] = []
            self.triggers["love_req"] = 0
            self.triggers["lust_req"] = 0
            self.triggers["totaldays"] = 0
            self.triggers["day_restrictions"] = []
            self.triggers["day_restriction_text"] = ""

            if self.type == "chain_lust_adv":
                self.previous_event = self.reqs.split(", ")[1]
                self.reqs = self.reqs.split(", ")[0]

            if self.type == "camp":
                self.previous_event = self.reqs.split(", ")[1]
                self.reqs = self.reqs.split(", ")[0]

            trigger_list = self.reqs.split(" and ")
            for trigger in trigger_list:
                if trigger.split()[0] == self.var_name:
                    trigger_list.pop(trigger_list.index(trigger))
                elif trigger.split()[0] == "totaldays":
                    self.triggers["totaldays"] = int(self.reqs.split()[2])
                if self.girl.name.lower() + "_love" in trigger:
                    self.triggers["love_req"] = int(trigger.split()[2])
                if self.girl.name.lower() + "_lust" in trigger:
                    self.triggers["lust_req"] = int(trigger.split()[2])

            for x in range(len(trigger_list)):
                current_trigger = trigger_list[x]
                if current_trigger[-4:] == "True" or current_trigger[-5:] == "False":
                    current_name = current_trigger.split()[0]
                    if current_name in event_vars:
                        if current_name not in self.triggers["event_checks"]:
                            self.triggers["event_checks"].append("ev_" + current_name)
                elif current_trigger[0:3] == "day":
                    if not current_trigger == "day > 0":
                        self.triggers["day_restrictions"].append(current_trigger)
                elif "_love" in current_trigger or "_lust" in current_trigger:
                    self.triggers["stat_checks"].append(current_trigger)

            if "chapter_end" in self.reqs:
                self.triggers["day_restrictions"].append(self.reqs.split(", ")[1])
                self.reqs = "chapter_end"

            if "_night" in self.type:
                if self.type not in ["date_night", "weekend_night", "saturday_night"]:
                    self.event_time = "night"
                    self.type = self.type[:-6]
            elif "_afternoon" in self.type:
                if self.type not in ["date_afternoon", "weekend_afternoon", "saturday_afternoon"]:
                    self.event_time = "afternoon"
                    self.type = self.type[:-10]

            if len(self.triggers["day_restrictions"]) != 0:
                self.triggers["day_restrictions"].sort()
                self.triggers["day_restriction_text"] = self.generate_day_restrictions_text(*self.triggers["day_restrictions"])

        # Method to handle events which have an "or" in their trigger by breaking that down into
        # two sets of event requirements. Currently written around the only two events that fall
        # into this category. Will likely have to be adjusted for future events.

        def or_handling(self):

            self.or_event = True
            self.or_reqs = self.reqs
            parens = False          # do the event's triggers include parentheses?
            paren_start = 0         # the location of the first (
            paren_stop = 0          # the location of the final )

            if "(" in self.or_reqs and ")" in self.or_reqs:
                parens = True
                i = 0
                for c in self.or_reqs:
                    if c == "(" and paren_start == 0:
                        paren_start = i
                    if c == ")":
                        paren_stop = i
                    i = i + 1
                paren_substring = self.or_reqs[paren_start:paren_stop+1]    # "(rindate50 == True or (rindorm50special == True and rinbetrayed == True))"
                temp_reqs = self.or_reqs.replace(paren_substring,"")        # "totaldays >= 400 and secondbeach18 == True and and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False"
                if " and  and " in temp_reqs:
                    temp_reqs = temp_reqs.replace(" and  and ", " and ")    # "totaldays >= 400 and secondbeach18 == True and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False"
                or_place = paren_substring.find(" or ")
                or_first_half = paren_substring[0:or_place]           # "(rindate50 == True"
                or_second_half = paren_substring[or_place+4:]         # "(rindorm50special == True and rinbetrayed == True))"
                or_first_half = or_first_half.replace("(", "")        # "rindate50 == True"
                or_first_half = or_first_half.replace(")", "")
                or_second_half = or_second_half.replace("(", "")      # "rindorm50special == True and rinbetrayed == True))"
                or_second_half = or_second_half.replace(")", "")      # "rindorm50special == True and rinbetrayed == True"
                self.reqs1 = temp_reqs + " and " + or_first_half
                self.reqs2 = temp_reqs + " and " + or_second_half
            else:
                or_place = self.or_reqs.find(" or ")
                or_first_half = self.or_reqs[0:or_place]              # "totaldays >= 139 and chika_lust >= 5 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False"
                or_second_half = self.or_reqs[or_place+4:]            # "chikadorm20 == True and mall20 == True and chika_lust >= 10 and day139 == False"
                self.reqs1 = or_first_half
                self.reqs2 = or_second_half

        # Method used to determine which set of requirements an event with an "or" in
        # its triggers should currently be using

        def or_choice(self):

            choose_first = False
            choose_second = False
            or_num = 1

            or_triggers1 = self.reqs1.split(" and ")
            or_triggers2 = self.reqs2.split(" and ")
            for t in or_triggers1:
                if t.split()[0] in fixed_vars:
                    if eval(t) == False:
                        choose_second = True
                    else:
                        choose_first = True
            for t in or_triggers2:
                if t.split()[0] in fixed_vars:
                    if eval(t) == False:
                        choose_first = True
                    else:
                        choose_second = True

            if choose_first:
                or_num = 1
            else:
                or_num = 2

            return or_num

        # Method to convert a chain event's triggers to those of a normal event
        # its requirements are made to point to the previous event in the chain

        def process_chain(self):

            if self.type == "chain" and self.chain_processed == False:
                self.previous_event = self.reqs
                self.reqs = self.previous_event + " == True and " + self.var_name + " == False"
                self.process_triggers()
            self.chain_processed = True
            if self.reqs.split()[0] == "totaldays":
                self.triggers["totaldays"] = int(self.reqs.split()[2])

        # Method to update the event's various variables to reflect the player's progress
        # Events will only be updated if they are not from a previous chapter and have not been completed

        def update_status(self):
            if self.or_event:                                               # if the event has an "or" in its requirements, see which set to follow
                if self.or_choice() == 1:
                    self.reqs = self.reqs1
                else:
                    self.reqs = self.reqs2
                self.process_triggers()
            if eval(self.var_name) == False:
                self.completed = False
                self.missed = False
                if self.type == "chain" and self.chain_processed == False:
                    self.process_chain()
                if self.miss_preq is not None:
                    if eval(self.miss_preq) == True:
                        self.missed = True
                if self.skip_var is not None:
                    if eval(self.skip_var) == True:
                        self.missed = True
                if self.chapter == current_chapter or self.var_name in xchapter_hints:
                    self.hint = ""
                    self.generate_hint()
            else:
                self.completed = True
                self.hint = ""
            if not self.hint == "" and not self.hint == "Event will trigger automatically.":
                self.girl.has_hint = True

        # Method to provide a single event hint from the event's requirements
        # Example output: "Visit Sana's dorm room on Wednesday."
        # Hint precedence = Affection > Lust > Events

        def generate_hint(self, block_override = False):

            import string

            failed_stat_checks = 0
            failed_event_checks = 0
            self.day_restriction = ""                                   # string to hold one day of the week restriction for the hint
            continue_parsing = True                                     # tells the parser whether to stop
            skip_processing = False
            self.hint = ""
            self.ready = False

            # 0. Special Handling for Chain Lust, Happy, and Chapter End Events
            if self.type == "chain_lust_adv":
                continue_parsing = False
                skip_processing = True
                if eval(self.reqs):
                    self.hint = "Event will trigger automatically."
                else:
                    for t in self.triggers["event_checks"]:
                        if eval(t) == False:
                            if eval("ev_" + t.split()[0]).type in ["chain_lust", "chain_lust_adv"]:
                                if eval("ev_" + t.split()[0]).missed:
                                    self.missed = True
                    if self.missed == False:
                        missed_lust = False
                        for t in self.triggers["stat_checks"]:
                            if "lust" in t:
                                if eval(t) == False:
                                    missed_lust = True
                                    lust_girl = t.split()[0]
                                    lust_girl = eval(lust_girl.split("_")[0].capitalize())
                                    self.hint = lust_girl.lust
                                    self.hint = self.hint[:-1] + " to " + t.split()[2] + " {color=#EF1A1A}(!){/color}" + " (currently " + str(lust_girl.current_lust) + ")."
                        for t in self.triggers["event_checks"]:
                            if eval(t) == False:
                                self.hint = eval("ev_" + t.split()[0]).girl.name + " progress needed {color=#EF1A1A}(!){/color}"
                        if len(self.triggers["event_checks"]) == 0 and not missed_lust:
                            self.hint = "Event will trigger if correct choices are made in " + eval("ev_" + self.previous_event).name + " "
                # if the player has progressed too far in the game to see the event, it is marked as missed
                if eval(self.reqs) and not self.completed and not self.girl.name == "Molly":
                    # print(self.var_name)
                    next_event = eval("ev_" + self.previous_event)
                    next_event = next_event.girl.event_list[next_event.girl.event_list.index(next_event) + 1]
                    if next_event.completed:
                        self.missed = True

            if self.type == "happy":
                continue_parsing = False
                skip_processing = True
                for key in happy_tracks:
                    if self.var_name == key and eval(happy_tracks[key]):
                        self.hint = self.reqs
                    elif self.var_name == key and eval(happy_tracks[key]) == False:
                        self.hint = ""
                        self.blocked == True

            if self.type == "camp":
                continue_parsing = False
                skip_processing = True
                if eval(self.previous_event):
                    self.hint = self.reqs
                else:
                    self.hint = ""
                    self.blocked == True

            if "chapter_end" in self.reqs:
                continue_parsing = False
                skip_processing = True
                MainEvent.chapter_progress(self)
                if self.ready:
                    self.generate_hint_text()
                self.event_blocking()

            # 1. Initial Trigger Processing
            if not self.miss_preq == None:
                if eval(self.miss_preq) == True:
                    self.missed = True
                    skip_processing = True
                    continue_parsing = False
            if continue_parsing == True:
                for trigger in self.triggers["event_checks"]:
                    # current_event = eval(trigger)
                    current_event = ProgressMod.event_dict[trigger]
                    if current_event.completed == False:
                        failed_event_checks += 1
                        break
                for trigger in self.triggers["stat_checks"]:
                    if eval(trigger) == False:
                        failed_stat_checks += 1
                        affection_girl = self.get_girl_from_stat(trigger)
                        if "_love" in trigger:
                            self.hint = affection_girl.affection[:-1] + " to " + trigger.split()[-1] + " (currently " + str(affection_girl.current_love) + ")."
                        elif "_lust" in trigger:
                            self.hint = affection_girl.lust[:-1] + " to " + trigger.split()[-1] + " (currently " + str(affection_girl.current_lust) + ")."
                        break

            # 2. Event Triggers
            if failed_event_checks > 0 and failed_stat_checks == 0 and skip_processing == False:
                self.hint = self.missing_events(*self.triggers["event_checks"])

            # 3. Event Hint (if all triggers have been met)
            if failed_event_checks == 0 and failed_stat_checks == 0 and skip_processing == False:
                self.ready = True
                if not self.girl in [MainEvent, HappyEvent]:
                    self.generate_hint_text()
                elif self.girl == MainEvent:
                    if len(self.triggers["day_restrictions"]) == 1:
                        if self.type == "weekend_night":
                            self.hint = self.girl.wait_weekend_night
                        else:
                            self.girl.wait_set_day(self.triggers["day_restriction_text"])
                            self.hint = self.girl.wait_day
                    else:
                        MainEvent.wait_set_time(self)
            if "Event will trigger automatically" in self.hint:
                self.hint = "Event will trigger automatically."
            if self.girl == MainEvent and self.ready and self.type == "chain":
                self.hint = "Automatic event chain in progress."
            elif self.type == "chain" and self.ready and eval(self.previous_event):
                self.hint = "Automatic event chain in progress."
            if self.attention:
                if "(!)" not in self.hint:
                    if not "automatically" in self.hint:
                        self.hint = self.hint[:-1] + " {color=#EF1A1A}(!){/color}"

            # 4. Event Blocking
            if not self.girl == HappyEvent:
                self.event_blocking()
                if self.blocked or self.missed:
                    self.hint = ""
                if (self.completed or self.missed) and show_complete:
                    self.hint = ""

            return self.hint

        # Method to create a string indicating progress is needed in one or more event types
        # Example input: "ev_cafe20", "ev_soccer20", "ev_streets15" (strings)
        # Example output: "Rin, Miku progress needed."

        def missing_events(self, *event_list):

            missing_list = ""                                                                                   # string to hold the events that the player still needs to complete
            already_added = []                                                                                  # used to prevent duplicates in list of girls
            for event in event_list:                                                                            # for each event in the provided list,
                event_name = ProgressMod.event_dict[event]
                if not event_name.completed:                                                                    # check to see if the event has been seen
                    if event_name in MainEvent.event_list and "main" not in already_added:                      # main events
                        missing_list = missing_list + MainEvent.colored_name + ", "
                        already_added.append("main")
                    elif event_name in HappyEvent.event_list and "happy" not in already_added:                  # happy events
                        missing_list = missing_list + HappyEvent.colored_name + ", "
                        already_added.append("happy")
                    else:                                                                                       # girl events
                        for current_girl in girls_list:
                            if event_name in current_girl.event_list and current_girl.name not in already_added:
                                missing_list = missing_list + current_girl.colored_name + ", "
                                already_added.append(current_girl.name)
                                break
            missing_list = missing_list[:-2] + " progress needed."
            return missing_list

        # Method to strip Boolean checks from a string
        # Example input: "kaoridate15p3 == True"
        # Example output: ev_kaoridate15p3 (Event object)
        def get_event(self, current_trigger):

            if current_trigger[-4:] == "True":
                current_trigger = current_trigger[:-8]
            elif current_trigger[-5:] == "False":
                current_trigger = current_trigger[:-9]
            current_trigger = eval("ev_" + current_trigger)
            return current_trigger

        # Method to determine the girl associated with a given affection or lust check
        # Example input: "touka_love >= 5"
        # Example output: Touka (Girl object)
        def get_girl_from_stat(self, var_name):

            component = var_name.split()                                 # splits the check into its component parts ("touka_love", ">=", "5")
            var_name = component[0]                                      # first component of the check ("touka_love")
            var_name = var_name.capitalize()                             # "Touka_love"
            var_name = var_name[:-5]                                     # "Touka"
            var_name = eval(var_name)                                    # Touka (Girl object)
            return var_name

        # Method to generate text explaining the day of the week restrictions for an event
        # Example input: "day != 2", "day < 5"
        # Example output: "a weekday other than Tuesday"
        def generate_day_restrictions_text(self, *temp_list):

            weekend_restriction = False                             # whether the event is weekend only
            weekday_restriction = False                             # whether the event is weekday only
            restriction_text = ""
            temp_restriction = ""
            exclude_day = []                                        # list of days the event cannot happen on
            restriction_list = []                                   # list of all restrictions
            greater_than = False
            lesser_than = False
            min_range = 0
            max_range = 7

            for element in temp_list:                               # copies input to new list (needed by Ren'py for some reason)
                restriction_list.append(element)

            for element in restriction_list:                                                                # goes through each element and
                if "!=" in element:                                                                         # adds any prohibited days to the appropriate list
                    exclude_day.append(element)
                if ">" in element:                                                                          # designates the event as weekend only
                    if "> 5" in element:
                        weekend_restriction = True
                    greater_than = True
                    min_range = int(element[-1:]) + 1                                                       # ("+1" is needed to exclude the first day from range)
                if "<" in element:                                                                          # designates the event as weekday only
                    if "< 6" in element:
                        weekday_restriction = True
                    lesser_than = True
                    max_range = int(element[-1:])

            if greater_than and lesser_than:                                                                # if there are both > and < in the restrictions
                weekday_restriction = False                                                                 # override other weekend/weekday designations
                weekend_restriction = False

            if len(exclude_day) >= 2:
                if "day != 6" in exclude_day and "day != 7" in exclude_day:                                 # replaces "day != 6 and day != 7" with "day < 6"
                    weekday_restriction = True
                    exclude_day.remove("day != 6")                   
                    exclude_day.remove("day != 7")
                    restriction_list.remove("day != 6")
                    restriction_list.remove("day != 7")
                    restriction_list.append("day < 6")
            if weekend_restriction == True and len(restriction_list) == 1:                                  # "Weekend"
                restriction_text = "Weekend"
            elif weekday_restriction == True and len(restriction_list) == 1:                                # "a weekday"
                restriction_text = "a weekday"
            elif "==" in restriction_list[0]:                                                               # "Tuesday"
                temp = restriction_list[0]
                restriction_text = days_of_the_week[int(temp[-1:])]
            else:
                if weekday_restriction == True:                                                             # "a weekday other than [Monday]"
                    restriction_text = "a weekday other than "
                elif greater_than and lesser_than:                                                              # "day > 2 and day < 6"
                    for i in range(min_range, max_range):
                        restriction_text = restriction_text + days_of_the_week[i] + " or "                      # "Wednesday or Thursday or Friday"
                    if len(range(min_range, max_range)) > 2:
                        temp_restriction = restriction_text.split()[0]
                        for i in range(len(range(min_range, max_range)) - 2):                                   # "- 2" to exclude the first and last days
                            temp_restriction = temp_restriction + ", " + restriction_text.split()[(i+1)*2]
                        temp_restriction = temp_restriction + ", or " + restriction_text.split()[-2] + " or "
                        restriction_text = temp_restriction                                                     # "Wednesday, Thursday, or Friday"
                elif lesser_than and not greater_than:
                    if self.event_time == "day":
                        restriction_text = "a weekday before " + days_of_the_week[max_range]  + " or "
                    elif self.event_time == "afternoon":    
                        restriction_text = "a weekday afternoon before " + days_of_the_week[max_range]  + " or "
                    elif self.event_time == "night":
                        restriction_text = "a weeknight before " + days_of_the_week[max_range]  + " or "
                else:                                                                                       # "not [Tuesday or Friday]"
                    restriction_text = restriction_text + "not "
                for i in exclude_day:
                    temp = i
                    restriction_text = restriction_text + days_of_the_week[int(temp[-1:])] + " or "
                restriction_text = restriction_text[:-4]
            if "date" in self.type:
                time = ""
                time = self.type.split("_")[1]
                if not self.type == "date_work":
                    if not restriction_text == "":
                        restriction_text = restriction_text + " " + time
            if "night" in self.type:
                restriction_text = restriction_text + " (evening)"
            elif "afternoon" in self.type:
                restriction_text = restriction_text + " (afternoon)"
            return restriction_text

        # Method to generate hint for an event whose triggers have all been met
        # Example output: "Visit Sana's dorm room'"
        def generate_hint_text(self):

            if self.hint_girl is not None:
                event_girl = self.hint_girl
            else:
                event_girl = self.girl

            if self.type in ["work", "work2", "dorm", "dorm2", "invite"]:
                temp_hint = event_girl.name + ".visit_" + self.type
                if self.type == "invite":
                    temp_hint = event_girl.name + "." + self.type
                temp_restrict = temp_hint + "_set_restriction('" + self.triggers["day_restriction_text"] + "')"
                if self.triggers["day_restriction_text"] == "":
                    self.hint = eval(temp_hint)
                else:
                    self.hint = eval(temp_restrict)
            elif self.type == "firsthall":                                                                      # generates hint for firsthall events (i.e., "sanafirsthall")
                self.hint = event_girl.firsthall
            elif "date" in self.type:
                time = ""
                time = self.type.split("_")[1]
                if not self.type == "date_work":
                    if self.triggers["day_restriction_text"] == "":
                        self.hint = eval(event_girl.name + ".call_" + time)
                else:
                    self.hint = event_girl.visit_work
                if not self.triggers["day_restriction_text"] == "":
                    self.hint = event_girl.call_set_restriction(self.triggers["day_restriction_text"])
            elif self.type in ["weekday_morning", "weekend_morning", "weekend_afternoon", "weekend_night", "saturday_morning", "saturday_afternoon", "saturday_night"]:
                if self.triggers["day_restriction_text"] == "":
                    target_time = event_girl.name + ".wait_" + self.type
                    self.hint = eval(target_time)
                else:
                    if len(self.triggers["day_restrictions"]) == 1 and self.type in ["saturday_morning", "saturday_afternoon", "saturday_night"]:
                        target_time = event_girl.name + ".wait_" + self.type
                        if self.girl == MainEvent:
                            target_time = "MainEvent.wait_" + self.type
                        self.hint = eval(target_time)
                    else:
                        self.hint = event_girl.wait_set_restriction(self.triggers["day_restriction_text"])

            if not event_girl == self.girl:
                self.hint = self.hint[:-1] + " (" + event_girl.colored_name + ")."

        # Method to determine whether or not the hint for an incomplete event should appear in the appropriate event tracker
        # Events will be blocked from appearing if:
        #
        # 1. Its triggers include an unseen main event or an unseen event from the same girl
        # 2. The requisite number of days have not passed in the game
        # 3. The triggers include an event from an earlier chapter
        # 4a. For girls, there is an earlier unseen event of the same type
        # 4b. For main events, there is an ealier unseen event of the same type ready to fire
        # 5. Chain_lust events appear one update in advance to provide advance notice

        def event_blocking(self):

            self.blocked = False
            self.blocked_reason = ""
            for event in self.triggers["event_checks"]:
                trigger = ProgressMod.event_dict[event]
                if trigger.completed:
                    trigger.blocked = False
                else:
                    if trigger.girl == MainEvent or trigger.girl == self.girl:
                        self.blocked_reason = "Unseen main event/same girl event in triggers"
                        break
                if trigger.blocked:
                    self.blocked_reason = "Blocked event in triggers"
                    break
                if not trigger.girl == MainEvent and not trigger.girl == HappyEvent:
                    if not trigger.girl.active:
                        self.blocked_reason = "Event for inactive girl in triggers"
                        break

            if self.girl in girls_list:
                if not self.type in ["firsthall", "chain", "chain_lust_adv", "camp"]:
                    temp_list = self.determine_list()
                    if not self in temp_list:
                        temp_list.append(self)
                    order_number = temp_list.index(self)
                    if not order_number == 0:
                        if temp_list[order_number-1].completed == False and temp_list[order_number-1].missed == False:
                            self.blocked_reason = "Earlier unseen event of the same type"
                if self.type == "camp":
                    if not ev_sportswars20.completed:
                        self.blocked_reason = "Too early for event"
                if self.var_name in ["mollyspring1","toukaspring1"]:
                    if not ev_saracamp2.completed:
                        self.blocked_reason = "Too early for event"
            if self.ready:
                if self.girl == MainEvent:
                    if not self.type == "chain":
                        temp_list = MainEvent.event_lists[self.type]
                        order_number = temp_list.index(self)
                        if not order_number == 0:
                            if temp_list[order_number-1].completed == False and temp_list[order_number-1].missed == False:
                                if temp_list[order_number-1].ready:
                                    self.blocked_reason = "Earlier unseen event of the same type"

            if self.type in ["chain_lust", "chain_lust_adv"]:
                trigger_event = eval("ev_" + self.previous_event)
                for key in chain_lust_timing:
                    if key in trigger_event.var_name:
                        if eval(chain_lust_timing[key]) == False:
                            self.blocked_reason = "Too early to show chain lust event"
            if self.type == "chain":
                prev = eval("ev_" + self.previous_event)
                if not self.girl == prev.girl:
                    if not eval(self.previous_event):
                        self.blocked_reason = "Later part of a chain"
            if "chapter_end" in self.reqs:
                if "Main event" in self.hint:
                    self.blocked_reason = "Chapter End event with unresolved main events"
            if totaldays < self.triggers["totaldays"]:
                self.blocked_reason = "Not enought days spent in game"
            if self.chapter < current_chapter:
                self.blocked_reason = "Event from an earlier chapter"
            if not self.blocked_reason == "":
                self.blocked = True

    # Class for each girl with events
    class Girl:

        def __init__(self, name, color, hall, work, work2 = "N/A"):
            self.name = name                                    # the girl's name
            self.color = color                                  # the color associated with her
            self.hall = hall                                    # the day of the week she is in the hallway
            self.work = work                                    # the non-dorm location where she has events
            self.work2 = work2                                  # second non-dorm location where she has events (if any)
            self.event_list = []                                # list for holding all events for the girl
            self.has_hint = False                               # has an event with a non-blank hint
            self.max = []                                       # list of total number of events the girl has in each chapter
            self.max.append(0)                                  # done to make the list index match directly with chapter numbers
            self.current_max = 0                                # number of total number of events the girl has in the current chapter
            self.active = False                                 # has the girl become active in the game yet

            self.highest_completed = 0                          # the highest event completed in her event list
            self.current_points = 0                             # the girl's combined number of seen and missed events
            self.current_love = 0
            self.current_lust = 0
            self.next_love = 0
            self.next_lust = 0
            self.lust_active = True                             # not currently used

            self.event_lists = dict()

            # Creates a string with the girl's name and the needed Renpy code to make it her color
            # (doing this in three steps is a workaround to prevent a Renpy error when starting the game)
            coloring1 = "{color=" + self.color
            coloring2 = "}"
            self.colored_name = coloring1 + coloring2 + self.name + "{/color}"

            # Strings to provide specific event hints
            self.firsthall = "Talk to " + self.colored_name + " in the dorm hallway (" + self.hall + ")."
            self.visit_dorm = "Visit " + self.colored_name + "'s dorm room."
            self.visit_dorm2 = "Meet " + self.colored_name + " at the dorms."
            self.visit_work = "Visit " + self.work + "."
            self.visit_work2 = "Visit " + self.work2 + "."
            self.call_morning = "Call " + self.colored_name + " in the morning."
            self.call_afternoon = "Call " + self.colored_name + " in the afternoon."
            self.call_night = "Call " + self.colored_name + " at night."
            self.invite = "Invite " + self.colored_name + " over."
            self.affection = "Increase " + self.colored_name + "'s affection."
            self.lust = "Increase " + self.colored_name + "'s lust."

            self.wait = "Wait for more time to pass."
            self.wait_weekday_morning = "Wait for a weekday."
            self.wait_weekend_morning = "Wait for the weekend."
            self.wait_weekend_afternoon = "Wait for the weekend (afternoon)"
            self.wait_weekend_night = "Wait for the weekend (night)."
            self.wait_saturday_morning = "Wait for Saturday."
            self.wait_saturday_afternoon = "Wait for Saturday afternoon."
            self.wait_saturday_night = "Wait for Saturday night."

        # Methods to create strings incorporating additional requirements, i.e. "not Tuesday" or "a weekday"
        def visit_dorm_set_restriction(self, restriction):
            visit_dorm_restricted = "Visit " + self.colored_name + "'s dorm room (" + restriction + ")."
            return visit_dorm_restricted
        def visit_work_set_restriction(self, restriction):
            visit_work_restricted = "Visit " + self.work + " (" + restriction + ")."
            return visit_work_restricted
        def visit_work2_set_restriction(self, restriction):
            visit_work_restricted = "Visit " + self.work2 + " (" + restriction + ")."
            return visit_work_restricted
        def call_set_restriction(self, restriction):
            call_restricted = "Call " + self.colored_name + " (" + restriction + ")."
            return call_restricted
        def invite_set_restriction(self, restriction):
            invite_restricted = "Invite " + self.colored_name + " over (" + restriction + ")."
            return invite_restricted
        def wait_set_restriction(self, restriction):
            wait_restricted = "Wait until " + restriction + "."
            return wait_restricted

        # Method to create a string incorporating a time requirement, i.e. "not Tuesday" or "a weekday"
        def wait_set_day(self, restriction):
            self.wait_day = "Wait until " + restriction + "."

        # Method to update variables related to a girl's progress
        def progress_check(self):

            self.current_love = eval(self.name.lower() + "_love")
            self.current_points = eval(self.name.lower() + "point") + eval(self.name.lower() + "miss")
            if not eval(self.name.lower() + "_lust") == "N/A":
                self.current_lust = eval(self.name.lower() + "_lust")
            event_progress = self.current_points - 1
            if event_progress < 0:
                event_progress = 0
            self.highest_completed = event_progress
            return event_progress

        # Method to determine the love and lust values needed for the girl's next events
        def next_vals(self):
            self.next_love = 0
            self.next_lust = 0

            for stat in ["love", "lust"]:
                found = False
                for i in range(len(self.event_list)):
                    # if not self.event_list[i].completed and found == False:
                    if not self.event_list[i].completed and found == False and not eval(self.name.lower() + "_" + stat) == "N/A":
                        # if self.event_list[i].triggers[stat + "_req"] > eval(self.name.lower() + "_" + stat):
                        if self.event_list[i].triggers[stat + "_req"] > int(eval(self.name.lower() + "_" + stat)):
                            if stat == "love":
                                self.next_love = self.event_list[i].triggers[stat + "_req"]
                            else:
                                self.next_lust = self.event_list[i].triggers[stat + "_req"]
                            found = True

    # Class to hold methods and variables not specific to a particular girl
    class StoryEvent:

        def __init__(self, name, color):

            self.name = name
            self.color = color
            self.max = []                                       # total number of events the girl has in the current chapter
            self.max.append(0)
            self.current_max = 0
            self.has_hint = False                               # has an event with a non-blank hint
            self.points = 0
            self.highest_completed = 0
            self.active = True
            self.temp_points = 0

            # Copied from Girl
            coloring1 = "{color=" + self.color
            coloring2 = "}"
            self.colored_name = coloring1 + coloring2 + self.name + "{/color}"

            self.event_list = []                                # list for holding all events for the girl

            # String to provide non-girl-specific event hints
            self.wait = "Wait for more time to pass."
            self.wait_weekday_morning = "Wait for a weekday."
            self.wait_weekend_morning = "Wait for the weekend."
            self.wait_weekend_afternoon = "Wait for the weekend (afternoon)"
            self.wait_weekend_night = "Wait for the weekend (night)."
            self.wait_saturday_morning = "Wait for Saturday."
            self.wait_saturday_afternoon = "Wait for Saturday afternoon."
            self.wait_saturday_night = "Wait for Saturday night."
            self.missed = "You will not be able to see this event."

            self.event_hint = ""        # used by parse_triggers(), stores the final event hint to be given to the player
            self.attention = False      # used by parse_triggers() to mark events needing (!)

            self.event_lists = dict()

        # Method to create a string incorporating a time requirement, i.e. "not Tuesday" or "a weekday"
        def wait_set_day(self, restriction):
            self.wait_day = "Wait until " + restriction + "."

        # method to create a string including a generic time requirement
        def wait_set_time(self, target_event):

            if not target_event.type in ["chain", "chain_lust_adv"]:
                if self == MainEvent:
                    target_time = "MainEvent.wait_" + target_event.type
                    target_event.hint = eval(target_time)
                elif self == HappyEvent:
                    target_time = "HappyEvent.wait_" + target_event.type
                    target_event.hint = eval(target_time)
            else:
                target_event.hint = "Automatic event chain in progress."

        def wait_set_restriction(self, restriction):
            wait_restricted = "Wait until " + restriction + "."
            return wait_restricted

        # Method to generate the hint for chapter_end events

        # Post-Chapter End Cutoff Events:
        # 1: 2 Main, 1 Happy
        # 2: 3 Main, 1 Happy, 4 Ami
        # 3: 20 Main, 1 Happy, 1 Ami
        # 4: 12 Main, 0 Happy, 

        def chapter_progress(self, target_event):

            main_missing = [0,2,3,20,13]                # list to hold the number of post-cutoff main events (2 in chapter 1, 3 in chapter 2, 20 in chapter 3)
            happy_missing = [0,1,1,1,0]                 # list to hold the number of post-cutoff happy events (1 each in chapters 1 to 3)
            girls_missing = dict()                      # dictionary to hold the number of post-cutoff events for each girl
            girls_missing["Ami"] = [0,0,4,1,0]            # 4 post-cutoff Ami events in chapter 2, 1 in chapter 3
            girls_missing["Ayane"] = [0,0,0,0,1]
            girls_missing["Futaba"] = [0,0,0,0,2]
            girls_missing["Haruka"] = [0,0,0,0,2]
            girls_missing["Kirin"] = [0,0,0,0,2]
            girls_missing["Makoto"] = [0,0,0,0,2]
            girls_missing["Maya"] = [0,0,0,0,3]
            girls_missing["Niki"] = [0,0,0,0,1]
            girls_missing["Nodoka"] = [0,0,0,0,4]
            girls_missing["Otoha"] = [0,0,0,0,3]
            girls_missing["Sara"] = [0,0,0,0,1]
            girls_missing["Tsubasa"] = [0,0,0,0,2]
            girls_missing["Tsukasa"] = [0,0,0,0,3]
            girls_missing["Tsuneyo"] = [0,0,0,0,2]
            girls_missing["Uta"] = [0,0,0,0,1]
            girls_missing["Yasu"] = [0,0,0,0,3]
            girls_missing["Yumi"] = [0,0,0,0,2]
            missing_list = ""

            if self.points < self.max[current_chapter] - main_missing[current_chapter]:
                missing_list = missing_list + self.colored_name + ", "
            if HappyEvent.points + happymiss < HappyEvent.max[current_chapter] - happy_missing[current_chapter]:
                missing_list = missing_list + HappyEvent.colored_name + ", "
            for current_girl in girls_list:
                if not current_girl == target_event.girl:
                    if current_girl.name in girls_missing.keys():
                        if current_girl.current_points < current_girl.max[current_chapter] - girls_missing[current_girl.name][current_chapter]:
                            missing_list = missing_list + current_girl.colored_name + ", "
                    elif current_girl.current_points < current_girl.max[current_chapter]:
                        missing_list = missing_list + current_girl.colored_name + ", "
            if len(missing_list[:-2]) > 0:
                target_event.hint = missing_list[:-2] + " progress needed."
            else:
                target_event.ready = True

        def progress_check(self):

            event_progress = self.points - 1
            if event_progress < 0:
                event_progress = 0
            self.highest_completed = event_progress

            return event_progress

    # class to hold non-girl and event specific variables and methods

    class LiLMod:

        def __init__(self):

            self.all_girls = girls_list[:]
            self.all_girls.append(MainEvent)
            self.all_girls.append(HappyEvent)

            self.chapter_values()
            self.event_list = []
            self.event_dict = dict()
            self.current_hints = dict()
            self.explain_list = dict()
            self.longest_hint = 0

            for current_girl in self.all_girls:
                for current_event in current_girl.event_list:
                    self.event_dict["ev_" + current_event.var_name] = current_event
                    if current_event.attention or current_event.type == "chain_lust_adv":
                        self.explain_list[current_event.var_name] = {"var_name" : current_event.var_name, "girl" : current_event.girl.name}

        # method to determine the chapter values to be shown on the Progress Screen in each chapter
        def chapter_values(self):

            highest_chapter = MainEvent.event_list[-1].chapter

            ch_counts = []
            ch_counts.append(0)
            for ch in range(highest_chapter):
                ch_counts.append(0)

            for current_girl in self.all_girls:
                if len(current_girl.max) < (highest_chapter + 1):
                    for ch in range(highest_chapter):
                        current_girl.max.append(0)
            for current_girl in self.all_girls:
                for ch in range(highest_chapter):
                    ch_counts[ch+1] = 0
                for ch in range(highest_chapter):
                    for current_event in current_girl.event_list:
                        if current_event.chapter == ch + 1:
                            ch_counts[ch+1] = ch_counts[ch+1] + 1
                    current_girl.max[ch+1] = ch_counts[ch+1]
                    current_girl.max[ch+1] = current_girl.max[ch+1] + current_girl.max[ch]

        # method to update the hints and certain variables for all events
        def update_all(self):

            self.current_hints = dict()
            self.longest_name = 0
            for current_girl in self.all_girls:
                current_girl.has_hint = False
                current_girl.progress_check()
                if current_girl.active:
                    for current_event in current_girl.event_list:
                        current_event.hint = ""
                        if current_event.event_number < current_event.girl.highest_completed + 6:
                            current_event.update_status()
                            if not current_event.hint in ["", "Event will trigger automatically."]:
                                self.current_hints[current_event.var_name] = {"var_name" : current_event.var_name, "girl" : current_event.girl.name, "hint" : current_event.hint}
                                if len(current_event.name) > self.longest_name:
                                    self.longest_name = len(current_event.name)
                if current_girl in girls_list:
                    if show_next:
                        current_girl.next_vals()