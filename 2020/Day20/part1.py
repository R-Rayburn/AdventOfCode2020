
with open('data.txt', 'r') as f:
    data = [x.split('\n') for x in f.read().split('\n\n') if x]


class CameraTile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile
        self.neighbors = []

    def get_tile_edges(self):
        edges = [self.tile[0], self.tile[-1]]
        edges.append(''.join([r[0] for r in self.tile]))
        edges.append(''.join(r[-1] for r in self.tile))
        return edges

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


camera_tiles = []
for d in data:
    id = int(''.join([x for x in d[0] if x.isdigit()]))
    tile = d[1:]
    camera_tiles.append(CameraTile(id, tile))


for i in range(len(camera_tiles)):
    for j in range(len(camera_tiles)):
        for edge in camera_tiles[i].get_tile_edges():
            print(edge)
            if i != j and edge in camera_tiles[j].get_tile_edges() or edge[::-1] in camera_tiles[j].get_tile_edges():
                camera_tiles[i].add_neighbor(camera_tiles[j].id)

corner_product = 1
for tile in camera_tiles:
    if len(tile.neighbors) == 2:
        corner_product *= tile.id
print(corner_product)
