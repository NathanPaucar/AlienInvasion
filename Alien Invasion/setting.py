class Settings:
    
    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800

        # Alien settings
        self.alien_speed = .5
        self.fleet_drop_speed = 20
        # Fleet_direction of 1 represents right; -1 respresents left.
        self.fleet_direction = 1

        self.bg_color = (230, 230, 230)
        #bullets settings
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 3
        # add a speed
        self.ship_speed = 1.5
        self.ship_limit = 3

