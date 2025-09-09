import ffmpeg
import os

main_video = 'mallocScreenShare.mp4'
overlay_video = 'malloc_face.mp4'  
output_video = 'output_overlay.mp4'

main_size = (720, 480)
overlay_size = (180, 102)

main_video_offset = 618.5 

process_duration = 4860  

(
    ffmpeg
    .input(main_video, ss=main_video_offset, t=process_duration)
    .output('main_scaled.mp4', vf=f'scale={main_size[0]}:{main_size[1]}', vcodec='libx264', an=None)
    .run(overwrite_output=True)
)

(
    ffmpeg
    .input(overlay_video, t=process_duration)
    .output('overlay_scaled.mp4', vf=f'scale={overlay_size[0]}:{overlay_size[1]}', vcodec='libx264', acodec='aac', strict='experimental')
    .run(overwrite_output=True)
)

main_in = ffmpeg.input('main_scaled.mp4')
overlay_in = ffmpeg.input('overlay_scaled.mp4')


(
    ffmpeg
    .filter([main_in.video, overlay_in.video], 'overlay', 0, 0)
    .output(
        output_video,
        vcodec='libx264',
        acodec='aac',
        strict='experimental',
        map='1:a' 
    )
    .run(overwrite_output=True)
)

print(f'Overlay complete. Output saved as {output_video}')

for f in ['main_scaled.mp4', 'overlay_scaled.mp4']:
    try:
        os.remove(f)
        print(f"Deleted intermediate file: {f}")
    except Exception as e:
        print(f"Could not delete {f}: {e}")