ball_y = 100
y_speed = 4
x_speed = 4
ball_x = 100
ball2_y = 350
ball2_x = 350
y2_speed = 4
x2_speed = 4
def setup():
    size(500, 500)
    
def draw():
    global ball_y
    global y_speed
    global x_speed
    global ball_x
    global ball2_x
    global ball2_y
    global y2_speed
    global x2_speed
    background(255, 222, 249)
    fill(222, 245, 255)
    ellipse(ball_x, ball_y, 100, 100)
    ellipse(ball2_x, ball2_y, 100, 100)
    line(0, 400, 500, 400)
    
    if ball_y > 350:
        print("BOUNCE")
        y_speed = -y_speed
    
    if ball_y < 50:
        print("bounceback")
        y_speed = 4
    
    if ball_x < 50:
        x_speed = 4
    
    if ball_x > 450:
        x_speed = -x_speed
        
    if ball2_y > 350:
        print("BOUNCE")
        y2_speed = -y_speed
    
    if ball2_y < 50:
        print("bounceback")
        y2_speed = 4
    
    if ball2_x < 50:
        x2_speed = 3
    
    if ball2_x > 450:
        x2_speed = -x_speed
    
    
        
        
        
    ball2_x = ball2_x + x2_speed
    ball2_y = ball2_y + y2_speed    
    ball_x = ball_x + x_speed
    ball_y = ball_y + y_speed
