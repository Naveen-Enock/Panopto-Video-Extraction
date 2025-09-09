# Panopto Video Extraction (Overlay Composer)

This mini-tool stitches together a Panopto-style screen recording and a face-cam overlay using **ffmpeg-python**. It:

1. trims and scales the **main** video,
2. scales the **overlay** video,
3. overlays the face-cam on top of the main video at `(0, 0)`,
4. keeps the **overlay video's audio** (by default),
5. cleans up intermediate files.

---

## What the script does

Given two input files:

- `mallocScreenShare.mp4` — the main screen recording  
- `malloc_face.mp4` — the face-cam recording

the script:

- Starts the main video at **618.5s** and processes **4860s** (`~81 min`)  
- Scales the main video to **720×480**  
- Scales the overlay to **180×102**  
- Places the overlay at the **top-left corner**  
- Exports `output_overlay.mp4` (H.264 video + AAC audio)  
- Removes temp files: `main_scaled.mp4`, `overlay_scaled.mp4`

Audio comes from the overlay clip (`map='1:a'`).

---

## Requirements

- **Python 3.9+**
- **ffmpeg** installed and on your `PATH`  
  - macOS: `brew install ffmpeg`  
  - Ubuntu/Debian: `sudo apt-get install ffmpeg`  
  - Windows: download a static build and add the `bin` folder to `PATH`
- Python packages:
  ```bash
  pip install ffmpeg-python
