# Super-Reso: Satellite Image Super-Resolution Using GANs and Aerial Images

This repository contains the code, trained models, and evaluation scripts associated with the paper:

## Satellite Imagery Super-Resolution Using GANs and Aerial Images

**IEEE Latin America Transactions**, 2026 //
**Manuscript ID:** 10603

### Authors

* **Magda Alexandra Trujillo-Jiménez**¹˒⁵*
* **Francisco Ramiro Iaconis**²
* **Debora Pollicelli**³
* **Gisela Noelia Revollo Sarmiento**⁴
* **Claudio Delrieux**¹

### Affiliations

¹ Laboratorio de Ciencias de las Imágenes (LCI), Departamento de Ciencias e Ingeniería de la Computación (DCIC), Universidad Nacional del Sur (UNS) – CONICET, Bahía Blanca, Argentina

² Instituto de Física del Sur (IFISUR), Departamento de Física, Universidad Nacional del Sur (UNS) – CONICET, Bahía Blanca, Argentina

³ Laboratorio de Investigación en Informática, Departamento de Informática, Universidad Nacional de la Patagonia San Juan Bosco (UNPSJB), Puerto Madryn, Argentina

⁴ Instituto de Ecorregiones Andinas (INECOA-CONICET), Facultad de Ingeniería, Universidad Nacional de Jujuy (UNJu), Jujuy, Argentina

⁵ Instituto Patagónico de Ciencias Sociales y Humanas (IPCSH), CCT CONICET-CENPAT, Puerto Madryn, Argentina

---

## Overview

High-resolution satellite imagery is often expensive, scarce, or unavailable for many regions. This project investigates whether high-resolution aerial orthophotos can be used as an alternative source of training data for satellite image super-resolution.

The proposed approach is based on **Real-ESRGAN**, a GAN-based super-resolution framework fine-tuned using aerial orthophotos and subsequently applied to satellite imagery without domain-specific adaptation.

The study evaluates the transferability of spatial representations learned from aerial imagery to satellite images using structural, perceptual, and color-based metrics.

---


---

## Main Contributions

* Demonstration of **aerial-to-satellite transfer learning** for image super-resolution.
* Use of publicly available aerial orthophotos as a scalable training source.
* Evaluation using multiple quality metrics:

  * SSIM-Y
  * MS-SSIM
  * LPIPS
  * CIEDE2000
* Comparative analysis against Bicubic interpolation and GAN-based super-resolution baselines.

---

## Repository Structure

```text
Super-Reso/
│
├── data/
│   ├── aerial/
│   └── satellite/
│
├── models/
│   ├── pretrained/
│   └── finetuned/
│
├── scripts/
│   ├── train.py
│   ├── inference.py
│   ├── evaluate.py
│   └── metrics.py
│
├── results/
│   ├── figures/
│   └── tables/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

## Dataset

### Aerial Orthophotos

Training was performed using high-resolution aerial orthophotos provided by the Institut Cartogràfic i Geològic de Catalunya (ICGC), with a native spatial resolution of **25 cm/pixel**.

Low-resolution images were generated synthetically through area-based downsampling:

| Scale | Resolution   |
| ----- | ------------ |
| ×2    | 50 cm/pixel  |
| ×4    | 100 cm/pixel |

A total of **1,418 image patches (512 × 512 pixels)** were extracted using a sliding-window strategy.

### Satellite Images

Satellite imagery was acquired from **SuperView-1** and evaluated using pan-sharpened products with an effective spatial resolution of **0.5 m/pixel**.

---

## Model

This work is based on:

> Wang et al., *Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data* (ICCV Workshops, 2021)

The network was initialized using the official pre-trained Real-ESRGAN weights and subsequently fine-tuned on aerial imagery.

### Training Configuration

| Parameter     | Value           |
| ------------- | --------------- |
| Architecture  | Real-ESRGAN     |
| Generator     | RRDBNet         |
| Discriminator | U-Net           |
| Optimizer     | Adam            |
| Learning Rate | 1e-4            |
| Iterations    | 100,000         |
| Batch Size    | 16              |
| GPU           | NVIDIA RTX 4060 |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aletrujim/Super-Reso.git
cd Super-Reso
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Training

To train the model:

```bash
python scripts/train.py
```

Training parameters and dataset paths can be configured in the corresponding configuration files.

---

## Inference

To generate super-resolved images:

```bash
python scripts/inference.py \
    --input data/test \
    --output results
```

---

## Evaluation

To compute quantitative metrics:

```bash
python scripts/evaluate.py
```

Metrics reported in the paper include:

* SSIM-Y
* MS-SSIM
* LPIPS
* CIEDE2000

---

## Results

The proposed model demonstrates that high-resolution aerial imagery can be used to learn transferable spatial representations that improve the perceptual quality of satellite image super-resolution.

The approach achieves competitive structural performance while significantly improving perceptual quality, supporting the feasibility of aerial-to-satellite transfer learning for remote sensing applications.

---

## Reproducibility

To ensure reproducibility:

* Fixed random seeds were used during training.
* Training and testing data were separated at image level.
* Patch extraction was performed using a fixed sliding-window protocol.
* All experiments were conducted using the same training configuration described in the manuscript.

---

## Citation

If you use this repository in your research, please cite:

```bibtex
@article{
 coming soon...
}
```

---

## License

This repository is released for academic and research purposes.

If you use this code, models, or derived results, please cite the associated publication.

---

## Contact

For questions, suggestions, or collaborations, please open an issue in this repository.
