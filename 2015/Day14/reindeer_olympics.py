from operator import attrgetter

with open('data.txt', 'r') as file:
    reindeer_data = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    reindeer_test = test_file.read().split('\n')

class Reindeer:
    def __init__(self, name, km_per_s, duration, rest_time):
        self.name = name
        self.km_per_s = km_per_s
        self.duration = duration
        self.rest_time = rest_time
        self.current_duration = duration
        self.current_rest_time = 0
        self.current_distance_traveled = 0
        self.points = 0

    def race(self):
        if self.current_duration > 0:
            self.current_duration -= 1
            self.current_distance_traveled += self.km_per_s
            if self.current_duration == 0:
                self.current_rest_time = self.rest_time
        elif self.current_rest_time > 0:
            self.current_rest_time -= 1
            if self.current_rest_time == 0:
                self.current_duration = self.duration

    def give_point(self):
        self.points += 1
    
    def __str__(self) -> str:
        return f'{self.name} has traveled {self.current_distance_traveled} and received {self.points} points'


def format_data(reindeers):
    formatted_data = []
    for reindeer in reindeers:
        name, _, _, km_per_s, _, _, duration, *_, rest_time, _ = reindeer.split(' ')
        formatted_data.append(Reindeer(
            name,
            int(km_per_s),
            int(duration),
            int(rest_time),
        ))
    return formatted_data


def race(data, race_duration, calc_point=False):
    reindeers = format_data(data)
    for _ in range(race_duration):
        for reindeer in reindeers:
            reindeer.race()
        if calc_point:
            first_place_value = max(reindeers, key=attrgetter('current_distance_traveled')).current_distance_traveled
            first_place_reindeers = [i for i, v in enumerate(reindeers) if v.current_distance_traveled == first_place_value]
            for reindeer_i in first_place_reindeers:
                reindeers[reindeer_i].give_point()
    winner_calc = 'points' if calc_point else 'current_distance_traveled'
    winner = max(reindeers, key=attrgetter(winner_calc))
    return winner

print('Part 1')
print(f'Test: {race(reindeer_test, 1000)}')
print(f'Data: {race(reindeer_data, 2503)}')

print('Part 2')
print(f'Test: {race(reindeer_test, 1000, True)}')
print(f'Data: {race(reindeer_data, 2503, True)}')
