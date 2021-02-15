class The_Board_Builder:

    def parse_grid(self, grid): # Parses the list of tuples and return a set of points
        piece_list = []
        for item in grid:
            if len(item) == 3:
                piece_position = self.build_pieces(item[0],item[1],item[2])
            else:
                piece_position = self.build_pieces(item[0], item[1], None)
            piece_list += piece_position
        return set(piece_list)

    # https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    def build_pieces(self, x_start, y_start, piece_name): # Build every piece from points, according to wiki scheme,
                                                        #  x_start and y_start being the top-left most point

        piece_points = []

        if piece_name is None:
            piece_points.append((x_start, y_start))

        if piece_name == "Eater":
            piece_points.append((x_start+2,y_start ))
            piece_points.append((x_start+3, y_start ))
            piece_points.append((x_start+1, y_start +1 ))
            piece_points.append((x_start+3, y_start + 1))
            piece_points.append((x_start+1, y_start + 2))
            piece_points.append((x_start, y_start + 3))
            piece_points.append((x_start + 1, y_start + 3))

        if piece_name == "Toad":
            piece_points.append((x_start+1,y_start ))
            piece_points.append((x_start+2, y_start ))
            piece_points.append((x_start+3, y_start ))
            piece_points.append((x_start, y_start + 1))
            piece_points.append((x_start+1, y_start + 1))
            piece_points.append((x_start+2, y_start + 1))

        if piece_name == "Glider":
            piece_points.append((x_start+1,y_start))
            piece_points.append((x_start+1, y_start+1))
            piece_points.append((x_start + 2, y_start+1))
            piece_points.append((x_start, y_start + 2))
            piece_points.append((x_start+2, y_start + 2))

        if piece_name == "Block":
            piece_points.append((x_start,y_start))
            piece_points.append((x_start+1, y_start))
            piece_points.append((x_start, y_start + 1))
            piece_points.append((x_start+1, y_start + 1))

        if piece_name == "Blinker":
            piece_points.append((x_start,y_start))
            piece_points.append((x_start+1, y_start))
            piece_points.append((x_start + 2, y_start))

        if piece_name == "Bee-hive":
            piece_points.append((x_start + 1 , y_start))
            piece_points.append((x_start , y_start+1))
            piece_points.append((x_start+2, y_start + 1))
            piece_points.append((x_start , y_start + 2))
            piece_points.append((x_start +2 , y_start + 2))
            piece_points.append((x_start +1, y_start+3))


        if piece_name == "Loaf":
            piece_points.append((x_start + 1, y_start))
            piece_points.append((x_start + 2, y_start))
            piece_points.append((x_start, y_start + 1))
            piece_points.append((x_start + 3, y_start + 1))
            piece_points.append((x_start +1, y_start + 2))
            piece_points.append((x_start + 3, y_start + 2))
            piece_points.append((x_start + 2, y_start + 3))

        if piece_name == "Ship":
            piece_points.append((x_start, y_start))
            piece_points.append((x_start + 1, y_start))
            piece_points.append((x_start, y_start - 1))
            piece_points.append((x_start + 2, y_start + 1))
            piece_points.append((x_start + 1, y_start + 2))
            piece_points.append((x_start + 2, y_start + 2))

        if piece_name == "Boat":
            piece_points.append((x_start + 1, y_start))
            piece_points.append((x_start, y_start + 1))
            piece_points.append((x_start + 2, y_start + 1))
            piece_points.append((x_start + 2, y_start + 1))
            piece_points.append((x_start + 1, y_start + 2))
            piece_points.append((x_start + 2, y_start + 2))

        if piece_name == "LWSS": # Light Weight Space Ship
            piece_points.append((x_start + 1, y_start))
            piece_points.append((x_start + 2, y_start ))
            piece_points.append((x_start + 3, y_start))
            piece_points.append((x_start, y_start + 1))
            piece_points.append((x_start + 3, y_start + 1))
            piece_points.append((x_start + 3, y_start + 2))
            piece_points.append((x_start + 3, y_start + 3))
            piece_points.append((x_start , y_start + 4))
            piece_points.append((x_start + 2, y_start + 4))

        return piece_points