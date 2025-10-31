import os
import numpy as np
import tensorflow.compat.v1 as tf # Ensure TF2 compatability
tf.disable_v2_behavior()
import keras
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt

# --- Configuration ---
# 1. UPDATE this path to your trained model file.
MODEL_PATH = 'checkpoints/steg_model-04-0.03.hdf5' 

# 2. UPDATE these paths to the images you want to use.
SECRET_IMAGE_PATH = 'secret.png' # The image you want to hide
COVER_IMAGE_PATH = 'cover.png'   # The image that will hide the secret

# 3. Directory to save the output images.
OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)


# --- Helper Functions (Copied from your train.py) ---
# These functions are REQUIRED to load the model and process the images correctly.

def normalize_batch(imgs):
    '''Performs channel-wise z-score normalization'''
    return (imgs - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])

def denormalize_batch(imgs, should_clip=True):
    '''Denormalize the images for prediction'''
    imgs = (imgs * np.array([0.229, 0.224, 0.225])) + np.array([0.485, 0.456, 0.406])
    if should_clip:
        imgs = np.clip(imgs, 0, 1)
    return imgs

def custom_loss_1(secret, secret_pred):
    '''Dummy loss function for model loading'''
    return keras.losses.mean_squared_error(secret, secret_pred)

def custom_loss_2(cover, cover_pred):
    '''Dummy loss function for model loading'''
    return keras.losses.mean_squared_error(cover, cover_pred)

# --- Main Execution ---
if __name__ == "__main__":
    
    # 1. Load the trained model
    print(f"Loading model from: {MODEL_PATH}")
    try:
        model = load_model(
            MODEL_PATH,
            custom_objects={'custom_loss_1': custom_loss_1, 'custom_loss_2': custom_loss_2}
        )
        print("Model loaded successfully. ✅")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please ensure the MODEL_PATH is correct and the .hdf5 file is not corrupted.")
        exit()

    # 2. Load and preprocess the input images
    print("Loading and preprocessing images...")
    
    # Load secret image
    secret_img = load_img(SECRET_IMAGE_PATH, target_size=(224, 224))
    secret_arr = img_to_array(secret_img) / 255.0
    secret_arr = np.expand_dims(secret_arr, axis=0) # Add batch dimension
    
    # Load cover image
    cover_img = load_img(COVER_IMAGE_PATH, target_size=(224, 224))
    cover_arr = img_to_array(cover_img) / 255.0
    cover_arr = np.expand_dims(cover_arr, axis=0) # Add batch dimension
    
    # Normalize images for the model
    normalized_secret = normalize_batch(secret_arr)
    normalized_cover = normalize_batch(cover_arr)
    print("Image preprocessing complete.")

    # 3. Run the prediction (the "process phase")
    print("Performing steganography (hiding and revealing)...")
    stego_image_normalized, revealed_secret_normalized = model.predict([normalized_secret, normalized_cover])
    print("Prediction complete.")

    # 4. Post-process the output images to make them viewable
    stego_image = denormalize_batch(stego_image_normalized)
    revealed_secret = denormalize_batch(revealed_secret_normalized)
    
    # Remove batch dimension and convert to uint8 (0-255 range)
    stego_image_final = np.squeeze(stego_image * 255.0).astype(np.uint8)
    revealed_secret_final = np.squeeze(revealed_secret * 255.0).astype(np.uint8)

    # 5. Save the output images
    stego_img_path = os.path.join(OUTPUT_DIR, 'stego_image.png')
    revealed_secret_path = os.path.join(OUTPUT_DIR, 'revealed_secret.png')
    
    plt.imsave(stego_img_path, stego_image_final)
    plt.imsave(revealed_secret_path, revealed_secret_final)
    print(f"Saved stego image to: {stego_img_path}")
    print(f"Saved revealed secret to: {revealed_secret_path}")
    
    # 6. Display the results
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle('Steganography Process Results', fontsize=16)

    # Original Secret
    axes[0, 0].imshow(np.squeeze(secret_arr))
    axes[0, 0].set_title('Input Secret Image')
    axes[0, 0].axis('off')

    # Original Cover
    axes[0, 1].imshow(np.squeeze(cover_arr))
    axes[0, 1].set_title('Input Cover Image')
    axes[0, 1].axis('off')

    # Stego Image (Cover with Secret hidden inside)
    axes[1, 0].imshow(stego_image_final)
    axes[1, 0].set_title('Output Stego Image')
    axes[1, 0].axis('off')
    
    # Revealed Secret
    axes[1, 1].imshow(revealed_secret_final)
    axes[1, 1].set_title('Output Revealed Secret')
    axes[1, 1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()