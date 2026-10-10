# GPU Dive

GPU Dive is a small interactive visual explainer for exploring the hardware and execution hierarchy of an NVIDIA GPU.

It starts with an ASUS Dual GeForce RTX 4070 and lets you progressively look inside the card:

```text
Graphics card → PCB → GPU chip → SM → Execution partition → CUDA core
                                      └→ Block → Warp → Thread
```

The diagram is intentionally simplified for teaching and exploration. Green elements represent physical hardware. Amber elements represent example logical work that can reside on the hardware.

## Live demo

After enabling GitHub Pages for this repository, open:

```text
https://YOUR-GITHUB-USERNAME.github.io/gpu-dive/
```

Replace `YOUR-GITHUB-USERNAME` with your GitHub username.

The page works as a standalone static website and does not require a server, database, build step, or external JavaScript library.

## How to use it

- Click the graphics card to enter the PCB view.
- Click the GPU chip to inspect the GPU and its SMs.
- Click an SM to inspect its execution partitions, caches, shared memory, and example resident blocks.
- Follow a Block to its Warps and then to individual Threads.
- Use the breadcrumb trail, the back button, or `Esc` to move up one level.
- Use the home button to return to the graphics card.
- Use the full-screen button for presentations.

## Run locally

Download or clone the repository, then open `index.html` directly in a browser. No installation is required.

You can also serve the folder with any static web server:

```bash
python3 -m http.server
```

Then open `http://localhost:8000`.

## Embed in another website

Copy `gpu-dive.js` into your website and add the custom element:

```html
<gpu-dive
  style="display:block; width:100%; height:760px; border-radius:20px; overflow:hidden;">
</gpu-dive>
<script src="/path/to/gpu-dive.js"></script>
```

The component uses Shadow DOM, so its internal styles are isolated from the host page. It automatically switches to a vertical layout on narrow screens.

An iframe is also possible:

```html
<iframe
  src="https://YOUR-GITHUB-USERNAME.github.io/gpu-dive/"
  title="GPU Dive"
  style="width:100%; height:760px; border:0; border-radius:20px;"
  allow="fullscreen">
</iframe>
```

## Optional change event

The component emits a `gpu-dive:change` event whenever the current level changes:

```js
document.querySelector('gpu-dive').addEventListener('gpu-dive:change', (event) => {
  console.log(event.detail.level);
  console.log(event.detail.path);
});
```

## Scope and accuracy

This is an educational visualization, not an exact PCB photograph or silicon floorplan. The SM layout, cache arrays, memory cells, execution partitions, and resident blocks are schematic. The shown RTX 4070 has 5,888 CUDA cores; the visualization uses 46 enabled SMs with 128 CUDA cores per SM as an illustrative Ada-based organization.

The UI separates L1 cache, Shared Memory, L2 cache, registers, and Global Memory by their programming and hardware roles. On Ada GPUs, L1 cache and Shared Memory can share a physical storage pool even though they are presented separately here for clarity.

## Sources

- [ASUS Dual GeForce RTX 4070](https://www.asus.com/motherboards-components/graphics-cards/dual/dual-rtx4070-12g/)
- [NVIDIA Ada GPU Architecture](https://images.nvidia.com/aem-dam/Solutions/geforce/ada/nvidia-ada-gpu-architecture.pdf)
- [NVIDIA Ada Tuning Guide](https://docs.nvidia.com/cuda/ada-tuning-guide/)
- [NVIDIA CUDA Programming Model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)

## License and image attribution

The ASUS product image is used as an attributed reference image for this educational demo. Check the original ASUS page for its product-image terms before redistributing the image in another project.
