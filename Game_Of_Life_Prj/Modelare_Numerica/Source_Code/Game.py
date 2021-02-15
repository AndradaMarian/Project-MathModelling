from Modelare_Numerica.Source_Code.Display import Display


class Game:
    def __init__(self, initial_state, rules,max_size):
        self.initial_state = initial_state
        self.rules = rules
        self.max_size = max_size

    def run_game(self, it, delay_time):
        state = self.initial_state
        previous_state = None
        progression = []
        i = 0
        display = Display(self.max_size)
        first = None
        if(state.equals(previous_state)): # If a stable state is reached before the end cycles
            print("Stable after: "+str(i)+" iterations!")
        while (i < it):
            i += 1
            previous_state = state.copy()
            progression.append(previous_state.grid)
            state = state.apply_rules(self.rules,self.max_size)
            x,y=display.proc_state(state.grid)
            if not first: # Workaround to intialize the first plot and prepare the specific struct for further iterations
                first = True
                display.first_figure(x,y)
            else:
                display.update_figure(x,y)
            display.delay_interval(delay_time) # Small delay for a better visualisation