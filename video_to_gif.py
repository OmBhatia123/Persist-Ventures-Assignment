import os
from moviepy.editor import VideoFileClip

def video_to_gif(video_path, gif_path, start_time, end_time):
    # Convert a segment of a video to a GIF.
    try:
        clip = VideoFileClip(video_path).subclip(start_time, end_time)
        clip.write_gif(gif_path)
        print(f"Successfully created GIF: {gif_path}")
    except Exception as e:
        print(f"Error processing {video_path}: {e}")

def process_videos_in_directory(directory):
    # Process all videos in the specified directory to GIFs
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith("video.mp4"):  # You can add more video formats if needed
            video_path = os.path.join(directory, filename)
            gif_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.gif")
            video_to_gif(video_path, gif_path, 0, 20)  # Example: first 20 seconds
            
# Example usage
video_directory = 'videos'  # Directory containing your videos
process_videos_in_directory(video_directory)
