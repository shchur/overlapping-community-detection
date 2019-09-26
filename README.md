# Overlapping Community Detection with Graph Neural Networks

Pytorch implementation of the **Neural Overlapping Community Detection** method from
["Overlapping Community Detection with Graph Neural Networks"](http://www.kdd.in.tum.de/nocd).

## Usage
The main algorithm and other utilities are implemented in the `nocd` package that can be installed as
```bash
python setup.py install
```
A Jupyter notebook `interactive.ipynb` contains the code for training the model and analyzing the results.

Experiments in the paper have been performed using an older TensorFlow version of the code that can be found 
[here](https://figshare.com/s/30894e4172505d5dc070).

## Requirements
```
numpy=1.16.4
pytorch=1.2.0
scipy=1.3.1
```

## Cite
Please cite our paper if you the code or datasets in your own work
```
@article{
    shchur2019overlapping,
    title={Overlapping Community Detection with Graph Neural Networks},
    author={Oleksandr Shchur and Stephan G\"{u}nnemann},
    journal={Deep Learning on Graphs Workshop, KDD},
    year={2019},
}
```
