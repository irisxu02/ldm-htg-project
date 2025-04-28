import os
import torch
import torchvision.utils as vutils
from PIL import Image

def save_single_images(images, save_path, args):
    """
    Save a batch of images as a grid or individually.
    
    Args:
        images (torch.Tensor): Tensor of images (N, C, H, W) in [-1, 1] or [0, 1] range.
        save_path (str): Path to save the image.
        args: Args object, can contain information like whether to normalize or not.
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    if isinstance(images, list):
        images = torch.stack(images)

    # If images are in [-1, 1], rescale to [0, 1]
    if images.min() < 0:
        images = (images + 1) / 2

    # Optional: clamp to [0, 1]
    images = images.clamp(0, 1)

    # Save as a grid
    grid = vutils.make_grid(images, nrow=4, padding=2, normalize=False)
    ndarr = grid.mul(255).byte().permute(1, 2, 0).cpu().numpy()
    img = Image.fromarray(ndarr)
    img.save(save_path)