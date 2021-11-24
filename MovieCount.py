from mrjob.job import MRJob
from mrjob.step import MRStep

class MoviesCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_movies,
                   reducer=self.reducer_count_movies)
        ]

    def mapper_get_movies(self, _, line):
        (userID, movieID, rating, timestamp) = line.split(",")
        yield movieID, 1

    def reducer_count_movies(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MoviesCount.run()
