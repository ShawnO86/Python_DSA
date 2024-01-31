#7.13
class Artist:
    def __init__(self, name = 'unknown', birth = -1, death = -1):
        self.name = name
        self.birth_date = birth
        self.death_date = death
    
    def print_info(self):
        output = f'Artist: {self.name} '
        if self.death_date < 0 and self.birth_date > 0:
            output += f'({self.birth_date} to present)'
        elif self.death_date > 0 and self.birth_date > 0:
            output += f'({self.birth_date} to {self.death_date})'
        print(output)
        

"""       
class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)

    # TODO: Define print_info() method
 """

if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    #new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    user_artist.print_info()
