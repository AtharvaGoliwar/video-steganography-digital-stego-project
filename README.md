Digital Watermarking and Steganography Project
This project demonstrates a deep learning approach to video steganography. It provides scripts to hide a "secret" video within a "cover" video and subsequently extract the secret video, leaving the cover video visually unaltered.
Prerequisites
Before you begin, please ensure you have the following software installed:
Python 3.8 or newer. You can check your version by opening a terminal and running python --version.
Git for cloning the repository.
Access to a command line interface (Terminal on macOS/Linux, or Command Prompt/PowerShell on Windows).
Setup and Installation
Follow these steps to set up the project environment on your local machine.

1. Clone the Repository
   Open your terminal and clone this repository to your desired location (e.g., your Desktop).
   code
   Bash
   git clone <your-repository-url>
   Replace <your-repository-url> with the actual URL of your GitHub repository.
2. Navigate to the Project Directory
   Change your current directory to the newly cloned project folder.
   code
   Bash
   cd <repository-folder-name>
3. Create and Activate a Virtual Environment
   It is highly recommended to use a virtual environment to keep project dependencies isolated.
   Create the environment:
   code
   Bash
   python -m venv venv
   Activate the environment:
   On Windows:
   code
   Powershell
   .\venv\Scripts\activate
   On macOS / Linux:
   code
   Bash
   source venv/bin/activate
   After running the command, your terminal prompt should change to show (venv) at the beginning.
4. Install Dependencies
   Once the virtual environment is active, install all the necessary libraries from the requirements.txt file.
   code
   Bash
   pip install -r requirements.txt
   That's it for setup! You are now ready to run the project.
   How to Run the Project
   The process involves two main scripts: first hiding the video (encoding), then revealing it (decoding). Sample videos are provided in the videos/ folder.
   Part A: Hide the Secret Video (Encoding)
   This step will hide videos/secret.mp4 inside videos/cover.mp4.
   Make sure your virtual environment is still active ((venv) is visible in your terminal).
   Run one of the following commands in your terminal:
   Without shuffle:
   code
   Bash
   python video_hide.py --model models/hide.h5 --secret_video videos/secret.mp4 --cover_video videos/cover.mp4
   With shuffle:
   code
   Bash
   python video_hide.py --model models/hide.h5 --secret_video videos/secret.mp4 --cover_video videos/cover.mp4 --shuffle
   Expected Output:
   You will see a progress bar as it processes the video frames.
   You might see a message like Ignore above cudart dlerror if you do not have a GPU. This is normal and can be ignored.
   When finished, it will print: Successfully encoded video !!!
   A new video file will be created at: results/cover_outvid_224.avi. This is your cover video with the secret video hidden inside.
   Part B: Reveal the Secret Video (Decoding)
   This step will take the encoded video from Part A and extract the original secret video from it.
   In the same terminal, run one of the following commands:
   Without shuffle:
   code
   Bash
   python video_reveal.py --model models/reveal.h5 --container_video results/cover_outvid_224.avi
   With shuffle:
   code
   Bash
   python video_reveal.py --model models/reveal.h5 --container_video results/cover_outvid_224.avi --shuffle
   Expected Output:
   You will see another progress bar.
   When finished, it will print: Successfully decoded video !!!
   The revealed video is saved at: results/secret_outvid_300.avi.
   Viewing the Results
   You have now successfully hidden a video inside another and then recovered it.
5. The Encoded Video
   Navigate to the results/ folder.
   Play the file cover_outvid_224.avi. It should look visually identical to the original cover video (videos/cover.mp4).
6. The Decoded Video
   In the same results/ folder, play the file secret_outvid_300.avi. This should be the secret video (videos/secret.mp4) that you successfully recovered.
7. Test Images
   During the process, two test images named test.png are created in the main project directory. These are single frames saved during the encoding and decoding steps for debugging purposes.
   Thank you for reviewing our project
