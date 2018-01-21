ball_size = 70
CPTballsize = 40
player_ballx = 0
player_bally = 0
CPT_ball1x = 0
CPT_ball1y = 0
CPT_ball2x = 0
CPT_ball2y = 0
CPT_ball3x = 0
CPT_ball3y = 0
CPT_ball4x = 0
CPT_ball4y = 0
score = 0
location = 0
screen = "menu"
hit = 0


def setup():
    size(1000, 600)


def draw():
    global hit
    global screen
    global score
    global location
    global player_ballx
    global player_bally
    global CPT_ball1x
    global CPT_ball1y
    global CPT_ball2x
    global CPT_ball2y
    global CPT_ball3x
    global CPT_ball3y
    global CPT_ball4x
    global CPT_ball4y
    background(0)

    if screen == "menu":
        if keyPressed:
            if key == "s":
                screen = "game"
        background(0)
        fill(255)
        textSize(100)
        text("WELCOME", width/4, height/2)
        textSize(25)
        text("press [s] to start", width/4, height/2 + 290)
        textSize(30)
        fill(0, 255, 0)
        text("Click red ball to get score. if score is 5, you win", 150, 30)
        text("If other balls hit the red ball youre score will reset", 150, 60)
    elif screen == "game":
        if keyPressed:
            if key == "r":
                screen = "menu"

        if score < 5:
            textSize(30)
            fill(255, 0, 0)
            text("Score: " + str(score), 10, 30)

            textSize(25)
            fill(255)
            text("press [r] to restart", 150, 30)

            # player ball
            location = location + 0.01
            player_ballx = noise(location)
            player_ballx = map(player_ballx, 0, 1, 0, width)
            player_bally = noise(location + 1)
            player_bally = map(player_bally, 0, 1, 0, width)
            maxXvaluepball = constrain(player_ballx, 0, 1000)
            minYvaluepball = constrain(player_bally, 0, 600)
            noStroke()
            fill(255, 0, 0)
            ellipse(maxXvaluepball, minYvaluepball, ball_size, ball_size)

            # CPT ball 1
            CPT_ball1x = noise(location + 20)
            CPT_ball1x = map(CPT_ball1x, 0, 1, 0, width)
            CPT_ball1y = noise(location + 50)
            CPT_ball1y = map(CPT_ball1y, 0, 1, 0, width)
            maxXvalCPTball1 = constrain(CPT_ball1x, 0, 1000)
            minYvalCPTball1 = constrain(CPT_ball1y, 0, 600)
            fill(0, 255, 0)
            ellipse(maxXvalCPTball1, minYvalCPTball1, CPTballsize, CPTballsize)

            # CPT ball 2
            CPT_ball2x = noise(location + 40)
            CPT_ball2x = map(CPT_ball2x, 0, 1, 0, width)
            CPT_ball2y = noise(location + 100)
            CPT_ball2y = map(CPT_ball2y, 0, 1, 0, width)
            maxXvalCPTball2 = constrain(CPT_ball2x, 0, 1000)
            minYvalCPTball2 = constrain(CPT_ball2y, 0, 600)
            fill(0, 0, 255)
            ellipse(maxXvalCPTball2, minYvalCPTball2, CPTballsize, CPTballsize)

            # CPT ball 3
            CPT_ball3x = noise(location + 60)
            CPT_ball3x = map(CPT_ball3x, 0, 1, 0, width)
            CPT_ball3y = noise(location + 150)
            CPT_ball3y = map(CPT_ball3y, 0, 1, 0, width)
            maxXvalCPTball3 = constrain(CPT_ball3x, 0, 1000)
            minYvalCPTball3 = constrain(CPT_ball3y, 0, 600)
            fill(255, 140, 0)
            ellipse(maxXvalCPTball3, minYvalCPTball3, CPTballsize, CPTballsize)

            # CPT ball 4
            CPT_ball4x = noise(location + 80)
            CPT_ball4x = map(CPT_ball4x, 0, 1, 0, width)
            CPT_ball4y = noise(location + 200)
            CPT_ball4y = map(CPT_ball4y, 0, 1, 0, width)
            maxXvalCPTball4 = constrain(CPT_ball4x, 0, 1000)
            minYvalCPTball4 = constrain(CPT_ball4y, 0, 600)
            fill(150, 50, 100)
            ellipse(maxXvalCPTball4, minYvalCPTball4, CPTballsize, CPTballsize)

            # CPT ball1 contact
            radius_ball = ball_size / 2
            radius_ball2 = CPTballsize / 2
            CPT_ball1x_value = CPT_ball1x - player_ballx
            CPT_ball1y_value = CPT_ball1x - player_bally
            distance = sqrt(CPT_ball1x_value ** 2 + CPT_ball1y_value ** 2)
            if distance <= radius_ball + radius_ball2:
                score = 0
                hit += 1

                if hit > 1:
                    textSize(50)
                    fill(150)
                    text("YOU GOT HIT BY A BALL!!", width/4, height/2)

            # CPT ball2 contact
            radius_ball = ball_size / 2
            radius_ball2 = CPTballsize / 2
            CPT_ball2x_value = CPT_ball2x - player_ballx
            CPT_ball2y_value = CPT_ball2y - player_bally
            distance = sqrt(CPT_ball2x_value ** 2 + CPT_ball2y_value ** 2)
            if distance <= radius_ball + radius_ball2:
                score = 0
                hit += 1

                if hit > 1:
                    textSize(50)
                    fill(150)
                    text("YOU GOT HIT BY A BALL!!", width/4, height/2)

            # CPT ball 3 contact
            radius_ball = ball_size / 2
            radius_ball2 = CPTballsize / 2
            CPT_ball3x_value = CPT_ball3x - player_ballx
            CPT_ball3y_value = CPT_ball3y - player_bally
            distance = sqrt(CPT_ball3x_value ** 2 + CPT_ball3y_value ** 2)
            if distance <= radius_ball + radius_ball2:
                score = 0
                hit += 1

                if hit > 1:
                    textSize(50)
                    fill(150)
                    text("YOU GOT HIT BY A BALL!!", width/4, height/2)

            # CPT ball 4 contact
            radius_ball = ball_size / 2
            radius_ball2 = CPTballsize / 2
            CPT_ball4x_value = CPT_ball4x - player_ballx
            CPT_ball4y_value = CPT_ball4y - player_bally
            distance = sqrt(CPT_ball4x_value ** 2 + CPT_ball4y_value ** 2)
            if distance <= radius_ball + radius_ball2:
                score = 0
                hit += 1

                if hit > 1:
                    textSize(50)
                    fill(150)
                    text("YOU GOT HIT BY A BALL!!", width/4, height/2)

        elif score == 5:
            if keyPressed:
                if key == "m":
                    screen = "menu"
                    score -= 5
            background(255)
            textSize(100)
            fill(random(255), random(255), random(255))
            text("YOU WIN!!!", width/4, height/2)
            textSize(25)
            text("press [m] to return to main menu", width/4, height/2 + 290)


def mousePressed():

    global score
    global ball_size
    global player_ballx
    global player_bally

    radius = ball_size / 2.0
    distance_x = abs(mouseX - player_ballx)
    distance_y = abs(mouseY - player_bally)
    hypotenuse = sqrt(distance_x ** 2 + distance_y ** 2)
    if hypotenuse <= radius:
        score += 1
