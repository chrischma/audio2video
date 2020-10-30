import os

audio = input("Drop your Audio File here: ")
image = input("Drop your image here:")

input_name = audio.split(".")
output_name = input_name[0]+".mp4"
command = f'''ffmpeg -y -loop 1 -framerate 2 -i {image} -i {audio}  -c:v libx264 -tune stillimage -c:a aac -b:a 320k -shortest -fflags +shortest -max_interleave_delta 100M {output_name}
'''

os.system(command)

print(f' \n Your file is ready. You find it here: \n {output_name} \n \n Have a nice day!')
