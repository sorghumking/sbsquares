# Generate a Super Bowl Squares 10x10 grid for an arbitrary number of players,
# filling leftover squares with 'rollover'. Save results as a CSV.

from itertools import product
from random import shuffle
from csv import writer

def generate_squares(players, team1, team2):
    # generate (row, col) coordinates for each square of 10x10 grid
    # i.e. (0,0),(0,1)...(0,9),(1,0),(1,1)...(1,9),(2,0),(2,1)...(9,8),(9,9)
    squares = list(product(range(10), range(10)))
    shuffle(squares) # shuffle coordinates
    shuffle(players) # shuffle players

    # report on whether numbers divide evenly
    sq_per = len(squares) // len(players) # squares per player
    extras = len(squares) % len(players) # leftover squares
    if extras > 0:
        print(f"{len(players)} doesn't divide {len(squares)} evenly, {extras} leftover squares.")
    else:
        print(f"{len(players)} divides {len(squares)} evenly, {sq_per} squares per player.")

    # assign each player sq_per squares
    sq_dict = {} # key: square, value: player. Will simplify writing to csv.
    for idx, p in enumerate(players):
        start = idx * sq_per
        end = start + sq_per
        player_squares = squares[start:end]
        for psq in player_squares:
            sq_dict[psq] = p
    # print(sq_dict)

    # assign remaining squares to rollover
    rollover_squares = squares[end:]
    if len(rollover_squares) > 0:
        for rsq in rollover_squares:
            sq_dict[rsq] = 'rollover'
        print(f"Rollover squares: {rollover_squares}")

    # confirm total number and uniqueness of squares
    assert len(sq_dict) == 100
    assert len(sq_dict.keys()) == len(set(sq_dict.keys()))

    # confirm that each player received sq_per unique squares
    for player in players:
        assert len([p for p in sq_dict.values() if p == player]) == sq_per

    # confirm player squares + rollover squares == 100
    assert len([p for p in sq_dict.values() if p == 'rollover']) + len(players) * sq_per == 100

    # for v in sorted(sq_dict.keys()):
        # print(f"{v}: {sq_dict[v]}")

    sorted_squares = sorted(sq_dict.keys())

    rows = []
    for ridx in range(10):
        new_row = [sq_dict[ssq] for ssq in sorted_squares[ridx*10:ridx*10+10]]
        assert len(new_row) == 10
        rows += [new_row]
        print(new_row)
    write_html(rows, "sbsquares.html")
    # write_csv(rows, "sbsquares2021.csv")

    # randomly assign teams to columns (x coordinates) or rows (y coordinates)
    teams = [team1, team2]
    shuffle(teams)
    col_team = teams[0]
    row_team = teams[1]
    print(f"Columns: {col_team}. Rows: {row_team}")

def write_csv(rows, filename):
    with open(filename, 'w') as csvfile:
        w = writer(csvfile)
        for r in rows:
            w.writerow(r)

def generate_html(rows):
    html = """<html><head>
        <script src="http://code.jquery.com/jquery-latest.min.js"></script>
        <script src="sbsquares.js"></script>
        <link rel="stylesheet" href="sbsquares.css">
        </head>
        <body>
        <table>
    """
    # score digit header row
    html += "<tr><td class='corner'></td>"
    for x in range(10):
        html += f"<td class='digit'>{x}</td>"
    html += "</tr>\n"

    for idx, row in enumerate(rows):
        html += f"  <tr><td class='digit'>{idx}</td>\n"
        for player in row:
            html += f"    <td class='player'>{player}</td>\n"
        html += "  </tr>\n"
    html += "</table></body></html>"
    return html

def write_html(rows, filename):
    with open(filename, 'w') as htmlfile:
        htmlfile.write(generate_html(rows))


if __name__ == "__main__":
    players = [f"P{n+1}" for n in range(25)] # replace with list of player names
    generate_squares(players, "Team 1", "Team 2")
