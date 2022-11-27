import pygame
import random as rand

pygame.init()

#constants
WIDTH, HEIGHT = 900, 600
FPS = 60
ROWS, COLS = 30, 30
SQUARE_SIZE = HEIGHT // ROWS

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (4, 130, 219)
TILE_LIGHT_GREEN = (0, 214, 57)
TILE_DARK_GREEN = (0, 189, 50)

#global variables

FPS_SPEED = 15

#maps

wall_1 = ([(i, 4) for i in range (5, 26, 1)] + [(i, 5) for i in range (5, 26, 1)] + [(i, 6) for i in range (5, 26, 1)] + [(i, 7) for i in range (5, 26, 1)] 
+ [(i, 25) for i in range (5, 26, 1)] + [(i, 24) for i in range (5, 26, 1)] + [(i, 23) for i in range (5, 26, 1)] + [(i, 22) for i in range (5, 26, 1)])

wall_2 = ([(4, i) for i in range (5, 26, 1)] + [(5, i) for i in range (5, 26, 1)] + [(6, i) for i in range (5, 26, 1)] + [(7, i) for i in range (5, 26, 1)] 
+ [(25, i) for i in range (5, 26, 1)] + [(24, i) for i in range (5, 26, 1)] + [(23, i) for i in range (5, 26, 1)] + [(22, i) for i in range (5, 26, 1)])

wall_3 = ([(i, j) for i in range(0, 7, 1) for j in range (6-i, -1, -1)] + [(i, 29 - j) for i in range(0, 7, 1) for j in range (6-i, -1, -1)] 
+ [(29 - i, j) for i in range(0, 7, 1) for j in range (6-i, -1, -1)]  + [(29 - i, 29 - j) for i in range(0, 7, 1) for j in range (6-i, -1, -1)])

wall_4 = ([(4 + i + j, j - 8) for i in range (4) for j in range (10, 21, 1)] + [(-8 + i + j, j + 7) for i in range (4) for j in range (10, 21, 1)])

walls = [wall_1, wall_2, wall_3, wall_4]

#classes

#Class Board

class Board:
    def __init__(self):
        self.board = []
    def draw_board(self, screen, walls, x_change = 0):
        img = pygame.transform.scale(pygame.image.load("./Graphics/grass.png"), (SQUARE_SIZE, SQUARE_SIZE))
        img2 = pygame.transform.scale(pygame.image.load("./Graphics/grass2.png"), (SQUARE_SIZE, SQUARE_SIZE))
        img_wall = pygame.transform.scale(pygame.image.load("./Graphics/wall.png"), (SQUARE_SIZE, SQUARE_SIZE))
        screen.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                if ((row, col) in walls):
                    screen.blit(img_wall, (x_change + row * SQUARE_SIZE, col * SQUARE_SIZE))
                else:
                    screen.blit(img, (x_change + row * SQUARE_SIZE, col * SQUARE_SIZE))

            for col in range((row+1) % 2, ROWS, 2):
                if ((row, col) in walls):
                    screen.blit( img_wall, (x_change + row * SQUARE_SIZE, col * SQUARE_SIZE))
                else:
                    screen.blit(img2, (x_change + row * SQUARE_SIZE, col * SQUARE_SIZE))
    def draw_snake(self, screen, snake, boost):
        rep = 'Snake'
        if (boost.boost_active):
            rep = 'Super_Snake'
        self.print_head(screen, snake.head, rep)
        self.print_body(screen, snake.body, snake.head[1], snake.tail[1], rep)
        self.print_tail(screen, snake.tail, rep)
    
    def print_head(self,screen, head, rep):
        if (head[0] == 'up'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/head_up.png"), (SQUARE_SIZE, SQUARE_SIZE)), (head[1][0] * SQUARE_SIZE, head[1][1] * SQUARE_SIZE))
        elif(head[0] == 'down'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/head_down.png"), (SQUARE_SIZE, SQUARE_SIZE)), (head[1][0] * SQUARE_SIZE, head[1][1] * SQUARE_SIZE))
        elif(head[0] == 'left'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/head_left.png"), (SQUARE_SIZE, SQUARE_SIZE)), (head[1][0] * SQUARE_SIZE, head[1][1] * SQUARE_SIZE))
        elif(head[0] == 'right'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/head_right.png"), (SQUARE_SIZE, SQUARE_SIZE)), (head[1][0] * SQUARE_SIZE, head[1][1] * SQUARE_SIZE))
    
    def print_body(self, screen, body, head, tail, rep):
        whole_body = []
        whole_body.append(head)
        for i in body:
            whole_body.append(i)
        whole_body.append(tail)

        for i in range(1, len(whole_body) - 1, 1):
            answer = self.helper(whole_body[i-1], whole_body[i], whole_body[i+1])
            if (answer == 'horizontal'):
                screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/body_horizontal.png"), (SQUARE_SIZE, SQUARE_SIZE)), (whole_body[i][0] * SQUARE_SIZE, whole_body[i][1] * SQUARE_SIZE))
            elif (answer == 'vertical'):
                screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/body_vertical.png"), (SQUARE_SIZE, SQUARE_SIZE)), (whole_body[i][0] * SQUARE_SIZE, whole_body[i][1] * SQUARE_SIZE))
            elif (answer == 'left-up'):
                screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/body_topleft.png"), (SQUARE_SIZE, SQUARE_SIZE)), (whole_body[i][0] * SQUARE_SIZE, whole_body[i][1] * SQUARE_SIZE))
            elif (answer == 'right-up'):
                screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/body_topright.png"), (SQUARE_SIZE, SQUARE_SIZE)), (whole_body[i][0] * SQUARE_SIZE, whole_body[i][1] * SQUARE_SIZE))
            elif (answer == 'left-down'):
                screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/body_bottomleft.png"), (SQUARE_SIZE, SQUARE_SIZE)), (whole_body[i][0] * SQUARE_SIZE, whole_body[i][1] * SQUARE_SIZE))
            elif (answer == 'right-down'):
                screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/body_bottomright.png"), (SQUARE_SIZE, SQUARE_SIZE)), (whole_body[i][0] * SQUARE_SIZE, whole_body[i][1] * SQUARE_SIZE))
    
    def print_tail(self, screen, tail, rep):
        if (tail[0] == 'up'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/tail_up.png"), (SQUARE_SIZE, SQUARE_SIZE)), (tail[1][0] * SQUARE_SIZE, tail[1][1] * SQUARE_SIZE))
        elif(tail[0] == 'down'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/tail_down.png"), (SQUARE_SIZE, SQUARE_SIZE)), (tail[1][0] * SQUARE_SIZE, tail[1][1] * SQUARE_SIZE))
        elif(tail[0] == 'left'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/tail_left.png"), (SQUARE_SIZE, SQUARE_SIZE)), (tail[1][0] * SQUARE_SIZE, tail[1][1] * SQUARE_SIZE))
        elif(tail[0] == 'right'):
            screen.blit(pygame.transform.scale(pygame.image.load(f"./Graphics/{rep}/tail_right.png"), (SQUARE_SIZE, SQUARE_SIZE)), (tail[1][0] * SQUARE_SIZE, tail[1][1] * SQUARE_SIZE))
    
    def draw_apple_boosts(self, screen, apple, boost):
        screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/apple.png"), (SQUARE_SIZE, SQUARE_SIZE)), (apple.position[0] * SQUARE_SIZE, apple.position[1] * SQUARE_SIZE))
        screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/boost.png"), (SQUARE_SIZE, SQUARE_SIZE)), (boost.position[0] * SQUARE_SIZE, boost.position[1] * SQUARE_SIZE))

    def draw_stats(self, screen, stats, boost):
        space = 10
        
        #result 
        font = pygame.font.SysFont("rasa", 40)

        text = font.render("Wynik", True, BLUE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))
        space += text.get_height()

        font = pygame.font.SysFont("rasa", 30)
        text = font.render(f"{int(stats.score)}", True, WHITE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))

        space += 10 + text.get_height()

        #game time
        font = pygame.font.SysFont("rasa", 40)
        
        text = font.render("Czas gry", True, BLUE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))
        space += text.get_height()
        
        font = pygame.font.SysFont("rasa", 30)
        text = font.render(f"{self.game_time(stats.game_time)}", True, WHITE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))
        
        space += 10 + text.get_height()

        #combo 
        font = pygame.font.SysFont("rasa", 30)

        text = font.render("Obecny mnożnik", True, BLUE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))

        text = font.render("punktów", True, BLUE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space + text.get_height() - 5))
        space += 2 * text.get_height()

        font = pygame.font.SysFont("rasa", 30)
        text = font.render(f"{stats.combo:.2}x", True, WHITE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))

        space += 10 + text.get_height()

        #apple collected
        font = pygame.font.SysFont("rasa", 40)

        text = font.render("Zebrane jabłka", True, BLUE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))
        space += text.get_height()

        font = pygame.font.SysFont("rasa", 30)
        text = font.render(f"{stats.apple_eaten}", True, WHITE)
        screen.blit(text, (600 + 150 - text.get_width() / 2, space))

        space += 10 + text.get_height()

        #boosts
        if(boost.boost_active):
            font = pygame.font.SysFont("rasa", 30)

            text = font.render("Pozostały czas działania", True, BLUE)
            screen.blit(text, (600 + 150 - text.get_width() / 2, space))

            text = font.render("złotego jabłka:", True, BLUE)
            screen.blit(text, (600 + 150 - text.get_width() / 2, space + text.get_height() - 5))
            space += -10 + 2 * text.get_height()

            font = pygame.font.SysFont("rasa", 30)
            text = font.render(f"{self.boost_time(boost.boost_time)}", True, WHITE)
            screen.blit(text, (600 + 150 - text.get_width() / 2, space))

            space += 10 + text.get_height()

        elif(not boost.boost_active):
            if (boost.boost_time > 0):
                font = pygame.font.SysFont("rasa", 30)

                text = font.render("Pozostały czas złotego:", True, BLUE)
                screen.blit(text, (600 + 150 - text.get_width() / 2, space))

                text = font.render("jabłka na planszy:", True, BLUE)
                screen.blit(text, (600 + 150 - text.get_width() / 2, space + text.get_height() - 5))
                space += -10 + 2 * text.get_height()

                font = pygame.font.SysFont("rasa", 30)
                text = font.render(f"{self.boost_time(boost.boost_time)}", True, WHITE)
                screen.blit(text, (600 + 150 - text.get_width() / 2, space))

                space += 10 + text.get_height()
            else:
                font = pygame.font.SysFont("rasa", 30)

                text = font.render("Czas do pojawienia się", True, BLUE)
                screen.blit(text, (600 + 150 - text.get_width() / 2, space))

                text = font.render("złotego jabłka:", True, BLUE)
                screen.blit(text, (600 + 150 - text.get_width() / 2, space + text.get_height() - 5))
                space += -10 + 2 * text.get_height()

                font = pygame.font.SysFont("rasa", 30)
                text = font.render(f"{self.boost_time(boost.boost_next_time)}", True, WHITE)
                screen.blit(text, (600 + 150 - text.get_width() / 2, space))

                space += 10 + text.get_height()
        

    def game_time(self, time):
        hours = int(time // 3600)
        time = time % 3600
        minutes = int(time // 60)
        time = time % 60
        seconds = int(time)
        if (minutes < 10 and time < 10):
            return f"{hours}:0{minutes}:0{seconds}"
        elif (minutes < 10):
            return f"{hours}:0{minutes}:{seconds}"
        elif (time < 10):
            return f"{hours}:{minutes}:0{seconds}"
        return f"{hours}:{minutes}:{seconds}"

    def boost_time(self, time):
        minutes = int(time // 60)
        time = time % 60
        seconds = int(time)
        if (minutes < 10 and time < 10):
            return f"0{minutes}:0{seconds}"
        elif (minutes < 10):
            return f"0{minutes}:{seconds}"
        elif (time < 10):
            return f"{minutes}:0{seconds}"
        return f"{minutes}:{seconds}"

    def helper(self, pos1, pos2, pos3):
        x_axis1 = pos1[0] - pos2[0] 
        x_axis2 = pos2[0] - pos3[0]
        y_axis1 = pos1[1] - pos2[1]
        y_axis2 = pos2[1] - pos3[1]

        if (x_axis1 == x_axis2 == 0):
            return 'vertical'
        elif(y_axis1 == y_axis2 == 0):
            return 'horizontal'
        elif((x_axis1 == 0 and y_axis1 == -1 and x_axis2 == 1 and y_axis2 == 0) or (x_axis1 == -1 and y_axis1 == 0 and x_axis2 == 0 and y_axis2 == 1)):
            return 'left-up'
        elif((x_axis1 == 0 and y_axis1 == -1 and x_axis2 == -1 and y_axis2 == 0) or (x_axis1 == 1 and y_axis1 == 0 and x_axis2 == 0 and y_axis2 == 1)):
            return 'right-up'
        elif((x_axis1 == 0 and y_axis1 == 1 and x_axis2 == 1 and y_axis2 == 0) or (x_axis1 == -1 and y_axis1 == 0 and x_axis2 == 0 and y_axis2 == -1)):
            return 'left-down'
        elif((x_axis1 == 1 and y_axis1 == 0 and x_axis2 == 0 and y_axis2 == -1) or (x_axis1 == 0 and y_axis1 == 1 and x_axis2 == -1 and y_axis2 == 0)):
            return 'right-down'

#Class Statistics

class Statistics:
    def __init__(self):
        self.game_time = 0.0
        self.apple_eaten = 0
        self.score = 0
        self.combo = 1.0
        self.combo_time = 30.0
    
    def apple_collected(self, boost):
        self.apple_eaten += 1
        if (boost.boost_active):
            self.score += 100.0 * self.combo * 2.0
        else:
            self.score += 100.0 * self.combo
        self.combo_time = 30.0
        self.combo += 0.1

    def reset_combo(self):
        self.combo = 1.0
        self.combo_time = 30.0
    
    def increase_game_time(self, time):
        self.game_time += time
    
    def decrease_combo_time(self, time):
        self.combo_time -= time
        if (self.combo_time == 0):
            self.reset_combo()

#Class Snake

class Snake:
    def __init__(self, wall):
        self.head = ['down', (15, 15)]
        self.body = []
        self.tail = ['up', (15, 14)]
        self.direction = self.head[0]
        self.wall = wall
    def whole_body(self):
        whole_body = []
        whole_body.append(self.head[1])
        for i in self.body:
            whole_body.append(i)
        whole_body.append(self.tail[1])
        return whole_body
    def turn_up(self):
        if self.direction != 'up' and self.direction != 'down':
            self.direction = 'up'
    
    def turn_down(self):
        if self.direction != 'up' and self.direction != 'down':
            self.direction = 'down'
    
    def turn_left(self):
        if self.direction != 'left' and self.direction != 'right':
            self.direction = 'left'
    
    def turn_right(self):
        if self.direction != 'left' and self.direction != 'right':
            self.direction = 'right'
    
    def move(self):

        #position of head and tail
        head = list(self.head[1])

        #change snake head position
        if self.direction == 'up':
            head[1] -= 1
            self.head[0] = 'up'
        elif self.direction == 'down':
            head[1] += 1
            self.head[0] = 'down'
        elif self.direction == 'left':
            head[0] -= 1
            self.head[0] = 'left'
        elif self.direction == 'right':
            head[0] += 1
            self.head[0] = 'right'
        
        # change snake body & save changes
        self.body.insert(0, self.head[1])
        self.tail[1] = self.body.pop()
        self.head[1] = tuple(head)
        
        #whole_body
        whole_body = self.whole_body()
        
        #change snake tail
        x_axis = whole_body[-1][0] - whole_body[-2][0]
        y_axis = whole_body[-1][1] - whole_body[-2][1]

        if x_axis == -1:
            self.tail[0] = 'left'
        elif x_axis == 1:
            self.tail[0] = 'right'
        elif y_axis == -1:
            self.tail[0] = 'up'
        elif y_axis == 1:
            self.tail[0] = 'down'
    
    def collision(self):
        if self.head[1][0] < 0 or self.head[1][0] >= ROWS:
            return True
        elif self.head[1][1] < 0 or self.head[1][1] >= ROWS:
            return True
        elif self.head[1] in self.whole_body()[1:]:
            return True
        elif self.head[1] in self.wall:
            return True
        return False
    
    def grow(self, apple, boost, stats):
        if (apple.position == self.head[1]):
            head = list(self.head[1])

            if self.direction == 'up':
                head[1] -= 1
                self.head[0] = 'up'
            elif self.direction == 'down':
                head[1] += 1
                self.head[0] = 'down'
            elif self.direction == 'left':
                head[0] -= 1
                self.head[0] = 'left'
            elif self.direction == 'right':
                head[0] += 1
                self.head[0] = 'right'
            self.body.insert(0, self.head[1])
            self.head[1] = tuple(head)
            apple.generate_new(self)
            stats.apple_collected(boost)
            pygame.mixer.Channel(1).set_volume(0.2)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('./Music/eat.mp3'))
            return True
        elif(boost.position == self.head[1]):
            boost.collected()
        return False

#Class Apple

class Apple:
    def __init__(self, snake, wall):
        self.wall = wall
        self.generate_new(snake)

    def generate_new(self, snake):
        generated = (rand.randint(0, ROWS - 1), rand.randint(0, ROWS - 1))
        while generated in snake.whole_body() or generated in self.wall:
            generated = (rand.randint(0, ROWS - 1), rand.randint(0, ROWS - 1))
        self.position = generated

#Class Boost

class Boost:
    def __init__(self, snake, apple, wall):
        self.position = (-10, -10)
        self.boost_active = False
        self.boost_time = 0.0
        self.boost_next_time = 181
        self.snake = snake
        self.apple = apple
        self.wall = wall
    
    def generate_new(self, snake, apple):
        generated = (rand.randint(0, ROWS - 1), rand.randint(0, ROWS - 1))
        while generated in snake.whole_body() or generated == apple.position or generated in self.wall:
            generated = (rand.randint(0, ROWS - 1), rand.randint(0, ROWS - 1))
        self.position = generated
        self.boost_ready = True
        pygame.mixer.music.load('./Music/Boost_on_map.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
    
    def collected(self):
        pygame.mixer.music.load('./Music/Boost_active.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.position = (-10, -10)
        self.boost_active = True
        self.boost_time = 60.0

    def decrease_boost_time(self, time):
        if(self.boost_active):
            self.boost_time -= time
            if (self.boost_time == 0):
                self.boost_active = False
                self.boost_next_time = 180.0
                pygame.mixer.music.load('./Music/Game_music.wav')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
            if (self.boost_time < 0.0):
                self.boost_time = 0.0
        else:
            self.boost_next_time -= time
            self.boost_time -= time
            if(self.boost_next_time == 0):
                self.boost_time = 30.0
                self.generate_new(self.snake, self.apple)
            elif(self.boost_time == 0):
                self.boost_next_time = 180.0
                self.position = (-10,-10)

       

    

# help functions
def menu_style(screen, start_x, start_y):
    pygame.draw.rect(screen, BLUE, (start_x, start_y, 500, 100))
    pygame.draw.rect(screen, BLACK, (start_x + 5, start_y + 5, 490, 90))

# main game functions
def main_menu(screen):
    pygame.mixer.music.stop()
    menu_run = True
    clock = pygame.time.Clock()
    pygame.mixer.music.load('./Music/technological_menace.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    curr_opt = 0
    mv = 'None'

    while menu_run:
        mv = 'None'
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    curr_opt = (curr_opt - 1) % 3
                elif event.key == pygame.K_DOWN:
                    curr_opt = (curr_opt + 1) % 3
                elif event.key == pygame.K_RETURN:
                    if (curr_opt == 0):
                        game(screen)
                    elif (curr_opt == 1):
                        choose_map(screen)
                    elif (curr_opt == 2):
                        exit()
        screen.fill(BLACK)
        if(curr_opt == 0):
            menu_style(screen, 200, 280)
        elif(curr_opt == 1):
            menu_style(screen, 200, 380)
        elif(curr_opt == 2):
            menu_style(screen, 200, 480)

        screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/SnakeMenu.png"), (600, 200)), (150,20))
        font = pygame.font.SysFont("rasa", 40)
        text = font.render("Rozpocznij grę", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 300))
        text = font.render("Niestandardowe plansze", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 400))
        text = font.render("Wyjdź", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 500))
        pygame.display.flip()
    

def choose_map(screen):
    choose_run = True
    clock = pygame.time.Clock()
    board = Board()
    global walls
    curr_opt = 0
    curr_fps = 15
    mv = 'None'
    while choose_run:
        mv = 'None'
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if curr_opt != 0:
                        curr_opt -= 1
                elif event.key == pygame.K_RIGHT:
                    if curr_opt != len(walls) - 1:
                        curr_opt += 1
                elif event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_RETURN:
                    game(screen, walls[curr_opt])

        screen.fill(BLACK)
        board.draw_board(screen, walls[curr_opt], 150)
        if curr_opt != 0:
            screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/key_arrow_left.png"), (70, 70)), (40, 265))
        if curr_opt != len(walls) - 1:
            screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/key_arrow_right.png"), (70, 70)), (800, 265))
        screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/ESC.png"), (70, 70)), (40, 50))
        font = pygame.font.SysFont("rasa", 30)
        text = font.render("Powrót", True, WHITE)
        screen.blit(text, (33, 3))
        screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/Enter.png"), (150, 75)), (750, 450))
        text = font.render("Zatwierdź", True, WHITE)
        screen.blit(text, (768, 535))
        pygame.display.flip()

    


def game(screen, walls = []):
    pygame.mixer.music.load('./Music/Game_music.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    run = True
    clock = pygame.time.Clock() 
    board = Board()
    snake = Snake(walls)
    apple = Apple(snake, walls)
    boost = Boost(snake, apple, walls)
    stats = Statistics()
    

    board.draw_board(screen, walls)
    board.draw_apple_boosts(screen, apple, boost)
    board.draw_snake(screen, snake, boost)
    board.draw_stats(screen, stats, boost)
    pygame.display.flip()
    turned = False
    while run:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and turned == False:
                if event.key == pygame.K_UP:
                    snake.turn_up()
                    turned = True
                elif event.key == pygame.K_DOWN:
                    snake.turn_down()
                    turned = True
                elif event.key == pygame.K_LEFT:
                    snake.turn_left()
                    turned = True
                elif event.key == pygame.K_RIGHT:
                    snake.turn_right()
                    turned = True
                elif event.key == pygame.K_ESCAPE:
                    pause(screen)
                    pygame.mixer.music.load('./Music/Game_music.wav')
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(-1)

        if(not snake.grow(apple, boost, stats)):
            snake.move()
            turned = False
        if snake.collision():
            game_over(screen, stats)
        board.draw_board(screen, walls)
        board.draw_apple_boosts(screen, apple, boost)
        board.draw_snake(screen, snake, boost)
        board.draw_stats(screen, stats, boost)

        boost.decrease_boost_time(0.2)
        stats.increase_game_time(0.2)
        
        pygame.display.flip()

def pause(screen):
    pygame.mixer.music.load('./Music/Pause_music.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    pause_run = True
    clock = pygame.time.Clock()
    curr_fps = 15
    curr_opt = 0
    mv = 'None'
    while pause_run:
        mv = 'None'
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    curr_opt = (curr_opt - 1) % 2
                elif event.key == pygame.K_DOWN:
                    curr_opt = (curr_opt + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if (curr_opt == 0):
                        return
                    elif (curr_opt == 1):
                        main_menu(screen)

        screen.fill(BLACK)
        if(curr_opt == 0):
            menu_style(screen, 200, 380)
        elif(curr_opt == 1):
            menu_style(screen, 200, 480)
        
        screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/snake_pause.png"), (250, 250)), (325,20))
        font = pygame.font.SysFont("rasa", 40)
        text = font.render("Wznów grę", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 400))
        text = font.render("Wróć do menu głównego", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 500))
        curr_fps += 1
        pygame.display.flip()
    

def game_over(screen, stats):
    pygame.mixer.music.load('./Music/Death_music.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    pause_run = True
    clock = pygame.time.Clock()

    curr_opt = 0
    while pause_run:
        mv = 'None'
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    curr_opt = (curr_opt - 1) % 2
                elif event.key == pygame.K_DOWN:
                    curr_opt = (curr_opt + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if curr_opt == 0:
                        main_menu(screen)
                    else:
                        exit()


        screen.fill(BLACK)
        if(curr_opt == 0):
            menu_style(screen, 200, 380)
        elif(curr_opt == 1):
            menu_style(screen, 200, 480)
        
        screen.blit(pygame.transform.scale(pygame.image.load("./Graphics/snake_death.png"), (250, 250)), (325,20))
        font = pygame.font.SysFont("rasa", 40)
        text = font.render(f"Wynik: {int(stats.score)}", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 300))
        text = font.render("Wróć do menu głównego", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 400))
        text = font.render("Zakończ grę", True, WHITE)
        screen.blit(text, ((450 - (text.get_width() / 2)), 500))
        pygame.display.flip()


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    main_menu(screen)

main()
