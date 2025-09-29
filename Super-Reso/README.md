# Super-Resolution

Super resolution based on ESRGAN (https://github.com/xinntao/BasicSR)

enviroment: conda activate sres
 
## Usage

1. Install the packages that are in requeriments.txt 

	original sizes:
   leida1: (15715x12261 px)
   leida2: (13480x14564 px)

2. Run imgs2lowres.py to get crops (512x512) and crops_lowres (128x182)

3. Run change_size.py to get all images to the same size (512x512 px)

3. Run change_ext.py to get all images to have the same extension ".jpg"
   


### Train

1. Set the dir in train.py

> hr_path: The path list of imgs with high resolution.

> lr_path: The path of imgs with low resolution.

Changes in train:

> batch_size = 2

> num-workers = 0

2. Run python train.py

### Train optimized

1. Change parameters (train2.py)

> batch_size = 1
> gpu_ids = '0,1,2,3,4'
> niter = 1000

2. Run python train2.py (multiple)


### Pretrained models

1. Select weights 

check_points/ESRGAN-V1/

2. Copy in results

> results/90000_G.pth 


### Test

1. Set 'pretrain_model_G' in test.py / test_folder.py

3. RUN python test.py / test_folder.py


### Test satellitales crops

Path: RGB_vertederos_recortes 
original sizes: 615x615 px

1. Run imgs2lowres.py to get crops (512x512) and crops_lowres (128x182)

4. Run change_ext.py to get all images to have the same extension ".jpg"

3. RUN python test_folder.py



