# A Latent Diffusion Model for Style and Content Controlled Handwriting Generation - WIP

This is a final coding project for CPSC 440, 2025 Winter Term 2. We base our work off of [DiffusionPen](https://github.com/koninik/DiffusionPen).

Download the [IAM Handwriting dataset](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database), place it in `DiffusionPen-modified/iam_data` (extracted).

Download saved model weights following the original instructions from DiffusionPen. You should have:
  DiffusionPen-mod/diffusionpen_iam_model_path/
	DiffusionPen-mod/iam_data/
	DiffusionPen-mod/saved_iam_data/
	DiffusionPen-mod/style_models/
To sample single words with the model weights pre-trained on IAM:
```
cd DiffusionPen-modified \

python train.py --save_path ./diffusionpen_iam_model_path --style_path ./style_models/iam_style_diffusionpen.pth --train_mode sampling --sampling_mode single_sampling
```

The main modified script is `train_sd3m.py`. To train:
```
python train_sd3m.py --epochs 1000 --model_name diffusionpen --save_path diffusionpen_iam_sd3m_model_path/
```

Some image samples we've generated and saved are in the `image_samples/` and `image_samples_sd3m/` folders.

---
Extra notes: the original DiffusionPen repo is missing a `requirements.txt`, which we add in here, but some packages needed in the environment may still be missing from the list. Setup with huggingface also required.
