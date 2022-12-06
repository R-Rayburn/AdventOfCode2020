file_name = 'test.txt'

with open(file_name, 'r') as f:
    data = [x.split('\n') for x in f.read().split('\n\n') if x]


class CameraTile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile
        self.neighbors = []
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def rotate(self):
        self.tile = list(zip(*self.tile[::-1]))

    def flip(self):
        self.tile = [x[::-1] for x in self.tile]

    def vertical_flip(self):
        self.tile = self.tile[::-1]


    def get_tile_edges(self):
        edges = [self.tile[0], self.tile[-1]]
        edges.append(''.join([r[0] for r in self.tile]))
        edges.append(''.join(r[-1] for r in self.tile))
        return edges

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __str__(self):
        return f'{self.id}\n' + '\n'.join(self.tile) + f'neighbors: {self.neighbors}'


camera_tiles = []
for d in data:
    id = int(''.join([x for x in d[0] if x.isdigit()]))
    tile = d[1:]
    camera_tiles.append(CameraTile(id, tile))


for i in range(len(camera_tiles)):
    for j in range(len(camera_tiles)):
        for edge in camera_tiles[i].get_tile_edges():
            if i != j and edge in camera_tiles[j].get_tile_edges() or edge[::-1] in camera_tiles[j].get_tile_edges():
                camera_tiles[i].add_neighbor(camera_tiles[j].id)

corner_product = 1
for tile in camera_tiles:
    if len(tile.neighbors) == 2:
        print(tile.id)
        corner_product *= tile.id
print(corner_product)


mapped_tiles = []


def map_neighbors(tile: CameraTile):
    mapped_tiles.append(tile.id)
    for neighbor_id in tile.neighbors:
        neighbor: CameraTile = [x for x in camera_tiles if x.id == neighbor_id][0]
        if neighbor.id not in mapped_tiles:
            grid = tile.tile
            if tile.top is None:
                # top = top
                if grid[0] == neighbor.tile[0]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.flip()
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id
                # top = bottom
                elif grid[0] == neighbor.tile[-1]:
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id
                # top = top flipped
                elif grid[0] == neighbor.tile[0][::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id
                # top = bottom flipped
                elif grid[0] == neighbor.tile[-1][::-1]:
                    neighbor.flip()
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id
                # top = left
                elif grid[0] == ''.join(r[0] for r in neighbor.tile):
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id
                # top = left flipped
                elif grid[0] == ''.join(r[0] for r in neighbor.tile)[::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.flip()
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id            
                # top = right
                elif grid[0] == ''.join(r[-1] for r in neighbor.tile):
                    neighbor.rotate()
                    neighbor.flip()
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id
                # top = right flipped
                elif grid[0] == ''.join(r[-1] for r in neighbor.tile)[::-1]:
                    neighbor.rotate()
                    tile.top = neighbor.id
                    neighbor.bottom = tile.id
                map_neighbors(neighbor)
            if tile.bottom is None:
                # bottom = top
                if grid[-1] == neighbor.tile[0]:
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id
                # bottom = bottom
                elif grid[-1] == neighbor.tile[-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.flip()
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id
                # bottom = top flipped
                elif grid[-1] == neighbor.tile[0][::-1]:
                    neighbor.flip()
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id
                # bottom = bottom flipped
                elif grid[-1] == neighbor.tile[-1][::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id
                # bottom = left
                elif grid[-1] == ''.join(r[0] for r in neighbor.tile):
                    neighbor.rotate()
                    neighbor.flip()
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id
                # bottom = left flipped
                elif grid[-1] == ''.join(r[0] for r in neighbor.tile)[::-1]:
                    neighbor.rotate()
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id            
                # bottom = right
                elif grid[-1] == ''.join(r[-1] for r in neighbor.tile):
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id
                # bottom = right flipped
                elif grid[-1] == ''.join(r[-1] for r in neighbor.tile)[::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.flip()
                    tile.bottom = neighbor.id
                    neighbor.top = tile.id
                map_neighbors(neighbor)
            if tile.left is None:
                tile_left_column = ''.join(r[0] for r in grid)
                # left = top
                if tile_left_column == neighbor.tile[0]:
                    neighbor.rotate()
                    tile.left = neighbor.id
                    neighbor.right = tile.id
                # left = bottom
                elif tile_left_column == neighbor.tile[-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.vertical_flip()
                    tile.left = neighbor.id
                    neighbor.right = tile.id
                # left = top flipped
                elif tile_left_column == neighbor.tile[0][::-1]:
                    neighbor.rotate()
                    neighbor.vertical_flip()
                    tile.left = neighbor.id
                    neighbor.right = tile.id
                # left = bottom flipped
                elif tile_left_column == neighbor.tile[-1][::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.left = neighbor.id
                    neighbor.right = tile.id
                # left = left
                elif tile_left_column == ''.join(r[0] for r in neighbor.tile):
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.vertical_flip()
                    tile.left = neighbor.id
                    neighbor.right = tile.id
                # left = left flipped
                elif tile_left_column == ''.join(r[0] for r in neighbor.tile)[::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.left = neighbor.id
                    neighbor.right = tile.id            
                # left = right
                elif tile_left_column == ''.join(r[-1] for r in neighbor.tile):
                    tile.left = neighbor.id
                    neighbor.right = tile.id
                # left = right flipped
                elif tile_left_column == ''.join(r[-1] for r in neighbor.tile)[::-1]:
                    neighbor.vertical_flip()
                    tile.left = neighbor.id
                    neighbor.right = tile.id
                map_neighbors(neighbor)
            if tile.right is None:
                tile_right_column = ''.join(r[-1] for r in grid)
                # right = top
                if tile_right_column == neighbor.tile[0]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.vertical_flip()
                    tile.right = neighbor.id
                    neighbor.left = tile.id
                # right = bottom
                elif tile_right_column == neighbor.tile[-1]:
                    neighbor.rotate()
                    tile.right = neighbor.id
                    neighbor.left = tile.id
                # right = top flipped
                elif tile_right_column == neighbor.tile[0][::-1]:
                    neighbor.rotate()
                    neighbor.vertical_flip()
                    tile.right = neighbor.id
                    neighbor.left = tile.id
                # right = bottom flipped
                elif tile_right_column == neighbor.tile[-1][::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.right = neighbor.id
                    neighbor.left = tile.id
                # right = left
                elif tile_right_column == ''.join(r[0] for r in neighbor.tile):
                    tile.right = neighbor.id
                    neighbor.left = tile.id
                # right = left flipped
                elif tile_right_column == ''.join(r[0] for r in neighbor.tile)[::-1]:
                    neighbor.vertical_flip()
                    tile.right = neighbor.id
                    neighbor.left = tile.id            
                # right = right
                elif tile_right_column == ''.join(r[-1] for r in neighbor.tile):
                    neighbor.rotate()
                    neighbor.rotate()
                    neighbor.vertical_flip()
                    tile.right = neighbor.id
                    neighbor.left = tile.id
                # right = right flipped
                elif tile_right_column == ''.join(r[-1] for r in neighbor.tile)[::-1]:
                    neighbor.rotate()
                    neighbor.rotate()
                    tile.right = neighbor.id
                    neighbor.left = tile.id
                map_neighbors(neighbor)
            mapped_tiles.append(neighbor.id)


for tile in camera_tiles:
    mapped_tiles = []
    map_neighbors(tile)
# mapped_tiles = []
# for tile in camera_tiles[::-1]:
#     map_neighbors(tile)
# map_neighbors(camera_tiles[0])


print([[x.top, x.right, x.bottom, x.left] for x in camera_tiles])
