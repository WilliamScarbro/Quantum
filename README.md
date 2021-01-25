# Quantum Computer Simulation

This quantum simulator is based on the mathematical framework descirbed in Quantum Computing for Computer Scientists.
This simulator provides models for:
* One particle systems of n states
* Multi particle systems of n states
* Quantum Computers (multi particle systems of 2 states)

Several quantum gates have been provided which can be used to program the quantum computer.

## Contents:

*QuantumComputer.ipynb* - jupyter notebook containing quantum computer
*circles.py* - bloch circle visualization library

### Libraries: 
python 3.6.9
jupyter 5.7.8
numpy 1.19.4
ipycanvas 0.8.2 - required for bloch circle visuals

(These specific versions are not necessarily required, but these are the version I am running)

For ipycanvas to work, the result of ```$ jupyter nbextensions list``` should be 

```
Known nbextensions:
  config dir: /usr/etc/jupyter/nbconfig
    notebook section
      ipycanvas/extension  enabled 
      - Validating: OK
  config dir: /usr/local/etc/jupyter/nbconfig
    notebook section
      jupyter-js-widgets/extension  enabled 
      - Validating: OK
```
