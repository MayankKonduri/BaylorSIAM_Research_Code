# Cerebral Tumor Quantitative Simulation Project Summary (April 2023 - October 2024)

# Abstract
## Overview

This project addresses the challenge of **inverse parameter identification** in semi-linear parabolic partial differential equations (PDEs), with a particular focus on applications in **tumor growth modeling**. Our goal is to accurately estimate model parameters from noisy observational data, which is essential for improving the predictive accuracy of tumor growth simulations.

## Motivation

Traditionally, parameter identification in such PDE models has relied on **variational techniques**. While effective, these methods can be sensitive to noise, limiting their robustness when working with real-world data. To overcome this, we introduce a **data-driven approach** using **dense neural networks (DNNs)**, which are trained to map noisy observations directly to the desired model parameters.

## Objectives

- Develop a framework for parameter estimation in semi-linear parabolic PDEs.
- Improve robustness to noise in observational data by utilizing DNNs.
- Construct a data-driven reconstruction map for direct mapping from observations to parameters.

## Methodology

1. **Modeling Tumor Growth:**  
   - Formulate the tumor growth dynamics using semi-linear parabolic PDEs.

2. **Data-Driven Reconstruction:**  
   - Employ Dense Neural Networks (DNNs) to learn a mapping from noisy observations to model parameters.
   - The DNN effectively serves as a reconstruction map, bypassing traditional iterative or variational methods.

3. **Training and Validation:**  
   - Generate synthetic data under controlled noise levels for training the DNN.
   - Validate the model's performance in parameter identification using additional noisy data.

## Key Innovations

- **DNN-Based Parameter Identification:** 
   - This approach leverages neural networks for direct parameter recovery, which enhances robustness against noise in observational data.
- **Non-Iterative Solution Framework:** 
   - By constructing a direct map, we bypass iterative methods, aiming for faster and potentially more accurate parameter estimation.

## Applications

This framework has potential applications in:
- **Biomedical Modeling:** Accurate modeling of tumor growth dynamics, improving treatment planning and prediction.
- **Inverse Problem Solving:** Provides a template for parameter identification in other semi-linear parabolic PDE models in fields like environmental science and materials science.


## Conference Poster
![Screenshot 2024-11-05 at 8 40 46 PM](https://github.com/user-attachments/assets/c0e91500-fb08-4c13-b943-b32e09cbe005)
[mayank_sciml_poster.pdf](https://github.com/user-attachments/files/17637383/mayank_sciml_poster.pdf)

## References

[1]  A. Mang A. Gholami and G. Biros. *An inverse problem formulation forparameter estimation of a reaction-diffusion model for low-grade gliomas.* Journal of Mathematical Biology, 72(1):409–433, 1996.

# Running the Code

To install the required libraries, run:

```bash
pip install torch torchvision torchaudio torch-geometric networkx matplotlib
git clone https://github.com/yourusername/UniversityOfHouston_BaylorSIAM_Research_Code
ls
python3 [Code To Be Compiled]

