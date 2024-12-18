general
five_landmark = hand_landmarks.landmark[5]
                x5 = five_landmark.x
                y5 = five_landmark.y
                z5 = five_landmark.z
                # print("x =", x5, ", y =", y5,)
                seven_landmark = hand_landmarks.landmark[4]
                x4 = seven_landmark.x
                y4 = seven_landmark.y
                z4 = five_landmark.z
                # print("x =", x7, ", y =", y7,)
                five_landmark = hand_landmarks.landmark[8]
                x8 = five_landmark.x
                y8 = five_landmark.y
                z8 = five_landmark.z
                # print("x =", x5, ", y =", y5,)
                seven_landmark = hand_landmarks.landmark[20]
                x20 = seven_landmark.x
                y20= seven_landmark.y
                z20 = five_landmark.z
                # print("x =", x7, ", y =", y7,)
                five_landmark = hand_landmarks.landmark[17]
                x17 = five_landmark.x
                y17= five_landmark.y
                z17= five_landmark.z



if y8 > y5 and y20 > y17 :
    print('close')
    hand_state == 0

else:
    print('open')
    hand_state == 1


hi(tilt right)
if y8 < y5 and y4 > y5 * 1.05:
    text = "Hi!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (0, 255, 0)  # Green
    thickness = 3
    position = (50, 100)  # (x, y) position for the text
    cv2.putText(image, text, position, font, font_scale, font_color, thickness)

i

five_landmark = hand_landmarks.landmark[8]
x5 = five_landmark.x
y5 = five_landmark.y
z5 = five_landmark.z
# print("x =", x5, ", y =", y5,)
seven_landmark = hand_landmarks.landmark[5]
x8 = seven_landmark.x
y8 = seven_landmark.y
z8 = seven_landmark.z
# print("x =", x7, ", y =", y7,)

if z5 >= z8 * 0.85:
    text = "u"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (0, 255, 0)  # Green
    thickness = 3
    position = (50, 100)  # (x, y) position for the text
    cv2.putText(image, text, position, font, font_scale, font_color, thickness)

you

five_landmark = hand_landmarks.landmark[5]
x5 = five_landmark.x
y5 = five_landmark.y
z5 = five_landmark.z
# print("x =", x5, ", y =", y5,)
seven_landmark = hand_landmarks.landmark[8]
x8 = seven_landmark.x
y8 = seven_landmark.y
z8 = seven_landmark.z
# print("x =", x7, ", y =", y7,)

if z8 * -1 >= z5 * -1.3 and z8 * -1 >= z5 * -0.001:
    text = "Hi!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (0, 255, 0)  # Green
    thickness = 3
    position = (50, 100)  # (x, y) position for the text
    cv2.putText(image, text, position, font, font_scale, font_color, thickness)
pointer :
eight_landmark = hand_landmarks.landmark[8]
x8= eight_landmark.x
y8 = eight_landmark.y

help(tilt right)

four_landmark = hand_landmarks.landmark[4]

y4 = four_landmark.y

# print("x =", x5, ", y =", y5,)
three_landmark = hand_landmarks.landmark[3]

y3 = three_landmark.y
ab = 2 * y3
if y3 < y4:
    print('help')


 please








