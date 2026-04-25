import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
TOOLBAR_HEIGHT = 80

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Modes (tools)
MODE_BRUSH = "brush"
MODE_RECT = "rectangle"
MODE_CIRCLE = "circle"
MODE_ERASER = "eraser"
MODE_SQUARE = "square"
MODE_TRIANGLE_RIGHT = "triangle_right"
MODE_TRIANGLE_EQ = "triangle_eq"
MODE_RHOMBUS = "rhombus"

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint Program")
clock = pygame.time.Clock()

# Button class
class Button:
    def __init__(self, x, y, w, h, color, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 24)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)

        if self.text:
            txt = self.font.render(self.text, True, BLACK)
            surface.blit(txt, txt.get_rect(center=self.rect.center))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Main function
def main():
    # Canvas (drawing area)
    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - TOOLBAR_HEIGHT))
    canvas.fill(WHITE)

    drawing = False
    start_pos = None
    current_mode = MODE_BRUSH
    brush_size = 5
    color = BLACK

    # Buttons
    buttons = [
        Button(10, 10, 80, 30, GRAY, "Brush"),
        Button(100, 10, 80, 30, GRAY, "Rect"),
        Button(190, 10, 80, 30, GRAY, "Circle"),
        Button(280, 10, 80, 30, GRAY, "Eraser"),
        Button(370, 10, 80, 30, GRAY, "Clear"),
        Button(460, 10, 80, 30, GRAY, "Square"),
        Button(550, 10, 80, 30, GRAY, "Tri R"),
        Button(640, 10, 80, 30, GRAY, "Tri E"),
        Button(730, 10, 80, 30, GRAY, "Rhomb"),
    ]

    running = True
    while running:
        for event in pygame.event.get():

            # Exit
            if event.type == pygame.QUIT:
                running = False

            # Mouse pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Toolbar click
                if y < TOOLBAR_HEIGHT:
                    if buttons[0].is_clicked(event.pos):
                        current_mode = MODE_BRUSH
                    elif buttons[1].is_clicked(event.pos):
                        current_mode = MODE_RECT
                    elif buttons[2].is_clicked(event.pos):
                        current_mode = MODE_CIRCLE
                    elif buttons[3].is_clicked(event.pos):
                        current_mode = MODE_ERASER
                    elif buttons[4].is_clicked(event.pos):
                        canvas.fill(WHITE)
                    elif buttons[5].is_clicked(event.pos):
                        current_mode = MODE_SQUARE
                    elif buttons[6].is_clicked(event.pos):
                        current_mode = MODE_TRIANGLE_RIGHT
                    elif buttons[7].is_clicked(event.pos):
                        current_mode = MODE_TRIANGLE_EQ
                    elif buttons[8].is_clicked(event.pos):
                        current_mode = MODE_RHOMBUS
                else:
                    drawing = True
                    start_pos = (x, y - TOOLBAR_HEIGHT)

                    # Instant draw for brush/eraser
                    if current_mode == MODE_BRUSH:
                        pygame.draw.circle(canvas, color, start_pos, brush_size)
                    elif current_mode == MODE_ERASER:
                        pygame.draw.circle(canvas, WHITE, start_pos, brush_size)

            # Mouse move
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    x, y = event.pos
                    if y > TOOLBAR_HEIGHT:
                        pos = (x, y - TOOLBAR_HEIGHT)

                        # Continuous drawing
                        if current_mode == MODE_BRUSH:
                            pygame.draw.circle(canvas, color, pos, brush_size)
                        elif current_mode == MODE_ERASER:
                            pygame.draw.circle(canvas, WHITE, pos, brush_size)

            # Mouse released → draw shapes
            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    x, y = event.pos
                    if y > TOOLBAR_HEIGHT:
                        end_pos = (x, y - TOOLBAR_HEIGHT)

                        # Rectangle
                        if current_mode == MODE_RECT:
                            rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                            pygame.draw.rect(canvas, color, rect, 2)

                        # Circle
                        elif current_mode == MODE_CIRCLE:
                            radius = int(math.hypot(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                            pygame.draw.circle(canvas, color, start_pos, radius, 2)

                        # Square
                        elif current_mode == MODE_SQUARE:
                            side = min(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                            rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                            pygame.draw.rect(canvas, color, rect, 2)

                        # Right triangle
                        elif current_mode == MODE_TRIANGLE_RIGHT:
                            points = [
                                start_pos,
                                (end_pos[0], start_pos[1]),
                                (start_pos[0], end_pos[1])
                            ]
                            pygame.draw.polygon(canvas, color, points, 2)

                        # Equilateral triangle
                        elif current_mode == MODE_TRIANGLE_EQ:
                            x1, y1 = start_pos
                            x2, _ = end_pos
                            side = abs(x2 - x1)
                            height = int((math.sqrt(3)/2) * side)

                            points = [
                                (x1, y1),
                                (x1 + side, y1),
                                (x1 + side//2, y1 - height)
                            ]
                            pygame.draw.polygon(canvas, color, points, 2)

                        # Rhombus
                        elif current_mode == MODE_RHOMBUS:
                            x1, y1 = start_pos
                            x2, y2 = end_pos
                            cx = (x1 + x2) // 2
                            cy = (y1 + y2) // 2

                            points = [
                                (cx, y1),
                                (x2, cy),
                                (cx, y2),
                                (x1, cy)
                            ]
                            pygame.draw.polygon(canvas, color, points, 2)

                drawing = False
                start_pos = None

        # Draw UI
        screen.fill(GRAY)
        screen.blit(canvas, (0, TOOLBAR_HEIGHT))

        pygame.draw.rect(screen, (200, 200, 200), (0, 0, SCREEN_WIDTH, TOOLBAR_HEIGHT))

        # Draw buttons
        for b in buttons:
            b.draw(screen)

        # Show mode
        font = pygame.font.Font(None, 24)
        text = font.render(f"Mode: {current_mode}", True, BLACK)
        screen.blit(text, (10, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Run program
if __name__ == "__main__":
    main()