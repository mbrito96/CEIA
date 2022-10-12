# # # Consigna TP5
# Parte 1:
# Implementar el detector de fondo naive usando la mediana como
# estimador El algoritmo debe recibir el parámetro N (cantidad de
# frames utilizados para la estimación) y el intervalo de tiempo para
# recalcular el fondo

# Parte 2:
# Se deben generar las mascaras de foreground y aplicarlas a los frames
# para segmentar los objetos en movimiento

# Parte 3:
# Comparar con alguno de los métodos vistos en la practica basados en
# mezcla de gaussianas

# importing libraries
from types import NoneType
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Naive background substraction')
parser.add_argument('-F', type=int, help='Cantidad de frames utilizados para la estimacion')
parser.add_argument('-S', type=int, help='Segundos para recalcular el fondo')

args = parser.parse_args()
variables = vars(args)
print(variables['F'])
bkg_n_frames = variables['F']	# Number of frames to use when calculating the background
bkg_sec_recalc = variables['S']	# Seconds between background calculations

# while(1):
#     pass
# Create a VideoCapture object and read from input file
videos = ['slow_traffic_small.mp4', 'vtest.mp4']
cap = cv.VideoCapture(videos[1])

# Check if camera opened successfully
if (cap.isOpened()== False):
	print("Error opening video file")

frame_count = cap.get(cv.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv.CAP_PROP_FPS)
length_s = frame_count / fps
print(f'Frame count= {frame_count} ; FPS= {fps} ; Length(s)= {length_s}')

# Radio para la ventana espacial
sp = 20
# Radio para la ventana color
sr = 40

cap.set(cv.CAP_PROP_POS_FRAMES, 0)	# Start the video from the beginning
while(cap.isOpened()):
	ret, frame = cap.read()
	curr_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
	if ret == True:
		img_out=cv.pyrMeanShiftFiltering(frame, sp, sr, maxLevel = 3)
		
		cv.imshow('Frame', img_out)

		
		if cv.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv.destroyAllWindows()