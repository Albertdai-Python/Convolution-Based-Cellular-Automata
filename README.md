# Convolution-Based-Cellular-Automata
## A Lenia-like Convolutional Model for Cellular Movement Simulation
**Programmer:** Yu-Cheng Dai

---
### Project Introduction & Motivation
*What if humans could create digital life?*\
This project is inspired by Conway's Game of Life, which consists of a two-dimensional grid where cells (classified as "alive" or "dead" depending on neighboring cells) evolve through generations via a 3x3 kernel. However, its square kernel shape and its discrete cell states do not provide an accurate cell simulation. This project uses Gaussian kernels similar to Bert Chan's Lenia to perform convolution and predict the next time step.

---
### Achieved Results (Videos included in Media folder)
Initially, experimentation started with 3x3 square kernels, which produced cells that move in one direction but oscillate similarly to the original Conway "Pulsar."

Further kernel tweaks led to a vertically expanding group of cells.

5x5 Gaussian kernels produced colonies that were able to grow in size independently.

After adjusting to significantly larger kernels (17x17), smooth, stable gliders that maintained their overall shapes throughout evolution appeared.

---
### Future Directions
- Add multiple channels to simulate different aspects of the environment (chemical gradients, force fields, etc.)
- Integrate neural networks to adjust kernels and produce different stable "organisms"
- Implement reproduction and genetic inheritance
- Incorporate feeding and sensory behaviors

---
### Python Module Requirements
- numpy
- matplotlib
- scipy

---
### Detailed Functions
- Self-programmed, Wrap-around Convolution Function
  - Scales existing matrices in 8 directions to allow continuous cell movement after crossing the border
  - Implements a differential equation by using a small time step to simulate continuous cell movement
- Different Initial Cell State Configurations
  - Allows random generation to simulate stable patterns during long time periods
  - Creates circular rings to generate glider patterns
  - Allows random generation with a threshold to simulate colony growth
- Matplotlib-powered Animation Generation

---
### References
- Bert Wang-Chak Chan; July 13–18, 2020. "Lenia and Expanded Universe." Proceedings of the ALIFE 2020: The 2020 Conference on Artificial Life. ALIFE 2020: The 2020 Conference on Artificial Life. Online. (pp. pp. 221-229). ASME. https://doi.org/10.1162/isal_a_00297
