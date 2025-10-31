
# 🎥 Digital Watermarking and Steganography Project

This project demonstrates a **deep learning approach to video steganography**.  
It provides scripts to hide a **secret video** within a **cover video** and subsequently extract the secret video — leaving the cover video visually unaltered.

---

## 🧩 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8 or newer**  
  _(Check your version using: `python --version`)_
- **Git** for cloning the repository
- **Command Line Interface** (Terminal, Command Prompt, or PowerShell)

---

## ⚙️ Setup and Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```


> Replace `<your-repository-url>` with the actual GitHub repository link.

---

### 2. Navigate to the Project Directory

```bash
cd <repository-folder-name>
```

---

### 3. Create and Activate a Virtual Environment

It’s recommended to use a virtual environment to keep project dependencies isolated.

**Create the environment:**

```bash
python -m venv venv
```

**Activate the environment:**

- On **Windows**:

  ```powershell
  .\venv\Scripts\activate
  ```

- On **macOS / Linux**:

  ```bash
  source venv/bin/activate
  ```

After activation, your terminal prompt should display `(venv)` at the start.

---

### 4. Install Dependencies

Once your environment is active, install all required libraries:

```bash
pip install -r requirements.txt
```

✅ That’s it for setup! You’re now ready to run the project.

---

## 🚀 How to Run the Project

The project includes two main parts:

1. **Hiding (Encoding)** a secret video inside a cover video
2. **Revealing (Decoding)** the hidden secret video

Sample videos are available in the `videos/` folder.

---

### 🕵️ Part A: Hide the Secret Video (Encoding)

This step hides `videos/secret.mp4` inside `videos/cover.mp4`.

Ensure your virtual environment `(venv)` is active.

**Run the following command:**

- Without shuffle:

  ```bash
  python video_hide.py --model models/hide.h5 --secret_video videos/secret.mp4 --cover_video videos/cover.mp4
  ```

- With shuffle:

  ```bash
  python video_hide.py --model models/hide.h5 --secret_video videos/secret.mp4 --cover_video videos/cover.mp4 --shuffle
  ```

#### 🧾 Expected Output:

- A progress bar appears as frames are processed.

- You may see a message like:

  ```
  Ignore above cudart dlerror
  ```

  _(This is normal if you don’t have a GPU.)_

- Once complete, you’ll see:

  ```
  Successfully encoded video !!!
  ```

- A new file `results/cover_outvid_224.avi` will be created — your **cover video with the secret hidden inside.**

---

### 🔍 Part B: Reveal the Secret Video (Decoding)

This step extracts the hidden video from the encoded cover video.

**Run one of the following:**

- Without shuffle:

  ```bash
  python video_reveal.py --model models/reveal.h5 --container_video results/cover_outvid_224.avi
  ```

- With shuffle:

  ```bash
  python video_reveal.py --model models/reveal.h5 --container_video results/cover_outvid_224.avi --shuffle
  ```

#### 🧾 Expected Output:

- Another progress bar appears.
- When done, you’ll see:

  ```
  Successfully decoded video !!!
  ```

- The recovered secret video is saved at:

  ```
  results/secret_outvid_300.avi
  ```

---

## 🖥️ Viewing the Results

You’ve now successfully hidden and revealed a video using deep learning!

### 🎬 1. Encoded Video

- Navigate to the `results/` folder.
- Play **`cover_outvid_224.avi`** — it should look identical to the original cover video (`videos/cover.mp4`).

### 🕶️ 2. Decoded (Recovered) Video

- In the same folder, play **`secret_outvid_300.avi`** — this is your recovered secret video.

### 🧠 3. Debug Test Images

During the process, two test frames (`test.png`) are created for debugging — one during encoding and one during decoding.

---

## 🙏 Acknowledgements

Thank you for reviewing our project!
We hope it helps you understand the power of **Deep Learning in Digital Watermarking and Steganography**.

---

```


