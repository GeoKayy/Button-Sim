import pygame
import random
import os

    ########## setup ###########
if not os.path.isfile("buttonsimhs.txt"):
    f = open("buttonsimhs.txt", "x")
    f = open("buttonsimhs.txt", "a")
    f.write("0")
    f.close()
if not os.path.isfile("buttonsimhsnumber.txt"):
    f = open("buttonsimhsnumber.txt", "x")
    f = open("buttonsimhsnumber.txt", "a")
    f.write("0")
    f.close()
pygame.init()
black = (0, 0, 0)
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
number = 0
mouseX = 0
mouseY = 0
loops = 0
average = 0
nums = []
pygame.display.set_caption("Button Simulator")
icon = pygame.image.load("button.png")
pygame.display.set_icon(icon)
highestnum = 0
showloops = False
showchance = False
showavg = False
hsFile = "buttonsimhs.txt"
hsnumFile = "buttonsimhsnumber.txt"
highscores = open(hsFile, "r").readlines()
highscoresnum = open(hsnumFile, "r").readlines()

    ############### reset chance calculator ########

def chanceofreset(n):
    chanceofnotreset = 1.0
    for i in range(1, n):
        chanceofnotreset *= (100 - i) / 100
    return str(round(100-round((1.0 - chanceofnotreset)*100,4),3))+"% chance!"
totalchance = chanceofreset(highestnum)

    ############ set font #################

numFont = pygame.font.SysFont("Times New Roman", 180)
genFont = pygame.font.SysFont("Times New Roman", 30)
showFont = pygame.font.SysFont("Times New Roman", 20)

    ########## render number #############

numDisplay = numFont.render(str(number), 1, black)
highnumDisplay = genFont.render(str(highestnum), 1, black)
loopsDisplay = genFont.render(str(loops), 1, black)
showloopsDisplay = showFont.render("Show loops:", 1, black)
chanceDisplay = genFont.render(str(totalchance), 1, black)
showchanceDisplay = showFont.render("Show chance of highscore:", 1, black)
hsDisplay = showFont.render(highscores[0], 1, black)
avgDisplay = genFont.render(str(round(average,2)), 1, black)
showavgDisplay = showFont.render("Show average:", 1, black)

    ######### main loop ############

mouse_button_down = False
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse is clicked
            mouse_button_down = True
        elif event.type == pygame.MOUSEBUTTONUP: # checks if mouse isnt clicked
            mouse_button_down = False
            mousepos = pygame.mouse.get_pos() # sets mouse pos
            mouseX, mouseY = mousepos

            if number < random.randint(1, 99) and mouseX < 555 and mouseX > 245 and mouseY < 455 and mouseY > 145: # if n is lower than a random number 1-99 then add 1 to n
                number += 1
                if highestnum < number: ### updates highscore
                    highestnum = number
                    totalchance = chanceofreset(highestnum)
                    if highestnum > int(highscoresnum[0]):
                        with open(hsnumFile, "w") as file: # write to buttonsimhsnumber.txt
                            file.write(str(highestnum))
                        with open(hsFile, "w") as file: # write to buttomsimhs.txt
                            file.write("The highscore for Button Sim is currently " + str(number) + ", or a " + str(totalchance))

            else:
                if mouseX < 555 and mouseX > 245 and mouseY < 455 and mouseY > 145:  ##### else reset n
                    nums.append(number)
                    number = 0
                    loops += 1
                    average = 0
                    for count in range(len(nums)): ##### calculate average
                        average += nums[count]
                    average = average/len(nums)
                    
            numDisplay = numFont.render(str(number), 1, black)
            highnumDisplay = genFont.render(("Session highscore: "+str(highestnum)), 1, black)
            loopsDisplay = genFont.render(("Loops: "+str(loops)), 1, black)
            showloopsDisplay = showFont.render("Show loops:", 1, black)
            showchanceDisplay = showFont.render("Show chance of highscore:", 1, black)
            hsDisplay = showFont.render(highscores[0], 1, black)
            chanceDisplay = genFont.render(str(totalchance), 1, black)
            avgDisplay = genFont.render("Average: "+str(round(average,2)), 1, black)
            showavgDisplay = showFont.render("Show average:", 1, black)

        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse is clicked
            mouse_button_down = True
        elif event.type == pygame.MOUSEBUTTONUP: # checks if mouse isnt clicked
            mouse_button_down = False
            mousepos = pygame.mouse.get_pos() # sets mouse pos
            mouseX, mouseY = mousepos
            if mouseX < 790 and mouseX > 770 and mouseY < 50 and mouseY > 30 and showloops == False:
                showloops = True
            elif mouseX < 790 and mouseX > 770 and mouseY < 50 and mouseY > 30 and showloops == True:
                showloops = False
                
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse is clicked
            mouse_button_down = True
        elif event.type == pygame.MOUSEBUTTONUP: # checks if mouse isnt clicked
            mouse_button_down = False
            mousepos = pygame.mouse.get_pos() # sets mouse pos
            mouseX, mouseY = mousepos
            if mouseX < 790 and mouseX > 770 and mouseY < 90 and mouseY > 70 and showchance == False:
                showchance = True
            elif mouseX < 790 and mouseX > 770 and mouseY < 90 and mouseY > 70 and showchance == True:
                showchance = False
                
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if mouse is clicked
            mouse_button_down = True
        elif event.type == pygame.MOUSEBUTTONUP: # checks if mouse isnt clicked
            mouse_button_down = False
            mousepos = pygame.mouse.get_pos() # sets mouse pos
            mouseX, mouseY = mousepos
            if mouseX < 790 and mouseX > 770 and mouseY < 130 and mouseY > 110 and showavg == False:
                showavg = True
            elif mouseX < 790 and mouseX > 770 and mouseY < 130 and mouseY > 110 and showavg == True:
                showavg = False

    ########### update screen ################

        screen.fill((255, 255, 255)) # clears screen
        pygame.draw.circle(screen, (220,220,220), (780, 120), 10, 1000) ### renders show average button
        if showavg == True:
                pygame.draw.circle(screen, (128,128,128), (780, 120), 7, 1000) 
        pygame.draw.circle(screen, (220,220,220), (780, 40), 10, 1000) ### renders show loop button
        if showloops == True:
            pygame.draw.circle(screen, (128,128,128), (780, 40), 7, 1000) 
        pygame.draw.circle(screen, (220,220,220), (780, 80), 10, 1000) ### renders show chance button
        if showchance == True:
            pygame.draw.circle(screen, (128,128,128), (780, 80), 7, 1000) 
        pygame.draw.circle(screen, (0,0,0), (400, 300), 155, 1000) #### renders big button
        pygame.draw.circle(screen, (255,0,0), (400, 300), 150, 1000)
        if number < 10: # centering number
            screen.blit(numDisplay, (350, 200))
        else:
            screen.blit(numDisplay, (300, 200))
        screen.blit(highnumDisplay, (290,100)) ###### show highscore
        screen.blit(showloopsDisplay, (660 ,25)) #### show loops
        screen.blit(showchanceDisplay, (540,65)) #### show chance of session hs
        screen.blit(showavgDisplay, (640,105)) #### show avg

        screen.blit(hsDisplay, (150,550)) ### show hs

        if showchance == True: ################### layering loops, chance, avg
            screen.blit(chanceDisplay, (320,70))
        if showloops == True and showchance == True:
            screen.blit(loopsDisplay, (345,40))
        elif showloops == True:
            screen.blit(loopsDisplay, (345,70))
        if showavg == True:
            if showloops == True and showchance == True:
                screen.blit(avgDisplay, (320,10))
            elif showloops == True or showchance == True:
                screen.blit(avgDisplay, (320, 40))
            else:
                screen.blit(avgDisplay, (320, 70))
        pygame.display.flip() ###### update screen

