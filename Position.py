from dataclasses import dataclass

# dataclass automatycznie generuje __init__ oraz nadpisuje działanie __eq__ (Equals) oraz __hash__,
# dzięki czemu można porównywać dwie pozycje po ich wartościach, a nie referencji
@dataclass(frozen=True)
class Position:
    x: int
    y: int

    # zwraca cztery sąsiednie pola
    def neighbors(self):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # północ / wschód / południe / zachód
        positions = []

        for dx, dy in directions:
            positions.append(Position(self.x + dx, self.y + dy))

        return positions